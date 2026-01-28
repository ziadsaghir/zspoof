# ZSPOOF ULTIMATE — The Next Evolution in Network Identity Manipulation

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow.svg)
![C++](https://img.shields.io/badge/C%2B%2B-17-red.svg)
![Version](https://img.shields.io/badge/version-2.1.0-green.svg)

**ZSPOOF ULTIMATE** is a next-generation network identity manipulation framework designed for professional penetration testers, red team operators, and security researchers. This tool represents a quantum leap from basic MAC spoofing—it's a comprehensive platform for understanding and testing network security boundaries.

## 🚀 What Makes This Ultimate?

### Revolutionary Features

**🔹 Cross-Platform Architecture**
- Native support for Linux, Windows, and macOS
- Platform-specific optimizations for each OS
- Unified interface across all systems

**🔹 Intelligent MAC Generation**
- **Context-Aware Profiles**: Generate MACs that statistically match real-world environments
- **Market-Share Weighting**: Based on 2025 vendor distribution data
- **Anti-Detection**: Proper unicast/locally-administered bit patterns
- **2025 OUI Database**: 100+ real vendor OUIs from current devices

**🔹 ARP Spoofing & MITM**
- Network reconnaissance and host discovery
- Man-in-the-Middle attack capabilities
- ARP cache poisoning
- Traffic interception (educational purposes)

**🔹 Advanced Session Management**
- Full session logging and history
- JSON export for forensic analysis
- Automatic restoration capabilities
- Detailed audit trails

**🔹 Professional Development**
- Hybrid C++17 + Python 3 architecture
- Optimized performance with cryptographic randomness
- Comprehensive error handling
- Cross-platform compatibility layer

## 📊 Technical Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   ZSPOOF ULTIMATE                       │
│                    User Interface                       │
│                  (Python Orchestrator)                  │
└────────────────┬────────────────────────────────────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
┌───▼────┐  ┌───▼────┐  ┌───▼────┐
│ MAC    │  │  ARP   │  │Network │
│ Engine │  │Spoofer │  │Analysis│
│ (C++17)│  │(Scapy) │  │        │
└────────┘  └────────┘  └────────┘
    │            │            │
    └────────────┴────────────┘
                 │
    ┌────────────▼────────────┐
    │   Platform Adapter      │
    │ (Linux/Windows/macOS)   │
    └─────────────────────────┘
```

## ⚡ Installation

### Prerequisites

**All Platforms:**
- Python 3.8 or higher
- C++17 compatible compiler (GCC, Clang, or MSVC)

**Linux/macOS:**
```bash
# Install build tools
sudo apt-get install build-essential  # Ubuntu/Debian
# OR
xcode-select --install  # macOS
```

**Windows:**
- Install [MinGW-w64](https://www.mingw-w64.org/) or [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/)
- Add compiler to PATH

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/ziadsaghir/zspoof.git
cd zspoof

# 2. Build and install (one command!)
make install
make

# 3. Run (requires admin/root)
# Linux/macOS:
sudo make run

# Windows (as Administrator):
make run
```

## 🎯 Usage Guide

### MAC Address Spoofing

The tool offers **7 sophisticated profiles** based on real-world device distributions:

#### 1️⃣ **Corporate Environment**
Mimics enterprise devices (Dell, Lenovo, HP, Cisco). Perfect for:
- Corporate network assessments
- Enterprise WiFi testing
- Office environment blending

**Example vendors**: Dell Latitude, Lenovo ThinkPad, HP EliteBook, Cisco VoIP

#### 2️⃣ **Public WiFi / Cafe Mode**
Mimics consumer mobile devices (Apple, Samsung, Google). Ideal for:
- Public hotspot testing
- Coffee shop/airport networks
- Mobile device emulation

**Example devices**: iPhone, MacBook, Galaxy, Pixel

#### 3️⃣ **Smart Home / IoT**
Mimics IoT devices (ESP32, Amazon Echo, Tuya). Used for:
- Smart home network testing
- IoT security assessment
- Home automation research

**Example devices**: Amazon Alexa, Smart Bulbs, ESP32 sensors

#### 4️⃣ **Gaming LAN**
Mimics gaming consoles (PlayStation, Xbox, Nintendo). Perfect for:
- Gaming network analysis
- LAN party environments
- Console authentication testing

**Example devices**: PS5, Xbox Series X, Nintendo Switch

#### 5️⃣ **Stealth Mode** ⭐ *Recommended*
Ultra-realistic mix of most common vendors with market-share weighting. Best for:
- General-purpose spoofing
- Evading vendor-based filtering
- Maximum realism

#### 6️⃣ **Pure Random**
Cryptographically random MAC with proper bit flags. For:
- Maximum privacy
- Research purposes
- Unique identities

#### 7️⃣ **Custom MAC**
Manual entry with validation. Supports:
- Specific testing requirements
- Known-good MACs
- Replication scenarios

### ARP Spoofing Operations

**Network Scanning:**
```bash
# Discovers all active hosts on the network
1. Select "ARP Spoofing / MITM"
2. Choose "Scan Network"
3. Specify IP range (e.g., 192.168.1.0/24)
```

**Man-in-the-Middle Attack:**
```bash
# Educational MITM demonstration
1. Select "ARP Spoofing / MITM"
2. Choose "MITM Attack"
3. Enter target IP and gateway IP
4. Specify duration
```

**⚠️ WARNING**: ARP spoofing can disrupt network traffic. Only use in authorized environments.

### Session Management

All operations are logged with:
- Timestamp
- Interface details
- Original and spoofed MACs
- Profile used
- ARP targets (if applicable)

Export sessions to JSON for:
- Compliance reporting
- Forensic analysis
- Audit trails

## 🔬 Advanced Features

### Anti-Detection Mechanisms

1. **Proper Bit Patterns**
   - Locally administered bit (bit 1 of first octet)
   - Unicast flag (bit 0 of first octet)
   
2. **Realistic Vendor Distribution**
   - Weighted selection based on market share
   - Multiple OUIs per vendor for diversity
   
3. **Cryptographic Randomness**
   - Hardware RNG seeding
   - High-resolution timer entropy
   - MT19937-64 generator

### Network Analysis Tools

- Interface enumeration
- Gateway detection
- IP/MAC correlation
- Traffic pattern analysis (upcoming)

## 📁 Project Structure

```
zspoof/
│
├── src/
│   ├── core_engine.cpp         # C++ MAC generation engine
│   ├── zspoof_ultimate.py      # Main Python application
│   └── __init__.py
│
├── bin/                        # Compiled binaries
├── logs/                       # Session logs and exports
├── profiles/                   # Custom profile definitions
├── tests/                      # Test suite
│
├── Makefile                    # Cross-platform build system
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
└── SECURITY.md                 # Security policy
```

## 🛡️ Security & Ethics

### Legal Disclaimer

**ZSPOOF ULTIMATE is developed strictly for:**
- Educational purposes
- Authorized penetration testing
- Security research
- Red team operations with explicit permission

**Unauthorized use is illegal.** Usage of this tool for attacking targets without prior mutual consent violates:
- Computer Fraud and Abuse Act (CFAA)
- Equivalent laws in other jurisdictions
- Ethical hacking principles

### Responsible Use Guidelines

✅ **DO:**
- Use in isolated lab environments
- Obtain written authorization
- Document all testing activities
- Disclose vulnerabilities responsibly
- Respect privacy and data protection laws

❌ **DON'T:**
- Use on networks without permission
- Intercept sensitive communications
- Cause network disruptions
- Share captured data
- Violate terms of service

### Reporting Vulnerabilities

If you discover security issues in ZSPOOF ULTIMATE:
- **DO NOT** open public GitHub issues
- Email: **ziadsghir8@gmail.com**
- Include: Description, reproduction steps, potential impact

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Code style guidelines
- Adding new vendor profiles
- Testing procedures
- Pull request process

### Development Roadmap

- [ ] Machine Learning-based profile generation
- [ ] DNS spoofing capabilities
- [ ] IPv6 support
- [ ] GUI interface
- [ ] Real-time traffic analysis
- [ ] Automated evasion testing
- [ ] Cloud deployment detection

## 📊 Performance

**Benchmarks (Tested on i7-10700K):**
- MAC generation: <1ms
- Interface switching: ~2-3s
- Network scan (254 hosts): ~5s
- ARP spoof rate: 1000 pps

## 🔧 Troubleshooting

### Common Issues

**"Command not found: make"**
```bash
# Ubuntu/Debian
sudo apt-get install build-essential

# macOS
xcode-select --install

# Windows
# Install MinGW or Visual Studio Build Tools
```

**"Permission denied" errors**
```bash
# Linux/macOS - run with sudo
sudo make run

# Windows - run as Administrator
```

**"ModuleNotFoundError: scapy"**
```bash
pip install -r requirements.txt
```

**Windows MAC changing limitations**
- Windows requires registry modifications
- Some drivers don't support MAC changes
- Use Device Manager → Network Adapter → Advanced → Network Address

**"Interface not found"**
- Check interface name: `ip link` (Linux) or `ipconfig` (Windows)
- Verify interface is not disabled
- Try different interface

## 📚 Technical Details

### MAC Address Format
```
XX:XX:XX:YY:YY:YY
│  │  │  │  │  │
│  │  │  └──┴──┴── NIC-specific (Random)
└──┴──┴────────── OUI (Vendor-specific)

Bit 0 (LSB): 0 = Unicast, 1 = Multicast
Bit 1:       0 = Global, 1 = Locally Administered
```

### Vendor Database Statistics
- **100+ OUIs** from 15+ major vendors
- Based on 2025 market share data
- Updated quarterly
- Covers enterprise, consumer, and IoT devices

### Cryptographic Quality
- Uses hardware RNG when available
- Fallback to Mersenne Twister (MT19937-64)
- Time-based entropy mixing
- Proper statistical distribution

## 📜 License

MIT License - see [LICENSE](LICENSE) file for details.

## 👤 Author

**Ziad SAGHIR (Zeus)**
- Role: Cybersecurity Student - EiJV
- Focus: Offensive Security / Network Research
- Philosophy: *"Identity is a Surface - Trust is an Illusion"*

---

## 🌟 Star History

If you find this tool useful for your research or education, please consider:
- ⭐ Starring the repository
- 🔄 Sharing with security community
- 🐛 Reporting issues
- 🤝 Contributing improvements

---

**Remember:** With great power comes great responsibility. Use this tool ethically and legally.

*"The best defense is understanding the offense."*
