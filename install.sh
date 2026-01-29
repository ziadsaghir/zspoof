#!/bin/bash
#
# ZSPOOF v3.0 - Professional Installation Script
# Supports: Kali, Ubuntu, Debian, Arch, macOS
#

set -e

echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║              ZSPOOF v3.0 - INSTALLER                     ║"
echo "║         AI-Powered Network Security Platform             ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS=$ID
        echo "[*] Detected: $PRETTY_NAME"
    else
        OS="linux"
        echo "[*] Detected: Linux (generic)"
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
    echo "[*] Detected: macOS"
else
    echo "[!] Unsupported OS: $OSTYPE"
    exit 1
fi

# Check Python
echo ""
echo "[*] Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "[!] Python 3 not found"
    exit 1
fi
PYTHON_VERSION=$(python3 --version)
echo "    ✓ $PYTHON_VERSION"

# Check C++ compiler
echo ""
echo "[*] Checking C++ compiler..."
if command -v g++ &> /dev/null; then
    GCC_VERSION=$(g++ --version | head -1)
    echo "    ✓ $GCC_VERSION"
elif command -v clang++ &> /dev/null; then
    CLANG_VERSION=$(clang++ --version | head -1)
    echo "    ✓ $CLANG_VERSION"
else
    echo "[!] No C++ compiler found"
    echo "    Install: sudo apt install build-essential (Debian/Ubuntu)"
    echo "    Install: sudo pacman -S base-devel (Arch)"
    echo "    Install: xcode-select --install (macOS)"
    exit 1
fi

# Install Python dependencies
echo ""
echo "[*] Installing Python dependencies..."

if [[ "$OS" == "kali" ]] || [[ "$OS" == "ubuntu" ]] || [[ "$OS" == "debian" ]]; then
    # Kali/Ubuntu 24+ requires --break-system-packages or system packages
    echo "    Using system packages for Kali/Ubuntu..."
    
    # Try system packages first
    sudo apt-get update -qq
    sudo apt-get install -y python3-flask python3-flask-cors python3-scapy python3-tqdm 2>/dev/null || {
        echo "    System packages not available, using pip with --break-system-packages..."
        python3 -m pip install --break-system-packages -r requirements.txt
    }
else
    # Other distros
    python3 -m pip install -r requirements.txt || {
        echo "[!] pip install failed"
        echo "    Try: python3 -m pip install --user -r requirements.txt"
        exit 1
    }
fi

echo "    ✓ Dependencies installed"

# Compile C++ engine
echo ""
echo "[*] Compiling C++ engine..."
make clean
make

if [ -f "bin/core_engine" ]; then
    echo "    ✓ Engine compiled successfully"
else
    echo "[!] Engine compilation failed"
    exit 1
fi

# Test engine
echo ""
echo "[*] Testing engine..."
TEST_MAC=$(./bin/core_engine random)
if [[ "$TEST_MAC" =~ ^([0-9A-F]{2}:){5}[0-9A-F]{2}$ ]]; then
    echo "    ✓ Engine test passed"
    echo "    Generated: $TEST_MAC"
else
    echo "[!] Engine test failed"
    exit 1
fi

# Create directories
echo ""
echo "[*] Creating directories..."
mkdir -p logs profiles

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                 INSTALLATION COMPLETE                    ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "Quick Start:"
echo "  CLI Mode:       sudo make run"
echo "  Dashboard:      cd dashboard && sudo python3 backend/app.py"
echo "  Tests:          make test"
echo ""
echo "Documentation:"
echo "  README.md       - Full documentation"
echo "  QUICK_START.md  - Quick reference"
echo "  SECURITY.md     - Security guidelines"
echo ""
