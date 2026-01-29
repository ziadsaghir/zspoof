# ZSPOOF v3.0 - Deployment Guide

## Quick Deployment
```bash
git clone https://github.com/ziadsaghir/zspoof.git
cd zspoof
./install.sh
```

## Platform-Specific Notes

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install build-essential python3-dev
./install.sh
```

### Kali Linux
```bash
# System packages preferred
sudo apt install python3-flask python3-scapy python3-tqdm
make
```

### Arch Linux
```bash
sudo pacman -S base-devel python python-pip
./install.sh
```

### macOS
```bash
xcode-select --install
./install.sh
```

## Docker (Optional)
```dockerfile
FROM python:3.12-slim
RUN apt-get update && apt-get install -y build-essential
WORKDIR /app
COPY . .
RUN ./install.sh
CMD ["python3", "src/zspoof_ultimate.py"]
```

## Production Checklist

- [ ] All tests pass
- [ ] Documentation reviewed
- [ ] Security guidelines understood
- [ ] Proper permissions configured
- [ ] Logging enabled
- [ ] Backup strategy in place

## Troubleshooting

See [README.md](README.md) troubleshooting section.

## Support

- Issues: GitHub Issues
- Security: ziadsaghir8@gmail.com
