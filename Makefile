# ZSPOOF v3.0 - Cross-Platform Build System
# Supports: Linux, macOS, Windows, Kali

# Detect OS
ifeq ($(OS),Windows_NT)
    CXX = g++
    TARGET = bin/core_engine.exe
    RM = del /Q
    MKDIR = if not exist bin mkdir bin
    PYTHON = python
    PIP_FLAGS = 
else
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Darwin)
        CXX = clang++
    else
        CXX = g++
    endif
    TARGET = bin/core_engine
    RM = rm -f
    MKDIR = mkdir -p bin
    PYTHON = python3
    # Use --break-system-packages for Kali/Ubuntu 24+
    PIP_FLAGS = --break-system-packages
endif

# Compiler flags
CXXFLAGS = -std=c++17 -Wall -Wextra -O3 -march=native
LDFLAGS = 

# Source files
SRC = src/core_engine.cpp

.PHONY: all clean run install install-venv test help dashboard

# Default target
all: directories $(TARGET)

# Create directories
directories:
	$(MKDIR)

# Build C++ engine
$(TARGET): $(SRC)
	@echo "Building ZSPOOF Engine..."
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC) $(LDFLAGS)
	@echo "Build complete!"

# Install dependencies (with Kali/Ubuntu fix)
install:
	@echo "Installing Python dependencies..."
	@if [ -f /etc/os-release ] && grep -q "Kali\|Ubuntu" /etc/os-release; then \
		echo "Detected Kali/Ubuntu - using --break-system-packages"; \
		$(PYTHON) -m pip install $(PIP_FLAGS) -r requirements.txt || \
		sudo apt install -y python3-scapy python3-tqdm python3-flask python3-flask-cors; \
	else \
		$(PYTHON) -m pip install -r requirements.txt; \
	fi
	@echo "Dependencies installed!"

# Install in virtual environment (recommended)
install-venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv venv
	@echo "Installing dependencies in venv..."
	./venv/bin/pip install -r requirements.txt
	@echo "Virtual environment ready!"
	@echo "Activate with: source venv/bin/activate"

# Run application
run: all
	@echo "Launching ZSPOOF..."
ifeq ($(OS),Windows_NT)
	$(PYTHON) src/zspoof_ultimate.py
else
	@if [ "$$(id -u)" -ne 0 ]; then \
		echo "Root access required. Run with: sudo make run"; \
		exit 1; \
	fi
	$(PYTHON) src/zspoof_ultimate.py
endif

# Run dashboard
dashboard: all install
	@echo "Starting ZSPOOF Dashboard..."
	cd dashboard && sudo $(PYTHON) backend/app.py

# Run tests
test: all
	@echo "Running tests..."
	$(PYTHON) tests/test_engine.py

# Clean build artifacts
clean:
	@echo "Cleaning..."
ifeq ($(OS),Windows_NT)
	$(RM) bin\*.exe bin\*.o 2>nul || echo Clean complete
else
	$(RM) $(TARGET) bin/*.o
endif
	@echo "Clean complete!"

# Help
help:
	@echo "ZSPOOF v3.0 - Build System"
	@echo ""
	@echo "Commands:"
	@echo "  make              - Build the project"
	@echo "  make install      - Install dependencies (system-wide)"
	@echo "  make install-venv - Install in virtual environment"
	@echo "  make run          - Run CLI (requires sudo)"
	@echo "  make dashboard    - Run web dashboard"
	@echo "  make test         - Run test suite"
	@echo "  make clean        - Remove build files"
	@echo ""
	@echo "Platform: $(UNAME_S)"
