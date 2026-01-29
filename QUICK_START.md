# ZSPOOF v3.0 - Quick Start Guide

## 5-Minute Setup
```bash
# 1. Clone
git clone https://github.com/ziadsaghir/zspoof.git
cd zspoof

# 2. Install
./install.sh

# 3. Run
sudo make run
```

## Common Tasks

### CLI Mode
```bash
sudo python3 src/zspoof_ultimate.py
```

### Dashboard Mode
```bash
cd dashboard
sudo python3 backend/app.py
# Open: http://localhost:5000
```

### Generate Single MAC
```bash
./bin/core_engine stealth
```

## Profiles

| Profile | Use Case |
|---------|----------|
| `corporate` | Enterprise networks |
| `cafe` | Public WiFi |
| `iot` | Smart home |
| `gamer` | Gaming networks |
| `stealth` | Maximum realism ⭐ |
| `random` | Pure random |

## Troubleshooting

### Kali/Ubuntu Installation
```bash
sudo apt install python3-flask python3-scapy python3-tqdm
```

### Permission Denied
```bash
sudo make run
```

### Engine Not Compiled
```bash
make clean
make
```

## API Quick Reference
```bash
# Health check
curl http://localhost:5000/api/health

# Generate MAC
curl -X POST http://localhost:5000/api/generate-mac \
  -H "Content-Type: application/json" \
  -d '{"profile": "stealth"}'

# Get profiles
curl http://localhost:5000/api/profiles
```

## Security Reminder

⚠️ **For authorized testing only**
- Obtain written permission
- Use in isolated environments
- Follow all applicable laws

---

For full documentation: [README.md](README.md)
