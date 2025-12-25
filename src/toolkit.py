import subprocess
import re
import sys
import argparse
import os
import time
from tqdm import tqdm


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BIN_PATH = os.path.join(BASE_DIR, "../bin/heavylifting")


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    header_path = os.path.join(BASE_DIR, "header.txt")
    if os.path.exists(header_path):
        with open(header_path, "r") as f:
            print(Colors.HEADER + f.read() + Colors.ENDC)
    else:
        print(f"{Colors.HEADER}--- ZSPOOF ---\nIdentity is a surface.{Colors.ENDC}")

def get_cpp_mac(profile="random"):
    if not os.path.exists(BIN_PATH):
        print(f"{Colors.FAIL}[!] Binary missing. Run 'make' first.{Colors.ENDC}")
        sys.exit(1)
    try:
        result = subprocess.run([BIN_PATH, profile], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"{Colors.FAIL}[!] C++ Engine Failure: {e}{Colors.ENDC}")
        sys.exit(1)

def get_current_state(iface):
    try:

        mac = subprocess.check_output(f"cat /sys/class/net/{iface}/address", shell=True).decode().strip()

        state = subprocess.check_output(f"cat /sys/class/net/{iface}/operstate", shell=True).decode().strip()
        return mac, state
    except:
        return "Unknown", "Unknown"

def set_interface_state(iface, state):
    subprocess.run(["ip", "link", "set", "dev", iface, state], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def change_mac(iface, new_mac):
    print(f"\n{Colors.BLUE}[*] Disengaging {iface}...{Colors.ENDC}")
    set_interface_state(iface, "down")
    
    print(f"{Colors.BLUE}[*] Burning new identity: {new_mac}{Colors.ENDC}")
    time.sleep(0.5) 
    
    try:
        subprocess.run(["ip", "link", "set", "dev", iface, "address", new_mac], check=True)
        success = True
    except subprocess.CalledProcessError:
        print(f"{Colors.FAIL}[!] Hardware Rejected the new MAC.{Colors.ENDC}")
        success = False

    print(f"{Colors.BLUE}[*] Re-engaging {iface}...{Colors.ENDC}")
    set_interface_state(iface, "up")
    return success

def main():
    print_banner()

    if os.geteuid() != 0:
        print(f"{Colors.FAIL}[!] Root access required.{Colors.ENDC}")
        sys.exit(1)


    try:
        route = subprocess.check_output("ip route show default", shell=True).decode()
        current_iface = route.split("dev")[1].split()[0]
    except:
        print(f"{Colors.WARNING}[!] No active network found. Pick an interface manually (eth0/wlan0):{Colors.ENDC}")
        current_iface = input("Interface name: ").strip()

    original_mac, _ = get_current_state(current_iface)
    
    print(f"{Colors.BOLD}Target Interface :{Colors.ENDC} {current_iface}")
    print(f"{Colors.BOLD}Original MAC     :{Colors.ENDC} {original_mac}\n")

    print(f"{Colors.HEADER}=== CAMOUFLAGE PROFILES ==={Colors.ENDC}")
    print("1. [Corporate]  (Blends into Offices - Dell/Lenovo/Cisco)")
    print("2. [Cafe/Public] (Blends into Public Wifi - Apple/Samsung)")
    print("3. [Smart Home] (Blends into IoT/Home - Amazon/Espressif)")
    print("4. [Gamer/LAN]  (Blends into LAN Parties - Sony/Nintendo)")
    print("5. [Ghost Mode] (Cryptographically Random)")
    print("0. [Exit]")

    try:
        choice = int(input(f"\n{Colors.GREEN}Select your cover identity > {Colors.ENDC}"))
    except ValueError:
        sys.exit(0)

    profile_map = {1: "corporate", 2: "cafe", 3: "iot", 4: "gamer", 5: "random"}
    
    if choice == 0:
        sys.exit(0)
        
    if choice in profile_map:
        new_mac = get_cpp_mac(profile_map[choice])
        

        for _ in tqdm(range(100), desc="Rewriting Firmware Headers", ncols=70, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
            time.sleep(0.005)
            
        if change_mac(current_iface, new_mac):
            print(f"\n{Colors.GREEN}[+] SPOOF SUCCESSFUL.{Colors.ENDC}")
            print(f"    Your new digital fingerprint: {Colors.BOLD}{new_mac}{Colors.ENDC}")
            print(f"    Profile loaded: {profile_map[choice].upper()}")
            

            print(f"\n{Colors.WARNING}[?] When you are done, run the tool again or reboot to reset.{Colors.ENDC}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()