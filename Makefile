# ZSPOOF ULTIMATE - Cross-Platform Build System
# Supports: Linux, macOS, Windows (MinGW/Cygwin)

# Compiler detection
ifeq ($(OS),Windows_NT)
    CXX = g++
    TARGET = bin/core_engine.exe
    RM = del /Q
    MKDIR = if not exist bin mkdir bin
    PYTHON = python
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
endif

# Compiler flags
CXXFLAGS = -std=c++17 -Wall -Wextra -O3 -march=native
LDFLAGS = 

# Source files
SRC = src/core_engine.cpp

# Phony targets
.PHONY: all clean run install test help

# Default target
all: directories $(TARGET)

# Create directories
directories:
	$(MKDIR)

# Build the C++ engine
$(TARGET): $(SRC)
	@echo "Building ZSPOOF Ultimate Engine..."
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC) $(LDFLAGS)
	@echo "Build complete: $(TARGET)"

# Install Python dependencies
install:
	@echo "Installing Python dependencies..."
	$(PYTHON) -m pip install -r requirements.txt
	@echo "Dependencies installed!"

# Run the application
run: all install
	@echo "Launching ZSPOOF Ultimate..."
ifeq ($(OS),Windows_NT)
	$(PYTHON) src/zspoof_ultimate.py
else
	sudo $(PYTHON) src/zspoof_ultimate.py
endif

# Run tests
test: all
	@echo "Running tests..."
	$(PYTHON) tests/test_engine.py

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
ifeq ($(OS),Windows_NT)
	$(RM) bin\core_engine.exe 2>nul || echo Clean complete
	$(RM) bin\*.o 2>nul || echo Clean complete
else
	$(RM) $(TARGET)
	$(RM) bin/*.o
endif
	@echo "Clean complete!"

# Development mode (debug build)
debug: CXXFLAGS = -std=c++17 -Wall -Wextra -g -DDEBUG
debug: all

# Help
help:
	@echo "ZSPOOF Ultimate - Build System"
	@echo ""
	@echo "Available targets:"
	@echo "  make          - Build the project"
	@echo "  make install  - Install Python dependencies"
	@echo "  make run      - Build and run the application (requires sudo on Unix)"
	@echo "  make test     - Run tests"
	@echo "  make clean    - Remove build artifacts"
	@echo "  make debug    - Build with debug symbols"
	@echo "  make help     - Show this help message"
	@echo ""
	@echo "Platform: $(UNAME_S)"
	@echo "Compiler: $(CXX)"
