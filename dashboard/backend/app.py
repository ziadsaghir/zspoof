#!/usr/bin/env python3
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from flask_socketio import SocketIO
import subprocess
from datetime import datetime
from pathlib import Path

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Paths
SCRIPT_DIR = Path(__file__).parent
DASHBOARD_DIR = SCRIPT_DIR.parent
PROJECT_DIR = DASHBOARD_DIR.parent
BIN_PATH = PROJECT_DIR / "bin" / "core_engine"
INDEX_HTML = DASHBOARD_DIR / "index.html"

@app.route('/')
def index():
    """Serve dashboard homepage"""
    return send_file(INDEX_HTML)

@app.route('/api/health')
def health():
    """Health check"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'engine_exists': BIN_PATH.exists()
    })

@app.route('/api/generate-mac', methods=['POST'])
def generate_mac():
    """Generate MAC address"""
    data = request.json
    profile = data.get('profile', 'random')
    
    if not BIN_PATH.exists():
        return jsonify({'error': 'Engine not compiled. Run: make'}), 500
    
    try:
        result = subprocess.run([str(BIN_PATH), profile], capture_output=True, text=True, timeout=5)
        mac = result.stdout.strip()
        return jsonify({'mac': mac, 'profile': profile, 'timestamp': datetime.now().isoformat()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/profiles')
def get_profiles():
    """Get available profiles"""
    profiles = [
        {'id': 'corporate', 'name': 'Corporate', 'icon': '🏢', 'description': 'Enterprise devices'},
        {'id': 'cafe', 'name': 'Public WiFi', 'icon': '☕', 'description': 'Consumer devices'},
        {'id': 'iot', 'name': 'Smart Home', 'icon': '🏠', 'description': 'IoT devices'},
        {'id': 'gamer', 'name': 'Gaming', 'icon': '🎮', 'description': 'Gaming consoles'},
        {'id': 'stealth', 'name': 'Stealth', 'icon': '🥷', 'description': 'Ultra-realistic (Recommended)'},
        {'id': 'random', 'name': 'Random', 'icon': '🎲', 'description': 'Cryptographic random'}
    ]
    return jsonify({'profiles': profiles})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 ZSPOOF Dashboard v2.2")
    print("="*60)
    print(f"📁 Project: {PROJECT_DIR}")
    print(f"🔧 Engine: {BIN_PATH} - {'✅ Found' if BIN_PATH.exists() else '❌ Missing'}")
    print(f"📄 Index: {INDEX_HTML} - {'✅ Found' if INDEX_HTML.exists() else '❌ Missing'}")
    print("="*60)
    print("\n🌐 Dashboard: http://localhost:5000")
    print("🔌 API: http://localhost:5000/api")
    print("\nPress Ctrl+C to stop\n")
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)
