# Contributing to ZSPOOF ULTIMATE

First off, thank you for considering contributing to ZSPOOF ULTIMATE! This project aims to be the most comprehensive and educational network security research tool available.

## Code of Conduct

### Our Standards

- **Ethical:** All contributions must support ethical security research
- **Legal:** No features that enable illegal activities
- **Quality:** Maintain high code quality and documentation
- **Respectful:** Be kind and constructive in all interactions

## How Can I Contribute?

### 🐛 Reporting Bugs

**Before submitting:**
1. Check existing issues to avoid duplicates
2. Verify the bug exists in the latest version
3. Test in a clean environment

**Bug Report Template:**
```markdown
**Environment:**
- OS: [e.g., Ubuntu 22.04, Windows 11, macOS 13]
- Python Version: [e.g., 3.10.5]
- ZSPOOF Version: [e.g., 2.0.0]

**Description:**
Clear description of the bug

**Steps to Reproduce:**
1. Step one
2. Step two
3. ...

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Logs/Screenshots:**
Relevant output or screenshots

**Additional Context:**
Any other relevant information
```

### 💡 Suggesting Features

We welcome feature suggestions! Please:

1. **Check roadmap** in README.md
2. **Search existing** feature requests
3. **Provide use case** - explain why it's needed
4. **Consider scope** - does it fit the project goals?

**Feature Request Template:**
```markdown
**Feature Description:**
Brief overview of the feature

**Use Case:**
How would this be used in security research?

**Proposed Implementation:**
Technical approach (if you have ideas)

**Alternatives Considered:**
Other approaches you've thought about

**Additional Context:**
Mockups, references, etc.
```

### 🔧 Code Contributions

#### Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/ziadsaghir/zspoof.git
   cd zspoof
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b bugfix/issue-number
   ```

3. **Set up development environment**
   ```bash
   make install
   make
   ```

#### Development Guidelines

**Python Code Style:**
- Follow PEP 8
- Use type hints where appropriate
- Document all functions with docstrings
- Maximum line length: 100 characters

```python
def example_function(param1: str, param2: int) -> bool:
    """
    Brief description of function.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When param2 is negative
    """
    pass
```

**C++ Code Style:**
- Modern C++17 practices
- Use RAII for resource management
- Avoid raw pointers (use smart pointers)
- Comprehensive comments for complex logic

```cpp
/**
 * @brief Brief description
 * @param param1 Description of param1
 * @return Description of return value
 */
std::string example_function(const std::string& param1) {
    // Implementation
}
```

**Commit Messages:**
```
type(scope): Brief description

Longer explanation if needed

Fixes #123
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(arp): Add ARP cache poisoning feature`
- `fix(mac): Correct unicast bit validation`
- `docs(readme): Update installation instructions`

#### Testing Your Changes

**Required Tests:**
```bash
# Compile without errors
make clean
make

# Run test suite (when available)
make test

# Manual testing checklist:
# - Test on target platform(s)
# - Verify no regressions
# - Test edge cases
# - Check memory leaks (C++ changes)
```

**Platform Testing:**
- Linux: Required for all changes
- Windows: Required for cross-platform features
- macOS: Optional but appreciated

#### Pull Request Process

1. **Update documentation**
   - README.md if adding features
   - Code comments
   - SECURITY.md if security-relevant

2. **Ensure all checks pass**
   - Code compiles without warnings
   - Tests pass (if applicable)
   - No obvious security issues

3. **Submit PR with:**
   - Clear title: `[Feature/Fix] Brief description`
   - Description of changes
   - Screenshots/demos if UI changes
   - Testing performed
   - Related issues (if any)

4. **Review process:**
   - Maintainer reviews within 1 week
   - Address feedback promptly
   - Squash commits if requested
   - Merge when approved

### 📚 Documentation

Documentation improvements are always welcome:

- **README.md**: Installation, usage, examples
- **SECURITY.md**: Security practices, policies
- **Code comments**: Explain complex logic
- **Docstrings**: All public functions
- **Examples**: Real-world use cases

### 🔬 Research Contributions

Share your findings:

- **Attack techniques**: New evasion methods
- **Detection methods**: How to detect spoofing
- **Use cases**: Novel applications
- **Benchmarks**: Performance data

## Specific Contribution Areas

### Adding New Vendor Profiles

To add support for a new device vendor:

1. **Research the vendor:**
   - Find official OUI registrations
   - Identify 5-10 common OUIs
   - Note typical hostname patterns
   - Estimate market share (if possible)

2. **Update C++ engine** (`src/core_engine.cpp`):
   ```cpp
   {"vendor_name", {{
       "OUI:1", "OUI:2", "OUI:3", ...  // At least 5 OUIs
   }, {"Hostname-", "Device-"}, market_share}},
   ```

3. **Update profiles** (if adding category):
   - Add to profile_map in Python
   - Update menu text
   - Document in README

4. **Test thoroughly:**
   ```bash
   # Generate 100 MACs and verify OUIs
   for i in {1..100}; do ./bin/core_engine vendor_name; done
   ```

### Cross-Platform Improvements

Help make ZSPOOF work better on all platforms:

**Windows:**
- Registry-based MAC changing
- Native interface enumeration
- Better error messages

**macOS:**
- SIP compatibility
- M1/M2 support
- Proper privilege handling

**BSD:**
- Initial support
- Interface detection
- Documentation

### Performance Optimization

- Profile C++ code with `gprof`/`perf`
- Optimize Python hot paths
- Reduce memory allocations
- Improve startup time

## Development Workflow

### Branch Strategy

- `main`: Stable releases only
- `develop`: Integration branch
- `feature/*`: New features
- `bugfix/*`: Bug fixes
- `hotfix/*`: Critical fixes for production

### Release Process

1. Update version numbers
2. Update CHANGELOG.md
3. Tag release: `git tag v2.0.0`
4. Create GitHub release
5. Update documentation

## Getting Help

**Questions about contributing?**

- Open a discussion on GitHub
- Email: ziadsghir8@gmail.com
- Check existing issues/PRs

**Before asking:**
- Read this document thoroughly
- Search closed issues
- Check documentation

## Recognition

Contributors will be:
- Listed in README.md
- Credited in release notes
- Acknowledged in documentation

Significant contributions may result in:
- Co-authorship on academic papers
- Conference presentation opportunities
- Direct maintainer access

## Legal Considerations

By contributing, you:

1. **Certify** you have the right to contribute the code
2. **License** your contribution under MIT License
3. **Agree** to ethical use guidelines
4. **Understand** contributions will be public

### Developer Certificate of Origin

```
By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the MIT license; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications; or

(c) The contribution was provided directly to me by some other
    person who certified (a) or (b) and I have not modified it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution is maintained
    indefinitely.
```

## Style Guides

### Python

Use `black` for formatting:
```bash
pip install black
black src/
```

Use `pylint` for linting:
```bash
pip install pylint
pylint src/zspoof_ultimate.py
```

### C++

Use `clang-format`:
```bash
clang-format -i src/core_engine.cpp
```

### Documentation

- Use Markdown for all docs
- 80 character line limit
- Clear, concise language
- Examples for complex topics

## First-Time Contributors

Welcome! Here are some good first issues:

- Documentation improvements
- Adding vendor OUIs
- Platform testing
- Error message clarity
- Code comments

**Look for issues tagged:** `good first issue`, `help wanted`, `documentation`

## Advanced Contributors

If you're experienced, consider:

- Architecture improvements
- Performance optimizations
- Security hardening
- ML/AI integration
- GUI development

## Questions?

Don't hesitate to ask! We're here to help you contribute successfully.

**Contact:**
- GitHub Discussions
- Email: ziadsghir8@gmail.com

---

Thank you for contributing to ZSPOOF ULTIMATE! Together, we're advancing security research and education.

*"The best contributions come from those who understand both the power and responsibility of security tools."*
