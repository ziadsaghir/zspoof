# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 3.0.x   | ✅ Yes            |
| 2.x     | ⚠️ Limited        |
| < 2.0   | ❌ No             |

## Reporting a Vulnerability

**IMPORTANT: Do NOT open public issues for security vulnerabilities.**

### How to Report

Email security issues to: **ziadsaghir8@gmail.com**

Include:
- Description of vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### Response Timeline

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 7 days
- **Fix & Disclosure**: Coordinated with reporter

### Responsible Disclosure

We follow coordinated vulnerability disclosure:
1. Report received
2. Vulnerability confirmed
3. Fix developed
4. Patch released
5. Public disclosure (coordinated)

## Security Best Practices

### For Users

**Do:**
- ✅ Use only in authorized environments
- ✅ Keep software updated
- ✅ Review code before running
- ✅ Use virtual environments
- ✅ Monitor system logs

**Don't:**
- ❌ Use on production networks without permission
- ❌ Run as root unnecessarily
- ❌ Disable security features
- ❌ Share credentials or access
- ❌ Use outdated versions

### For Developers

**Code Security:**
- Input validation on all user data
- Proper error handling
- Secure random generation
- No hardcoded credentials
- Regular dependency updates

**Testing:**
- Run security scans
- Test edge cases
- Validate input sanitization
- Check for privilege escalation
- Review third-party libraries

## Known Limitations

### Platform-Specific

**Linux:**
- Requires root for MAC changes
- Some drivers don't support MAC modification
- Network manager interference possible

**Windows:**
- Registry modification required
- Limited driver support
- Administrator access needed

**macOS:**
- System Integrity Protection considerations
- Some interfaces protected
- Requires admin access

### General

- ML engine requires training data
- Network scan limited by permissions
- ARP spoofing detectable by IDS
- Some enterprise networks have MAC filtering

## Ethical Guidelines

ZSPOOF is designed for:
- ✅ Authorized penetration testing
- ✅ Security research (controlled)
- ✅ Educational purposes
- ✅ Red team operations (authorized)

**Never use for:**
- ❌ Unauthorized access
- ❌ Identity theft
- ❌ Corporate espionage
- ❌ Any illegal activity

## Legal Notice

Users are solely responsible for compliance with:
- Computer Fraud and Abuse Act (CFAA)
- Local computer crime laws
- Corporate policies
- Terms of service agreements

Misuse may result in:
- Criminal prosecution
- Civil liability
- Employment termination
- Academic consequences

## Contact

**Security Issues:** ziadsaghir8@gmail.com  
**General Questions:** GitHub Issues  
**Community:** GitHub Discussions

---

*Last Updated: January 2026*
