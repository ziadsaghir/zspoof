# Contributing to ZSPOOF

Thank you for considering contributing to ZSPOOF! This document provides guidelines for contributing.

## Code of Conduct

- Be respectful and professional
- Focus on constructive feedback
- Help create a welcoming environment
- Follow ethical hacking principles

## How to Contribute

### Reporting Bugs

**Before submitting:**
1. Check existing issues
2. Verify it's reproducible
3. Test on latest version

**Bug Report Template:**
```markdown
**Environment:**
- OS: [e.g., Ubuntu 24.04]
- Python: [e.g., 3.12]
- ZSPOOF: [e.g., 3.0.0]

**Description:**
Clear description of the bug

**Steps to Reproduce:**
1. Step one
2. Step two
3. Step three

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Logs/Screenshots:**
Any relevant output
```

### Suggesting Features

**Feature Request Template:**
```markdown
**Problem:**
What problem does this solve?

**Proposed Solution:**
How would it work?

**Alternatives:**
Other approaches considered

**Use Case:**
Real-world scenarios
```

### Pull Requests

**Process:**
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Make changes
4. Test thoroughly
5. Commit with clear messages
6. Push to branch
7. Open Pull Request

**PR Requirements:**
- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New tests added (if applicable)
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts

## Development Guidelines

### Code Style

**Python:**
- Follow PEP 8
- Use type hints
- Maximum line length: 100 characters
- Use meaningful variable names
```python
# Good
def generate_mac_address(profile: str) -> str:
    """Generate MAC address for given profile."""
    pass

# Bad
def gen(p):
    pass
```

**C++:**
- Follow C++17 standards
- Use descriptive names
- Add comments for complex logic
```cpp
// Good
std::string generate_random_mac() {
    // Generate cryptographically secure MAC
    return mac;
}

// Bad
std::string gen() { return m; }
```

### Commit Messages

Format: `type: brief description`

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Tests
- `chore`: Maintenance

**Examples:**
```bash
feat: add ML-based vendor selection
fix: resolve Kali installation issue
docs: update API documentation
```

### Testing

**Before submitting:**
```bash
# Run tests
make test

# Test CLI
sudo make run

# Test dashboard
cd dashboard && sudo python3 backend/app.py

# Test installation
./install.sh
```

### Documentation

Update documentation for:
- New features
- API changes
- Configuration options
- Breaking changes

## Adding Vendor Profiles

To add new vendors to the database:

**1. Update C++ Engine (`src/core_engine.cpp`):**
```cpp
{"vendor_name", {{
    "OUI1:prefix", "OUI2:prefix", "OUI3:prefix"
}, {"Hostname-Pattern-"}, market_share}},
```

**2. Get Real OUIs:**
- Search IEEE OUI database
- Verify manufacturer
- Use at least 3 OUIs

**3. Update Documentation:**
- Add to README vendor list
- Update profile descriptions

## Project Structure
```
zspoof/
├── src/
│   ├── core_engine.cpp       # C++ MAC generator
│   ├── ml_engine.py           # ML intelligence
│   ├── zspoof_ultimate.py     # CLI application
│   └── __init__.py
├── dashboard/
│   ├── backend/
│   │   └── app.py             # Flask API
│   └── index.html             # Web UI
├── tests/
│   └── test_engine.py
├── docs/
└── Makefile
```

## Release Process

**Maintainers only:**

1. Update version in:
   - `src/__init__.py`
   - `setup.py`
   - `README.md`

2. Update CHANGELOG.md

3. Create release commit:
```bash
   git commit -m "chore: release v3.x.x"
```

4. Tag release:
```bash
   git tag -a v3.x.x -m "Release v3.x.x"
```

5. Push:
```bash
   git push origin main
   git push origin v3.x.x
```

## Questions?

- **General:** Open GitHub Issue
- **Security:** Email ziadsaghir8@gmail.com
- **Chat:** GitHub Discussions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to ZSPOOF! 🎉
