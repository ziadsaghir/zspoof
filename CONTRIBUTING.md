# Contributing to ZSPOOF

First off, thanks for taking the time to contribute!

The goal of ZSPOOF is to provide a stealthy, context-aware spoofing tool. We value clean code, clear documentation, and ethical usage.

## How to Contribute

1. **Fork the repo** and create your branch from `main`.
2. **Test your changes**! Ensure `make run` still compiles and runs without errors.
3. **Format your code**. Python should generally follow PEP8.
4. **Issue a Pull Request** describing what you changed.

## Development Guide

### Adding New Vendors
If you want to add a new vendor (e.g., generic HP laptops) to the masquerade list, you need to update the C++ engine:

1. Open `src/heavylifting.cpp`.
2. Find the `db` map.
3. Add the vendor name and at least 3 valid OUIs.
   ```cpp
   {"hp", {{"00:11:22", "33:44:55", "66:77:88"}}},

    Recompile with make to test.

Reporting Bugs

If you find a bug, please create a GitHub Issue including:

    Your OS version (e.g., Kali Linux 2024.1).

    The error message.

    Steps to reproduce the bug.