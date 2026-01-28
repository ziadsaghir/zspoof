# ZSPOOF ULTIMATE - Quick Reference Guide

## 🚀 Installation (1 Minute)

```bash
git clone https://github.com/YOUR_USERNAME/zspoof-ultimate.git
cd zspoof-ultimate
./install.sh  # Automated installation
```

**Or manually:**
```bash
make install  # Install dependencies
make          # Compile C++ engine
sudo make run # Run (Linux/macOS)
```

---

## 📋 Common Commands

### Running ZSPOOF
```bash
# Linux/macOS
sudo python3 src/zspoof_ultimate.py

# Windows (as Administrator)
python src/zspoof_ultimate.py

# Using Make
sudo make run
```

### Testing
```bash
make test              # Run test suite
python3 tests/test_engine.py  # Direct test execution
```

### Building
```bash
make          # Build project
make clean    # Clean build files
make debug    # Build with debug symbols
```

---

## 🎯 Feature Quick Access

### Main Menu Navigation

```
[1] MAC Address Spoofing     → Change your MAC address
[2] ARP Spoofing / MITM       → Network attacks
[3] Network Analysis          → Interface info & scanning
[4] Session History           → View past operations
[0] Exit                      → Quit program
```

### MAC Spoofing Profiles

| Profile | Use Case | Example Vendors |
|---------|----------|----------------|
| **1. Corporate** | Office networks | Dell, Lenovo, HP, Cisco |
| **2. Public WiFi** | Cafes, airports | Apple, Samsung, Google |
| **3. IoT** | Smart homes | ESP32, Amazon Echo, Tuya |
| **4. Gaming** | LAN parties | PlayStation, Xbox, Nintendo |
| **5. Stealth** | General purpose | Mixed vendors (recommended) |
| **6. Random** | Maximum privacy | Fully random |
| **7. Custom** | Specific testing | Manual MAC entry |

---

## 🔧 Common Tasks

### Task 1: Change MAC Address
```
1. Run ZSPOOF
2. Select interface
3. Main Menu → [1] MAC Address Spoofing
4. Choose profile (e.g., [5] for Stealth Mode)
5. Confirm change
```

### Task 2: Scan Network
```
1. Run ZSPOOF
2. Main Menu → [2] ARP Spoofing
3. Choose [1] Scan Network
4. Enter IP range (or press Enter for default)
```

### Task 3: View Session History
```
1. Run ZSPOOF
2. Main Menu → [4] Session History
3. Review past MAC changes
```

### Task 4: Restore Original MAC
```
Method 1: Reboot your system
Method 2: Run ZSPOOF and change to original MAC manually
Method 3: Check session history for original MAC
```

---

## 🛠️ Troubleshooting

### Problem: "Permission denied"
**Solution:**
```bash
# Linux/macOS
sudo python3 src/zspoof_ultimate.py

# Windows
# Run as Administrator
```

### Problem: "Engine binary not found"
**Solution:**
```bash
make clean
make
```

### Problem: "No module named 'scapy'"
**Solution:**
```bash
pip install -r requirements.txt
# or
pip install scapy tqdm
```

### Problem: "Interface not found"
**Solution:**
```bash
# Linux: List interfaces
ip link show

# Windows: List interfaces
ipconfig /all

# macOS: List interfaces
ifconfig
```

### Problem: MAC change doesn't work on Windows
**Solution:**
Windows requires special handling:
1. Open Device Manager
2. Network Adapters → Your Adapter
3. Properties → Advanced → Network Address
4. Enter the MAC (no colons): `001122334455`
5. Restart adapter

---

## 📊 Command Reference

### C++ Engine (Direct Usage)

```bash
# Generate MAC for profile
./bin/core_engine corporate
./bin/core_engine cafe
./bin/core_engine random

# Validate MAC address
./bin/core_engine validate 00:11:22:33:44:55

# Get hostname suggestion
./bin/core_engine hostname dell
```

### Python API (Advanced Users)

```python
from src.zspoof_ultimate import MACEngine, ARPSpoofer

# Generate MAC
engine = MACEngine()
mac = engine.generate("stealth")
print(f"Generated: {mac}")

# Validate MAC
is_valid = engine.validate("00:11:22:33:44:55")

# ARP operations (requires scapy)
spoofer = ARPSpoofer("eth0")
devices = spoofer.scan_network("192.168.1.0/24")
```

---

## 🔐 Security Checklist

Before using ZSPOOF:
- [ ] Have written authorization for testing
- [ ] Using isolated test environment
- [ ] Understand legal implications
- [ ] Have rollback plan (original MAC saved)
- [ ] Network owner has been notified
- [ ] Session logging is enabled
- [ ] Not using on production systems

---

## 📁 File Locations

```
zspoof-ultimate/
├── bin/               → Compiled binaries
├── logs/              → Session logs (*.json)
│   └── sessions.json  → All session history
├── profiles/          → Custom profiles
├── src/               → Source code
│   ├── core_engine.cpp     → C++ engine
│   └── zspoof_ultimate.py  → Main application
└── tests/             → Test suite
```

### Important Files

- `logs/sessions.json` - All MAC changes are logged here
- `logs/zspoof_export_*.json` - Exported session logs

---

## 🎓 Learning Path

### Beginner (Day 1)
1. Install ZSPOOF
2. Run test suite
3. Try MAC spoofing with Stealth profile
4. View session history
5. Restore original MAC (reboot)

### Intermediate (Week 1)
1. Understand different profiles
2. Learn about OUIs and vendor identification
3. Try network scanning
4. Read SECURITY.md
5. Experiment with custom MACs

### Advanced (Month 1)
1. Study ARP spoofing theory
2. Set up isolated lab network
3. Perform controlled MITM tests
4. Contribute to project (add vendors)
5. Write custom automation scripts

---

## 💡 Pro Tips

1. **Always test in isolated environments first**
2. **Use Stealth mode for general purpose** (best vendor mix)
3. **Corporate profile works best in enterprise networks**
4. **Keep session logs for compliance** (export regularly)
5. **Reboot to restore** (simplest method)
6. **Check interface status** before and after changes
7. **Use network scanning** to understand environment first
8. **Custom MACs** useful for replicating specific devices

---

## 📞 Getting Help

### Documentation
- `README.md` - Full documentation
- `SECURITY.md` - Security policy
- `CONTRIBUTING.md` - How to contribute
- `CHANGELOG.md` - Version history

### Commands
```bash
make help  # Build system help
```

### Support
- **GitHub Issues**: Bug reports & feature requests
- **Email**: ziadsghir8@gmail.com (security issues only)
- **Discussions**: GitHub Discussions (questions)

---

## ⚖️ Legal Reminder

**ZSPOOF ULTIMATE is for:**
✅ Educational purposes  
✅ Authorized penetration testing  
✅ Security research  
✅ Red team operations (with permission)

**NOT for:**
❌ Unauthorized network access  
❌ Identity theft  
❌ Corporate espionage  
❌ Any illegal activity

**Stay ethical. Get permission. Document everything.**

---

## 🎯 Quick Wins

**Want to see ZSPOOF in action immediately?**

```bash
# 1. Install (30 seconds)
./install.sh

# 2. Test engine (10 seconds)
make test

# 3. Generate a MAC (instant)
./bin/core_engine stealth

# 4. Full run (2 minutes)
sudo make run
# → Select interface
# → Choose [1] MAC Spoofing
# → Pick [5] Stealth Mode
# → Confirm
# → Done! Check your new MAC
```

**Total time: ~3 minutes** ⚡

---

*Last updated: January 2026*  
*Version: 2.0.0 ULTIMATE EDITION*
