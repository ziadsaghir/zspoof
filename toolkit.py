import csv, subprocess, platform, re, random, sys, argparse, os, time
from tqdm import tqdm

def processing_bar():
    for _ in tqdm(range(100), desc="Processing your demand", ncols=70):
        time.sleep(0.01)

def print_banner():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    header_path = os.path.join(base_dir, "header.txt")
    with open(header_path, "r") as f:
        print(f.read())

print_banner()

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action="store_true")
args = parser.parse_args()

print("Verbose mode is ON" if args.verbose else "Verbose mode is OFF")

result = subprocess.run(
    "ip link show",
    capture_output=True,
    shell=True,
    text=True
)

ipconfig = result.stdout.splitlines()

mac_pattern = r'([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}'
physical_ifaces_keywords = ("eth", "en", "wlan", "wl")
exclude_keywords = ("docker", "veth", "br-", "lo")

my_mac = None
current_iface = None

for line in ipconfig:
    if ":" in line and "<" in line:
        current_iface = line.split(":")[1].strip()

    if current_iface and (
        any(k in current_iface for k in exclude_keywords) or
        not current_iface.startswith(physical_ifaces_keywords)
    ):
        continue

    match = re.search(mac_pattern, line)
    if match and current_iface:
        my_mac = match.group()
        break

option = int(input(
    "========== Please choose your mode ==========\n\n"
    "\t[1] Manually changing my MAC address\n"
    "\t[2] Other options for pentesters :) to come\n"
    "\t[0] Exit program\nYour option:\t"
))

match option:
    case 1:
        new_mac = input("Please enter your new MAC Address (first try):\t")

        if not re.fullmatch(mac_pattern, new_mac):
            while True:
                new_mac = input(
                    "Weird MAC, try again (maybe go study MAC format before using this tool :) ):\t"
                )
                if re.fullmatch(mac_pattern, new_mac):
                    break
                print("\nBro, your MAC isn't MACcing (incorrect MAC address), verify your input please!")

        subprocess.run(["ifconfig", current_iface, "down"], shell=True)
        subprocess.run(["ifconfig", current_iface, "hw", "ether", new_mac], shell=True)
        subprocess.run(["ifconfig", current_iface, "up"], shell=True)

        processing_bar()
        print("Quick reminder:")
        print("-> Your original MAC address:", my_mac)
        print("-> Your new MAC address:", new_mac)
        print("Here is a quick break down of the new configuration:\n")
        subprocess.run("ifconfig", shell=True)

    case 2:
        print("Coming later!")
        sys.exit(0)

    case 0:
        sys.exit(0)

    case _:
        print("Invalid option!!! you fool!")
        sys.exit(1)

if args.verbose:
    print(result.stderr)

if result.returncode == 0:
    print("Successfully ZSpoofffeedd!! - Ziad SAGHIR")
else:
    print("Something went wrong, go study the README file on github to understand the usage of the tool, you fool!")
