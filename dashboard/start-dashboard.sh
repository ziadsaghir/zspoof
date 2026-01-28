#!/bin/bash
#
# ZSPOOF Dashboard Launcher
# Quick start script for the web dashboard
#

set -e

echo "🎨 ZSPOOF Dashboard Launcher v2.2"
echo "=================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "⚠️  Warning: Dashboard should be run as root for full functionality"
    echo "   Run with: sudo $0"
    echo ""
fi

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

echo "📁 Project directory: $PROJECT_DIR"
echo ""

# Check if dependencies are installed
echo "🔍 Checking dependencies..."

if ! python3 -c "import flask" 2>/dev/null; then
    echo "❌ Flask not installed"
    echo "   Installing dashboard dependencies..."
    pip install --break-system-packages -r dashboard/backend/requirements.txt
fi

if ! python3 -c "import scapy" 2>/dev/null; then
    echo "⚠️  Scapy not installed - ARP features will be limited"
    echo "   Install with: sudo apt install python3-scapy"
fi

echo "✅ Dependencies OK"
echo ""

# Check if C++ engine is compiled
if [ ! -f "bin/core_engine" ]; then
    echo "⚙️  Compiling C++ engine..."
    make
    echo "✅ Engine compiled"
    echo ""
fi

# Start backend
echo "🚀 Starting ZSPOOF Dashboard..."
echo ""
echo "📊 Dashboard URL: http://localhost:5000"
echo "🔌 API Endpoint: http://localhost:5000/api"
echo ""
echo "Press Ctrl+C to stop"
echo "=================================="
echo ""

cd "$SCRIPT_DIR"
python3 backend/app.py
