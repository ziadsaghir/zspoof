# Changelog

All notable changes to ZSPOOF ULTIMATE will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.1.0.html).

## [2.1.0] - 2026-01-28

### 🚀 Added - Version 2.1

**Major Features:**
- Cross-platform support (Linux, Windows, macOS)
- ARP spoofing and MITM attack capabilities
- Network scanning and host discovery
- Session management with JSON export
- Comprehensive logging system
- Advanced anti-detection mechanisms
- 5 new sophisticated spoofing profiles

**Core Engine:**
- Rebuilt C++ engine with modern C++17
- Cryptographic randomness using hardware RNG
- 100+ vendor OUIs from 15+ manufacturers
- Market-share weighted profile generation
- Proper unicast/locally-administered bit handling
- MAC address validation system

**User Interface:**
- Complete UI redesign with intuitive menus
- Cross-platform color support
- Progress indicators with fallback
- Detailed interface information display
- Session history viewer

**Platform Support:**
- Linux: Full native support via `ip` commands
- Windows: Registry-based MAC changing (documented)
- macOS: Native `ifconfig` support
- Automatic platform detection

**Security:**
- Privilege checking on all platforms
- Secure session logging
- Input validation and sanitization
- Safe command execution

**Profiles:**
1. Corporate Environment (Dell, Lenovo, HP, Cisco)
2. Public WiFi / Cafe (Apple, Samsung, Google)
3. Smart Home / IoT (ESP32, Amazon, Tuya)
4. Gaming LAN (PlayStation, Xbox, Nintendo)
5. Stealth Mode (Ultra-realistic vendor mix)
6. Pure Random (Cryptographic)
7. Custom MAC (Manual entry with validation)

**Documentation:**
- Comprehensive README with installation guide
- Security policy (SECURITY.md)
- Contributing guidelines (CONTRIBUTING.md)
- Professional test suite
- Cross-platform build system

### 🔧 Changed

- Migrated from simple Python script to hybrid architecture
- Complete rewrite of MAC generation algorithm
- Enhanced error handling and user feedback
- Improved performance (sub-millisecond generation)
- Better cross-platform compatibility

### 🐛 Fixed

- MAC address bit pattern issues
- Platform detection edge cases
- Permission handling on different systems
- Interface enumeration reliability

### 🔒 Security

- Added security policy and disclosure process
- Implemented input validation throughout
- Added session audit logging
- Improved privilege escalation handling

---

## [1.0.0] - 2025-XX-XX

### Initial Release

**Features:**
- Basic MAC address spoofing
- Linux support only
- Simple vendor profiles (Corporate, Cafe, IoT, Gamer, Random)
- C++ generation engine
- Python orchestrator
- Command-line interface

**Components:**
- src/toolkit.py - Main application
- src/heavylifting.cpp - MAC generation
- Basic vendor database (10 vendors)
- Manual interface selection

---

## Version History

### Legend
- 🚀 Added: New features
- 🔧 Changed: Changes to existing functionality
- 🐛 Fixed: Bug fixes
- 🔒 Security: Security improvements
- ⚠️ Deprecated: Features marked for removal
- 🗑️ Removed: Removed features

---

## [Unreleased]

### Planned Features
- [ ] Machine Learning-based profile generation
- [ ] DNS spoofing capabilities
- [ ] IPv6 support and manipulation
- [ ] Graphical user interface (GUI)
- [ ] Real-time traffic analysis
- [ ] Automated evasion testing
- [ ] Cloud deployment detection
- [ ] Mobile app (Android/iOS research tools)
- [ ] Plugin architecture for extensions
- [ ] Database of known MAC addresses

### Under Consideration
- Integration with popular pentesting frameworks
- Docker container support
- Remote management API
- Collaborative red team features
- AI-powered anomaly detection evasion

---

## Release Notes

### Version 2.1.0 - "ULTIMATE"

This is a complete reimagining of ZSPOOF. What started as a simple MAC spoofing 
tool has evolved into a comprehensive network identity manipulation framework.

**Key Improvements:**
- **3x faster** MAC generation
- **Cross-platform** support out of the box
- **10x more** vendor OUIs
- **New features**: ARP spoofing, network scanning, session management
- **Better UX**: Intuitive menus, better error messages, progress indicators
- **Production ready**: Comprehensive testing, documentation, security policies

**Breaking Changes:**
- Command-line arguments changed (now uses interactive menu)
- File structure reorganized
- Configuration format updated
- Requires Python 3.8+ (was 3.6+)

**Migration Guide:**
```bash
# Old version
sudo python3 src/toolkit.py

# New version
make run  # or
sudo python3 src/zspoof_ultimate.py
```

**Contributors:**
- Ziad SAGHIR (Zeus) - Lead Developer & Security Research

**Special Thanks:**
- Security research community for feedback
- Beta testers for platform validation
- Open source projects that inspired this work

---

**Support:** ziadsghir8@gmail.com  
**Repository:** https://github.com/ziadsaghir/zspoof  
**Documentation:** README.md, SECURITY.md, CONTRIBUTING.md
