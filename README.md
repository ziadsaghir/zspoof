# ZSPOOF — Identity is a Surface.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)
![Language](https://img.shields.io/badge/python-3.x-yellow.svg)
![Language](https://img.shields.io/badge/C++-17-red.svg)

**ZSPOOF** is a hybrid MAC address manipulation tool designed for pentesters and red team operations. It combines a high-performance C++ randomization engine with a Python orchestrator to deliver context-aware interface spoofing.

Unlike standard tools that generate random noise, **ZSPOOF** generates **Weighted Environmental Profiles**. It allows an operator to blend into specific network environments (e.g., Corporate Offices, Coffee Shops, IoT Networks) by mathematically weighting the OUI selection to match target devices.

## ⚡ Features

- **Hybrid Architecture**: Python 3 Orchestrator + C++17 Mathematical Engine.
- **Context-Aware Camouflage**:
  - `[Corporate]` Mimics Dell, Lenovo, Cisco infrastructure.
  - `[Cafe]` Mimics Apple, Samsung mobile devices.
  - `[Gamer]` Mimics Sony, Nintendo consoles.
  - `[IoT]` Mimics Amazon Echo, Espressif chips.
- **Fail-Safe Restoration**: Automatically captures original state for clean exits.
- **Smart Validation**: Ensures generated MACs adhere to unicast/locally-administered standards.

## 📦 Installation

### Prerequisites
- Linux (Kali, Ubuntu, Debian, etc.)
- `g++` (GCC Compiler)
- Python 3 + `pip`

### Setup
```bash
# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/zspoof.git](https://github.com/YOUR_USERNAME/zspoof.git)
cd zspoof

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Compile the C++ Engine and Run
make run

🚀 Usage

Run the tool with root privileges (required for interface manipulation):
Bash

sudo python3 src/toolkit.py

Follow the interactive menu to select your camouflage profile:
Plaintext

[1] Manually enter a MAC address
[2] Vendor Masquerade (Stealth Mode)
    ├── Corporate (Office environments)
    ├── Cafe      (Public Wi-Fi)
    └── Gamer     (LAN Parties)
[3] Randomize (YOLO Mode)

⚠️ Legal Disclaimer

ZSPOOF is developed for educational and ethical testing purposes only. Usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.
🤝 Contributing

We welcome contributions! Please see CONTRIBUTING.md for details on how to add new vendor profiles or improve the engine.
👤 Author

Ziad SAGHIR (Zeus)
    Cybersecurity Student - EiJV
    Offensive Security / Network Research

"Entropy > Identity > Trust"