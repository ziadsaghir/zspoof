# ZSPOOF v3.0 - AI-Powered Network Security Platform

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/ziadsaghir/zspoof)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/ziadsaghir/zspoof)
[![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)](https://www.python.org)
[![C++](https://img.shields.io/badge/C++-17-red.svg)](https://isocpp.org)

**Professional MAC address manipulation framework with AI-powered intelligence for penetration testing and security research.**

## What's New in v3.0

### AI-Powered Features
- **Machine Learning Engine** - Intelligent MAC generation based on network environment
- **Network Fingerprinting** - Analyzes target networks for optimal blending
- **Confidence Scoring** - ML-based risk assessment for each operation
- **Adaptive Profiles** - Dynamic profile selection based on temporal and environmental factors

### Professional Dashboard
- **Modern UI/UX** - Clean, professional interface inspired by security tools
- **Real-time Intelligence** - Live ML recommendations and confidence metrics
- **Network Visualization** - Advanced network analysis and reporting
- **Zero Dependencies** - Single-file dashboard with no build process

### Enhanced Core
- **Cross-Platform Build System** - Supports Kali, Ubuntu, Debian, Arch, macOS
- **Intelligent Error Handling** - Better diagnostics and recovery
- **Performance Optimizations** - Faster MAC generation and network operations
- **Comprehensive Testing** - Full test suite with validation

## Quick Start
```bash
# Clone repository
git clone https://github.com/ziadsaghir/zspoof.git
cd zspoof

# Install (one command)
./install.sh

# Run CLI
sudo make run

# Run Dashboard
cd dashboard
sudo python3 backend/app.py
# Open http://localhost:5000
```

## Features

### Core Capabilities
- **Context-Aware Spoofing** - 6 intelligent profiles for different environments
- **Cryptographic Random** - High-quality randomness with proper bit patterns
- **Cross-Platform** - Native support for Linux and macOS
- **Session Management** - Full logging and audit trails
- **Network Analysis** - Built-in scanner and reconnaissance

### AI/ML Features
- **Environmental Analysis** - Analyzes network to recommend optimal profiles
- **Temporal Intelligence** - Time-based weighting for realistic behavior
- **Vendor Distribution** - Matches real-world device statistics
- **Detection Prediction** - Estimates probability of detection
- **Behavioral Mimicry** - Patterns match legitimate device behavior

### Profiles

| Profile | Use Case | Vendors | Detection Risk |
|---------|----------|---------|----------------|
| **Corporate** | Enterprise networks | Dell, Lenovo, HP, Cisco | Low |
| **Public WiFi** | Coffee shops, airports | Apple, Samsung, Google | Very Low |
| **Smart Home** | IoT environments | ESP32, Amazon, Tuya | Medium |
| **Gaming** | LAN parties, esports | PlayStation, Xbox, Nintendo | Low |
| **Stealth** | Maximum realism | Mixed with market weighting | Very Low |
| **Random** | Maximum privacy | Cryptographic random | Medium |

## Architecture
```
┌─────────────────────────────────────────────┐
│           User Interface Layer              │
│  ┌──────────────┐      ┌─────────────────┐ │
│  │  CLI Tool    │      │  Web Dashboard  │ │
│  └──────┬───────┘      └────────┬────────┘ │
└─────────┼──────────────────────┼───────────┘
          │                      │
┌─────────┼──────────────────────┼───────────┐
│         │   Python Layer       │           │
│  ┌──────▼──────┐        ┌─────▼────────┐  │
│  │ ML Engine   │        │  Flask API   │  │
│  │ (AI Logic)  │        │  (Backend)   │  │
│  └──────┬──────┘        └──────┬───────┘  │
└─────────┼──────────────────────┼───────────┘
          │                      │
┌─────────▼──────────────────────▼───────────┐
│            C++ Core Engine                  │
│  ┌────────────────────────────────────────┐│
│  │  MAC Generation with                   ││
│  │  Cryptographic Randomness              ││
│  └────────────────────────────────────────┘│
└─────────────────────────────────────────────┘
```

## Installation

### Prerequisites
- **Python** 3.8 or higher
- **C++ Compiler** (GCC 8+, Clang 10+, or MSVC 2019+)
- **Root Access** (for network interface manipulation)

### Automated Installation
```bash
./install.sh
```

The installer will:
1. Detect your OS and environment
2. Install Python dependencies
3. Compile the C++ engine
4. Run validation tests
5. Set up directories

### Manual Installation
```bash
# Install dependencies
pip3 install -r requirements.txt

# Compile engine
make

# Verify
./bin/core_engine random
```

## Usage

### Command Line Interface
```bash
# Launch CLI
sudo make run

# Select interface
# Choose profile
# Apply spoofing
```

### Web Dashboard
```bash
# Start dashboard
cd dashboard
sudo python3 backend/app.py

# Open browser
# Navigate to http://localhost:5000
```

### API Usage
```python
# Generate MAC
curl -X POST http://localhost:5000/api/generate-mac \
  -H "Content-Type: application/json" \
  -d '{"profile": "stealth"}'

# Response includes ML intelligence
{
  "mac": "00:14:22:A3:B4:C5",
  "profile": "stealth",
  "ml_confidence": 0.89,
  "ml_reasoning": "Blending with 3 vendors detected",
  "ml_risk_level": "low"
}
```

## Security & Ethics

### Legal Notice
**ZSPOOF is for AUTHORIZED TESTING ONLY.**

✅ **Permitted Uses:**
- Authorized penetration testing
- Security research in controlled environments
- Educational purposes in labs
- Red team operations with permission

❌ **Prohibited Uses:**
- Unauthorized network access
- Identity theft or fraud
- Malicious activities
- Any illegal operations

**You are solely responsible for compliance with all applicable laws.**

### Responsible Use
1. **Always** obtain written authorization
2. **Never** target production systems without permission
3. **Respect** privacy and data protection laws
4. **Document** all testing activities
5. **Report** vulnerabilities responsibly

## Development

### Project Structure
```
zspoof/
├── src/
│   ├── core_engine.cpp       # C++ MAC generator
│   ├── ml_engine.py           # ML intelligence
│   ├── zspoof_ultimate.py     # CLI application
│   └── __init__.py
├── dashboard/
│   ├── backend/
│   │   └── app.py             # Flask API
│   └── index.html             # Web interface
├── tests/
│   └── test_engine.py         # Test suite
├── Makefile                   # Build system
├── install.sh                 # Installer
└── requirements.txt           # Dependencies
```

### Building
```bash
# Clean build
make clean

# Compile
make

# Run tests
make test
```

### Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Technical Details

### MAC Address Format
```
XX:XX:XX:YY:YY:YY
│  │  │  │  │  │
│  │  │  └──┴──┴── NIC (Random)
└──┴──┴────────── OUI (Vendor)

Bit 0: Unicast (0) / Multicast (1)
Bit 1: Global (0) / Local (1)
```

### Vendor Database
- **100+ OUIs** from 15+ manufacturers
- Based on 2025 market share data
- Quarterly updates
- Covers enterprise, consumer, IoT

### Performance
- MAC Generation: <1ms
- Interface Detection: ~100ms
- Network Scan: ~5s (254 hosts)
- Dashboard Load: <500ms

## Troubleshooting

### Installation Issues

**"externally-managed-environment" on Kali/Ubuntu:**
```bash
# Option 1: Use system packages (recommended)
sudo apt install python3-flask python3-scapy python3-tqdm

# Option 2: Use --break-system-packages
pip3 install --break-system-packages -r requirements.txt

# Option 3: Virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**"Permission denied":**
```bash
# Run with sudo
sudo make run
```

**"Engine not compiled":**
```bash
# Install build tools
sudo apt install build-essential  # Debian/Ubuntu
sudo pacman -S base-devel         # Arch
xcode-select --install            # macOS

# Compile
make
```

### Runtime Issues

**"Interface not found":**
```bash
# List interfaces
ip link show

# Use correct name (e.g., eth0, wlan0, enp0s3)
```

**"MAC change failed":**
- Check if interface supports MAC changing
- Verify you're running as root
- Some drivers don't support MAC modification

## Roadmap

### Upcoming Features
- [ ] Deep Learning-based anomaly detection
- [ ] Automated evasion recommendations
- [ ] Traffic pattern analysis
- [ ] IPv6 support
- [ ] DNS spoofing integration
- [ ] Multi-interface coordination
- [ ] Cloud deployment detection

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

**Ziad SAGHIR (Zeus)**
- Cybersecurity Student - EiJV
- Focus: Offensive Security / Network Research
- Email: ziadsaghir8@gmail.com

## Acknowledgments

- Security research community
- Open source contributors
- Ethical hacking community

---

**Remember: With great power comes great responsibility.**

*"The best defense is understanding the offense."*
