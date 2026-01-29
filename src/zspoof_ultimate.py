#!/usr/bin/env python3
"""
ZSPOOF v3.0 - AI-Powered Network Security Platform
Professional MAC spoofing with machine learning
"""

import sys
import os
import subprocess
import time
from pathlib import Path

# Color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class ZSpoofCLI:
    """Command-line interface for ZSPOOF"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.bin_path = self.base_dir / "bin" / "core_engine"
        
    def print_banner(self):
        banner = f"""{Colors.HEADER}
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║                  ZSPOOF v3.0 Professional                ║
║           AI-Powered Network Security Platform           ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
{Colors.ENDC}"""
        print(banner)
        
    def check_root(self):
        if os.geteuid() != 0:
            print(f"{Colors.FAIL}[!] Root access required.{Colors.ENDC}")
            print(f"    Run with: sudo python3 {sys.argv[0]}")
            sys.exit(1)
    
    def check_engine(self):
        if not self.bin_path.exists():
            print(f"{Colors.FAIL}[!] Engine not compiled.{Colors.ENDC}")
            print(f"    Run: make")
            sys.exit(1)
    
    def get_interfaces(self):
        """Get network interfaces"""
        try:
            result = subprocess.run(['ip', 'link', 'show'], capture_output=True, text=True)
            interfaces = []
            for line in result.stdout.split('\n'):
                if ': ' in line and 'state' in line.lower():
                    parts = line.split(': ')
                    if len(parts) >= 2:
                        name = parts[1].split(':')[0].split('@')[0]
                        if name != 'lo':
                            interfaces.append(name)
            return interfaces
        except:
            return []
    
    def get_current_mac(self, interface):
        """Get current MAC address"""
        try:
            result = subprocess.run(['cat', f'/sys/class/net/{interface}/address'], 
                                  capture_output=True, text=True)
            return result.stdout.strip()
        except:
            return "Unknown"
    
    def generate_mac(self, profile):
        """Generate MAC address"""
        try:
            result = subprocess.run([str(self.bin_path), profile], 
                                  capture_output=True, text=True)
            return result.stdout.strip()
        except Exception as e:
            print(f"{Colors.FAIL}[!] Generation failed: {e}{Colors.ENDC}")
            return None
    
    def set_mac(self, interface, mac):
        """Set MAC address"""
        try:
            print(f"{Colors.BLUE}[*] Bringing interface down...{Colors.ENDC}")
            subprocess.run(['ip', 'link', 'set', 'dev', interface, 'down'], check=True)
            
            print(f"{Colors.BLUE}[*] Setting new MAC: {mac}{Colors.ENDC}")
            subprocess.run(['ip', 'link', 'set', 'dev', interface, 'address', mac], check=True)
            
            print(f"{Colors.BLUE}[*] Bringing interface up...{Colors.ENDC}")
            subprocess.run(['ip', 'link', 'set', 'dev', interface, 'up'], check=True)
            
            return True
        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}[!] Failed to set MAC: {e}{Colors.ENDC}")
            return False
    
    def run(self):
        """Main CLI loop"""
        self.print_banner()
        self.check_root()
        self.check_engine()
        
        # Get interfaces
        interfaces = self.get_interfaces()
        if not interfaces:
            print(f"{Colors.FAIL}[!] No network interfaces found{Colors.ENDC}")
            sys.exit(1)
        
        print(f"\n{Colors.BOLD}Available Interfaces:{Colors.ENDC}")
        for i, iface in enumerate(interfaces, 1):
            mac = self.get_current_mac(iface)
            print(f"  {i}. {iface} ({mac})")
        
        # Select interface
        try:
            choice = int(input(f"\n{Colors.GREEN}Select interface [1-{len(interfaces)}]: {Colors.ENDC}"))
            if choice < 1 or choice > len(interfaces):
                print(f"{Colors.FAIL}Invalid choice{Colors.ENDC}")
                sys.exit(1)
            interface = interfaces[choice - 1]
        except (ValueError, KeyboardInterrupt):
            print(f"\n{Colors.FAIL}Cancelled{Colors.ENDC}")
            sys.exit(0)
        
        original_mac = self.get_current_mac(interface)
        print(f"\n{Colors.BOLD}Selected:{Colors.ENDC} {interface}")
        print(f"{Colors.BOLD}Current MAC:{Colors.ENDC} {original_mac}")
        
        # Profile menu
        print(f"\n{Colors.HEADER}═══ SPOOFING PROFILES ═══{Colors.ENDC}")
        profiles = [
            ("Corporate", "corporate", "Enterprise networks (Dell, Lenovo, HP)"),
            ("Public WiFi", "cafe", "Coffee shops, airports (Apple, Samsung)"),
            ("Smart Home", "iot", "IoT devices (ESP32, Amazon)"),
            ("Gaming", "gamer", "Console networks (PlayStation, Xbox)"),
            ("Stealth", "stealth", "Ultra-realistic mix (Recommended)"),
            ("Random", "random", "Cryptographic random"),
        ]
        
        for i, (name, _, desc) in enumerate(profiles, 1):
            print(f"  {i}. {name:15s} - {desc}")
        print(f"  0. Exit")
        
        try:
            choice = int(input(f"\n{Colors.GREEN}Select profile [0-{len(profiles)}]: {Colors.ENDC}"))
            if choice == 0:
                sys.exit(0)
            if choice < 1 or choice > len(profiles):
                print(f"{Colors.FAIL}Invalid choice{Colors.ENDC}")
                sys.exit(1)
            
            profile_name, profile_id, _ = profiles[choice - 1]
        except (ValueError, KeyboardInterrupt):
            print(f"\n{Colors.FAIL}Cancelled{Colors.ENDC}")
            sys.exit(0)
        
        # Generate MAC
        print(f"\n{Colors.BLUE}[*] Generating MAC with profile: {profile_name}{Colors.ENDC}")
        new_mac = self.generate_mac(profile_id)
        
        if not new_mac:
            sys.exit(1)
        
        print(f"{Colors.GREEN}[+] Generated: {new_mac}{Colors.ENDC}")
        
        # Confirm
        confirm = input(f"\n{Colors.WARNING}Apply this MAC? [y/N]: {Colors.ENDC}")
        if confirm.lower() != 'y':
            print(f"{Colors.FAIL}Cancelled{Colors.ENDC}")
            sys.exit(0)
        
        # Apply
        if self.set_mac(interface, new_mac):
            print(f"\n{Colors.GREEN}[✓] SUCCESS{Colors.ENDC}")
            print(f"    Interface: {interface}")
            print(f"    Original:  {original_mac}")
            print(f"    Spoofed:   {new_mac}")
            print(f"    Profile:   {profile_name}")
            print(f"\n{Colors.WARNING}[!] Reboot or run again to restore{Colors.ENDC}")
        else:
            print(f"\n{Colors.FAIL}[✗] FAILED{Colors.ENDC}")
            sys.exit(1)

if __name__ == "__main__":
    cli = ZSpoofCLI()
    cli.run()
