#!/usr/bin/env python3
"""
ZSPOOF v3.0.0 - Test Suite
Comprehensive validation tests
"""

import subprocess
import re
import sys
from pathlib import Path

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'

def test_engine_exists():
    """Test if engine binary exists"""
    engine = Path(__file__).parent.parent / "bin" / "core_engine"
    if engine.exists():
        print(f"{Colors.GREEN}✓ PASS{Colors.ENDC} Engine binary exists")
        return True
    else:
        print(f"{Colors.RED}✗ FAIL{Colors.ENDC} Engine binary not found")
        return False

def test_mac_format(mac):
    """Validate MAC address format"""
    pattern = r'^([0-9A-F]{2}:){5}[0-9A-F]{2}$'
    return bool(re.match(pattern, mac))

def test_profile(profile):
    """Test MAC generation for a profile"""
    engine = Path(__file__).parent.parent / "bin" / "core_engine"
    try:
        result = subprocess.run([str(engine), profile], 
                              capture_output=True, text=True, timeout=5)
        mac = result.stdout.strip()
        
        if test_mac_format(mac):
            print(f"{Colors.GREEN}✓ PASS{Colors.ENDC} Generate {profile} profile: {mac}")
            return True
        else:
            print(f"{Colors.RED}✗ FAIL{Colors.ENDC} Invalid MAC format for {profile}: {mac}")
            return False
    except Exception as e:
        print(f"{Colors.RED}✗ FAIL{Colors.ENDC} Profile {profile} error: {e}")
        return False

def test_uniqueness():
    """Test MAC uniqueness"""
    engine = Path(__file__).parent.parent / "bin" / "core_engine"
    macs = set()
    
    for _ in range(100):
        result = subprocess.run([str(engine), "random"], 
                              capture_output=True, text=True, timeout=5)
        macs.add(result.stdout.strip())
    
    if len(macs) > 95:  # Allow small collision probability
        print(f"{Colors.GREEN}✓ PASS{Colors.ENDC} Uniqueness test: {len(macs)}/100 unique")
        return True
    else:
        print(f"{Colors.RED}✗ FAIL{Colors.ENDC} Too many collisions: {len(macs)}/100")
        return False

def test_unicast_bit():
    """Test that generated MACs are unicast (not multicast)"""
    engine = Path(__file__).parent.parent / "bin" / "core_engine"
    
    for _ in range(20):
        result = subprocess.run([str(engine), "random"], 
                              capture_output=True, text=True, timeout=5)
        mac = result.stdout.strip()
        first_byte = int(mac[:2], 16)
        
        if first_byte & 0x01:  # Check multicast bit
            print(f"{Colors.RED}✗ FAIL{Colors.ENDC} Multicast MAC generated: {mac}")
            return False
    
    print(f"{Colors.GREEN}✓ PASS{Colors.ENDC} All MACs are unicast")
    return True

def test_local_admin_bit():
    """Test locally administered bit for random MACs"""
    engine = Path(__file__).parent.parent / "bin" / "core_engine"
    
    for _ in range(20):
        result = subprocess.run([str(engine), "random"], 
                              capture_output=True, text=True, timeout=5)
        mac = result.stdout.strip()
        first_byte = int(mac[:2], 16)
        
        if not (first_byte & 0x02):  # Check local admin bit
            print(f"{Colors.YELLOW}⚠ WARN{Colors.ENDC} Not locally administered: {mac}")
    
    print(f"{Colors.GREEN}✓ PASS{Colors.ENDC} Local admin bit test completed")
    return True

def main():
    """Run all tests"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BLUE}ZSPOOF v3.0.0 - Test Suite{Colors.ENDC}")
    print(f"{Colors.BLUE}{'='*60}{Colors.ENDC}\n")
    
    tests = []
    
    # Engine tests
    tests.append(test_engine_exists())
    
    # Profile tests
    profiles = ['corporate', 'cafe', 'iot', 'gamer', 'stealth', 'random']
    for profile in profiles:
        tests.append(test_profile(profile))
    
    # Advanced tests
    tests.append(test_uniqueness())
    tests.append(test_unicast_bit())
    tests.append(test_local_admin_bit())
    
    # Summary
    passed = sum(tests)
    total = len(tests)
    
    print(f"\n{Colors.BLUE}{'='*60}{Colors.ENDC}")
    if passed == total:
        print(f"{Colors.GREEN}✓ ALL TESTS PASSED ({passed}/{total}){Colors.ENDC}")
        print(f"{Colors.BLUE}{'='*60}{Colors.ENDC}\n")
        return 0
    else:
        print(f"{Colors.RED}✗ SOME TESTS FAILED ({passed}/{total}){Colors.ENDC}")
        print(f"{Colors.BLUE}{'='*60}{Colors.ENDC}\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
