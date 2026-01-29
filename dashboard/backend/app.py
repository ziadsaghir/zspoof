#!/usr/bin/env python3
"""
ZSPOOF v3.0 - AI-Powered Backend
Professional Flask API with ML integration
"""

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from flask_socketio import SocketIO
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'src'))

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Paths
SCRIPT_DIR = Path(__file__).parent
DASHBOARD_DIR = SCRIPT_DIR.parent
PROJECT_DIR = DASHBOARD_DIR.parent
BIN_PATH = PROJECT_DIR / "bin" / "core_engine"
INDEX_HTML = DASHBOARD_DIR / "index.html"

# Try to import ML engine
try:
    from ml_engine import MLMACEngine, AdvancedNetworkAnalyzer
    ML_AVAILABLE = True
    ml_engine = MLMACEngine()
    network_analyzer = AdvancedNetworkAnalyzer()
except ImportError:
    ML_AVAILABLE = False
    ml_engine = None
    network_analyzer = None

@app.route('/')
def index():
    return send_file(INDEX_HTML)

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'operational',
        'timestamp': datetime.now().isoformat(),
        'ml_available': ML_AVAILABLE,
        'engine_available': BIN_PATH.exists()
    })

@app.route('/api/interfaces')
def get_interfaces():
    """Get network interfaces"""
    try:
        # Linux
        result = subprocess.run(['ip', 'link', 'show'], capture_output=True, text=True, timeout=5)
        interfaces = []
        
        for line in result.stdout.split('\n'):
            if ': ' in line and 'state' in line.lower():
                parts = line.split(': ')
                if len(parts) >= 2:
                    name = parts[1].split(':')[0].split('@')[0]
                    if name != 'lo':
                        # Get MAC
                        mac_result = subprocess.run(['cat', f'/sys/class/net/{name}/address'], 
                                                   capture_output=True, text=True, timeout=2)
                        mac = mac_result.stdout.strip() if mac_result.returncode == 0 else 'unknown'
                        
                        # Get state
                        state_result = subprocess.run(['cat', f'/sys/class/net/{name}/operstate'], 
                                                     capture_output=True, text=True, timeout=2)
                        state = state_result.stdout.strip() if state_result.returncode == 0 else 'unknown'
                        
                        interfaces.append({
                            'name': name,
                            'mac': mac,
                            'state': state,
                            'ip': 'N/A'
                        })
        
        return jsonify({'interfaces': interfaces})
    except Exception as e:
        return jsonify({'error': str(e), 'interfaces': []}), 500

@app.route('/api/generate-mac', methods=['POST'])
def generate_mac():
    """Generate MAC with ML intelligence"""
    data = request.json
    profile = data.get('profile', 'random')
    
    if not BIN_PATH.exists():
        return jsonify({'error': 'Engine not compiled'}), 500
    
    try:
        # Use C++ engine
        result = subprocess.run([str(BIN_PATH), profile], capture_output=True, text=True, timeout=5)
        mac = result.stdout.strip()
        
        # Add ML intelligence if available
        if ML_AVAILABLE and ml_engine:
            intelligence = ml_engine.generate_intelligent_mac(profile)
            return jsonify({
                'mac': mac,
                'profile': profile,
                'ml_confidence': intelligence.confidence,
                'ml_reasoning': intelligence.reasoning,
                'ml_risk_level': intelligence.risk_level,
                'timestamp': datetime.now().isoformat()
            })
        else:
            return jsonify({
                'mac': mac,
                'profile': profile,
                'timestamp': datetime.now().isoformat()
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/spoof-mac', methods=['POST'])
def spoof_mac():
    """Apply MAC spoofing"""
    data = request.json
    interface = data.get('interface')
    mac = data.get('mac')
    profile = data.get('profile', 'custom')
    
    if not interface or not mac:
        return jsonify({'error': 'Interface and MAC required'}), 400
    
    try:
        # Linux MAC change
        subprocess.run(['ip', 'link', 'set', 'dev', interface, 'down'], check=True, timeout=5)
        subprocess.run(['ip', 'link', 'set', 'dev', interface, 'address', mac], check=True, timeout=5)
        subprocess.run(['ip', 'link', 'set', 'dev', interface, 'up'], check=True, timeout=5)
        
        socketio.emit('mac_spoofed', {
            'interface': interface,
            'spoofed_mac': mac,
            'profile': profile
        })
        
        return jsonify({
            'success': True,
            'message': 'MAC spoofed successfully',
            'interface': interface,
            'mac': mac
        })
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'error': 'MAC change failed - check permissions'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/scan-network', methods=['POST'])
def scan_network():
    """Network scan (requires scapy)"""
    data = request.json
    interface = data.get('interface')
    ip_range = data.get('ip_range', '192.168.1.0/24')
    
    try:
        from scapy.all import ARP, Ether, srp
        
        arp = ARP(pdst=ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        
        result = srp(packet, timeout=3, verbose=0, iface=interface)[0]
        
        devices = []
        for sent, received in result:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})
        
        socketio.emit('scan_complete', {
            'devices': devices,
            'count': len(devices),
            'ip_range': ip_range
        })
        
        return jsonify({
            'success': True,
            'devices': devices,
            'count': len(devices)
        })
    except ImportError:
        return jsonify({'error': 'Scapy not installed'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/profiles')
def get_profiles():
    """Get available profiles"""
    profiles = [
        {'id': 'corporate', 'name': 'Corporate', 'description': 'Enterprise networks'},
        {'id': 'cafe', 'name': 'Public WiFi', 'description': 'Coffee shops, airports'},
        {'id': 'iot', 'name': 'Smart Home', 'description': 'IoT devices'},
        {'id': 'gamer', 'name': 'Gaming', 'description': 'Console networks'},
        {'id': 'stealth', 'name': 'Stealth', 'description': 'Ultra-realistic mix'},
        {'id': 'random', 'name': 'Random', 'description': 'Cryptographic random'}
    ]
    return jsonify({'profiles': profiles})

@app.route('/api/stats')
def get_stats():
    """Get statistics"""
    # Simple stats (could be enhanced with database)
    return jsonify({
        'total_sessions': 0,
        'active_session': None,
        'ml_available': ML_AVAILABLE
    })

@app.route('/api/sessions')
def get_sessions():
    """Get session history"""
    return jsonify({
        'sessions': [],
        'count': 0
    })

@socketio.on('connect')
def handle_connect():
    print('✓ Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('✗ Client disconnected')

if __name__ == '__main__':
    print("\n" + "="*70)
    print("  ZSPOOF v3.0 - AI-Powered Network Security Platform")
    print("="*70)
    print(f"  Project: {PROJECT_DIR}")
    print(f"  Engine: {BIN_PATH} - {'✓ Found' if BIN_PATH.exists() else '✗ Missing'}")
    print(f"  ML Engine: {'✓ Available' if ML_AVAILABLE else '✗ Not Available'}")
    print(f"  Dashboard: {INDEX_HTML}")
    print("="*70)
    print(f"\n  🌐 Dashboard: http://localhost:5000")
    print(f"  🔌 API: http://localhost:5000/api")
    print("\n  Press Ctrl+C to stop\n")
    print("="*70 + "\n")
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)
