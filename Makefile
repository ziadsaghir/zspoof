CXX = g++
CXXFLAGS = -std=c++17 -Wall -O2
TARGET = bin/heavylifting

all: directories $(TARGET)

$(TARGET): src/heavylifting.cpp
	$(CXX) $(CXXFLAGS) -o $(TARGET) src/heavylifting.cpp

directories:
	mkdir -p bin

run: all
	sudo python3 src/toolkit.py