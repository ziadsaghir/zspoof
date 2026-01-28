#!/bin/bash
#
# ZSPOOF ULTIMATE - Quick Installation Script
# Automates the complete installation process
#

set -e  # Exit on error

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Banner
echo -e "${CYAN}${BOLD}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║              ZSPOOF ULTIMATE - INSTALLER                 ║"
echo "║                                                           ║"
echo "║              Version 2.0.0 - ULTIMATE EDITION            ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Detect OS
echo -e "${BLUE}[*] Detecting operating system...${NC}"
OS="unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
    echo -e "${GREEN}✓ Linux detected${NC}"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
    echo -e "${GREEN}✓ macOS detected${NC}"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    OS="windows"
    echo -e "${GREEN}✓ Windows (MinGW/Cygwin) detected${NC}"
else
    echo -e "${YELLOW}⚠ Unknown OS: $OSTYPE${NC}"
fi

# Check for required tools
echo -e "\n${BLUE}[*] Checking prerequisites...${NC}"

check_command() {
    if command -v $1 &> /dev/null; then
        echo -e "${GREEN}✓ $1 found${NC}"
        return 0
    else
        echo -e "${RED}✗ $1 not found${NC}"
        return 1
    fi
}

# Check Python
if ! check_command python3; then
    echo -e "${RED}[!] Python 3 is required but not installed.${NC}"
    echo -e "${YELLOW}[i] Please install Python 3.8 or higher${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${CYAN}    Version: $PYTHON_VERSION${NC}"

# Check C++ compiler
echo -e "\n${BLUE}[*] Checking C++ compiler...${NC}"
CXX_FOUND=false

if command -v g++ &> /dev/null; then
    echo -e "${GREEN}✓ g++ found${NC}"
    GXX_VERSION=$(g++ --version | head -n1)
    echo -e "${CYAN}    $GXX_VERSION${NC}"
    CXX_FOUND=true
elif command -v clang++ &> /dev/null; then
    echo -e "${GREEN}✓ clang++ found${NC}"
    CLANG_VERSION=$(clang++ --version | head -n1)
    echo -e "${CYAN}    $CLANG_VERSION${NC}"
    CXX_FOUND=true
fi

if [ "$CXX_FOUND" = false ]; then
    echo -e "${RED}[!] No C++ compiler found${NC}"
    
    if [ "$OS" = "linux" ]; then
        echo -e "${YELLOW}[i] Install with: sudo apt-get install build-essential${NC}"
    elif [ "$OS" = "macos" ]; then
        echo -e "${YELLOW}[i] Install with: xcode-select --install${NC}"
    elif [ "$OS" = "windows" ]; then
        echo -e "${YELLOW}[i] Install MinGW-w64 or Visual Studio Build Tools${NC}"
    fi
    
    read -p "$(echo -e ${YELLOW}Continue anyway? [y/N]: ${NC})" -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check make
if ! check_command make; then
    echo -e "${YELLOW}[!] make not found - installation may fail${NC}"
fi

# Install Python dependencies
echo -e "\n${BLUE}[*] Installing Python dependencies...${NC}"
if python3 -m pip install -r requirements.txt; then
    echo -e "${GREEN}✓ Dependencies installed${NC}"
else
    echo -e "${RED}✗ Failed to install dependencies${NC}"
    echo -e "${YELLOW}[i] Try: python3 -m pip install --user -r requirements.txt${NC}"
    exit 1
fi

# Compile C++ engine
echo -e "\n${BLUE}[*] Compiling C++ engine...${NC}"
if make; then
    echo -e "${GREEN}✓ Engine compiled successfully${NC}"
else
    echo -e "${RED}✗ Compilation failed${NC}"
    echo -e "${YELLOW}[i] Check compiler errors above${NC}"
    exit 1
fi

# Check if binary exists
BINARY="bin/core_engine"
if [ "$OS" = "windows" ]; then
    BINARY="bin/core_engine.exe"
fi

if [ -f "$BINARY" ]; then
    echo -e "${GREEN}✓ Binary created: $BINARY${NC}"
else
    echo -e "${RED}✗ Binary not found: $BINARY${NC}"
    exit 1
fi

# Test the engine
echo -e "\n${BLUE}[*] Testing engine...${NC}"
TEST_MAC=$($BINARY random 2>&1)
if [[ $TEST_MAC =~ ^[0-9A-F]{2}(:[0-9A-F]{2}){5}$ ]]; then
    echo -e "${GREEN}✓ Engine test passed${NC}"
    echo -e "${CYAN}    Generated MAC: $TEST_MAC${NC}"
else
    echo -e "${YELLOW}⚠ Engine test warning${NC}"
    echo -e "${CYAN}    Output: $TEST_MAC${NC}"
fi

# Create necessary directories
echo -e "\n${BLUE}[*] Creating directories...${NC}"
mkdir -p logs profiles tests
echo -e "${GREEN}✓ Directories created${NC}"

# Check permissions
echo -e "\n${BLUE}[*] Checking permissions...${NC}"
if [ "$OS" = "linux" ] || [ "$OS" = "macos" ]; then
    if [ "$(id -u)" -ne 0 ]; then
        echo -e "${YELLOW}⚠ Not running as root${NC}"
        echo -e "${CYAN}[i] You'll need sudo to run ZSPOOF${NC}"
    else
        echo -e "${GREEN}✓ Running as root${NC}"
    fi
fi

# Installation complete
echo -e "\n${GREEN}${BOLD}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║           ✓ INSTALLATION SUCCESSFUL!                     ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Usage instructions
echo -e "${CYAN}${BOLD}QUICK START:${NC}"
echo -e "${CYAN}════════════${NC}\n"

if [ "$OS" = "linux" ] || [ "$OS" = "macos" ]; then
    echo -e "${YELLOW}Run ZSPOOF:${NC}"
    echo -e "  ${GREEN}sudo make run${NC}"
    echo -e "  ${CYAN}or${NC}"
    echo -e "  ${GREEN}sudo python3 src/zspoof_ultimate.py${NC}\n"
elif [ "$OS" = "windows" ]; then
    echo -e "${YELLOW}Run ZSPOOF (as Administrator):${NC}"
    echo -e "  ${GREEN}make run${NC}"
    echo -e "  ${CYAN}or${NC}"
    echo -e "  ${GREEN}python src/zspoof_ultimate.py${NC}\n"
fi

echo -e "${YELLOW}Run Tests:${NC}"
echo -e "  ${GREEN}make test${NC}\n"

echo -e "${YELLOW}Get Help:${NC}"
echo -e "  ${GREEN}make help${NC}\n"

echo -e "${CYAN}${BOLD}DOCUMENTATION:${NC}"
echo -e "${CYAN}══════════════${NC}"
echo -e "  • README.md       - Full usage guide"
echo -e "  • SECURITY.md     - Security policy"
echo -e "  • CONTRIBUTING.md - How to contribute"
echo -e "  • CHANGELOG.md    - Version history\n"

echo -e "${YELLOW}${BOLD}IMPORTANT:${NC}"
echo -e "${RED}This tool is for educational and authorized testing only!${NC}"
echo -e "${RED}Unauthorized use may violate laws. Stay ethical.${NC}\n"

echo -e "${CYAN}Happy hacking! 🎯${NC}"
