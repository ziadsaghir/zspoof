#!/usr/bin/env python3
"""
ZSPOOF ULTIMATE - Test Suite
Validates MAC generation engine and core functionality
"""

import subprocess
import sys
import re
from pathlib import Path

# Colors for test output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_test(name, passed, details=""):
    """Print test result"""
    status = f"{Colors.GREEN}✓ PASS{Colors.ENDC}" if passed else f"{Colors.RED}✗ FAIL{Colors.ENDC}"
    print(f"  {status} {name}")
    if details:
        print(f"      {Colors.CYAN}{details}{Colors.ENDC}")

def validate_mac(mac):
    """Validate MAC address format"""
    pattern = r'^([0-9A-F]{2}:){5}[0-9A-F]{2}$'
    return bool(re.match(pattern, mac))

def check_unicast_local(mac):
    """Check if MAC has proper unicast and locally-administered bits"""
    first_byte = int(mac.split(':')[0], 16)
    is_unicast = (first_byte & 0x01) == 0  # Bit 0 should be 0
    is_local = (first_byte & 0x02) != 0     # Bit 1 should be 1 for local
    return is_unicast, is_local

def run_engine_test(binary_path, profile):
    """Run engine with profile and return MAC"""
    try:
        result = subprocess.run(
            [binary_path, profile],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout.strip()
    except Exception as e:
        return f"ERROR: {e}"

def main():
    """Run all tests"""
    print(f"\n{Colors.BOLD}ZSPOOF ULTIMATE - Test Suite{Colors.ENDC}\n")
    
    # Find binary
    binary_path = Path("bin/core_engine")
    if not binary_path.exists():
        binary_path = Path("bin/core_engine.exe")
    
    if not binary_path.exists():
        print(f"{Colors.RED}✗ Engine binary not found!{Colors.ENDC}")
        print(f"  Run 'make' first to compile the engine.")
        sys.exit(1)
    
    print(f"{Colors.CYAN}Using binary: {binary_path}{Colors.ENDC}\n")
    
    total_tests = 0
    passed_tests = 0
    
    # Test 1: Binary execution
    print(f"{Colors.BOLD}[1] Binary Execution Tests{Colors.ENDC}")
    try:
        result = subprocess.run([binary_path, "random"], capture_output=True, timeout=5)
        success = result.returncode == 0
        print_test("Engine executes without errors", success)
        total_tests += 1
        passed_tests += success
    except Exception as e:
        print_test("Engine executes without errors", False, str(e))
        total_tests += 1
    
    # Test 2: Profile generation tests
    print(f"\n{Colors.BOLD}[2] Profile Generation Tests{Colors.ENDC}")
    profiles = ["corporate", "cafe", "iot", "gamer", "stealth", "random"]
    
    for profile in profiles:
        mac = run_engine_test(binary_path, profile)
        valid = validate_mac(mac)
        print_test(f"Generate {profile} profile", valid, mac if valid else "Invalid format")
        total_tests += 1
        passed_tests += valid
    
    # Test 3: MAC format validation
    print(f"\n{Colors.BOLD}[3] MAC Format Validation Tests{Colors.ENDC}")
    
    # Generate 10 random MACs and validate all
    all_valid = True
    macs = []
    for _ in range(10):
        mac = run_engine_test(binary_path, "random")
        macs.append(mac)
        if not validate_mac(mac):
            all_valid = False
    
    print_test("All random MACs have valid format", all_valid, 
               f"Tested {len(macs)} MACs")
    total_tests += 1
    passed_tests += all_valid
    
    # Test 4: Unicast/Local bit validation
    print(f"\n{Colors.BOLD}[4] Bit Pattern Validation Tests{Colors.ENDC}")
    
    correct_bits = 0
    total_bit_tests = 20
    
    for _ in range(total_bit_tests):
        mac = run_engine_test(binary_path, "random")
        is_unicast, is_local = check_unicast_local(mac)
        
        if is_unicast:  # Should always be unicast
            correct_bits += 1
    
    bit_test_passed = correct_bits == total_bit_tests
    print_test("Unicast bit correctly set", bit_test_passed,
               f"{correct_bits}/{total_bit_tests} correct")
    total_tests += 1
    passed_tests += bit_test_passed
    
    # Test 5: Uniqueness test
    print(f"\n{Colors.BOLD}[5] Randomness/Uniqueness Tests{Colors.ENDC}")
    
    test_macs = set()
    for _ in range(100):
        mac = run_engine_test(binary_path, "random")
        test_macs.add(mac)
    
    uniqueness = len(test_macs) / 100.0
    uniqueness_passed = uniqueness > 0.95  # 95% should be unique
    print_test("High uniqueness in random generation", uniqueness_passed,
               f"{len(test_macs)}/100 unique ({uniqueness*100:.1f}%)")
    total_tests += 1
    passed_tests += uniqueness_passed
    
    # Test 6: Validation command
    print(f"\n{Colors.BOLD}[6] Validation Function Tests{Colors.ENDC}")
    
    test_cases = [
        ("00:11:22:33:44:55", True, "Valid MAC"),
        ("AA:BB:CC:DD:EE:FF", True, "Valid MAC (uppercase)"),
        ("00:11:22:33:44", False, "Too short"),
        ("00:11:22:33:44:55:66", False, "Too long"),
        ("GG:11:22:33:44:55", False, "Invalid hex"),
        ("00-11-22-33-44-55", False, "Wrong separator"),
    ]
    
    validation_tests_passed = 0
    for mac, expected_valid, description in test_cases:
        result = subprocess.run(
            [binary_path, "validate", mac],
            capture_output=True,
            text=True,
            timeout=5
        )
        is_valid = result.stdout.strip() == "VALID"
        test_passed = is_valid == expected_valid
        print_test(f"Validate: {description}", test_passed, mac)
        total_tests += 1
        if test_passed:
            passed_tests += 1
            validation_tests_passed += 1
    
    # Test 7: Performance test
    print(f"\n{Colors.BOLD}[7] Performance Tests{Colors.ENDC}")
    
    import time
    start = time.time()
    for _ in range(1000):
        subprocess.run([binary_path, "random"], capture_output=True, timeout=5)
    elapsed = time.time() - start
    avg_time = elapsed / 1000 * 1000  # ms per generation
    
    perf_passed = avg_time < 10  # Should be < 10ms per generation
    print_test("Performance (1000 generations)", perf_passed,
               f"Average: {avg_time:.2f}ms per MAC")
    total_tests += 1
    passed_tests += perf_passed
    
    # Final summary
    print(f"\n{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}Test Summary{Colors.ENDC}")
    print(f"{'='*60}")
    print(f"Total Tests:  {total_tests}")
    print(f"Passed:       {Colors.GREEN}{passed_tests}{Colors.ENDC}")
    print(f"Failed:       {Colors.RED}{total_tests - passed_tests}{Colors.ENDC}")
    print(f"Success Rate: {passed_tests/total_tests*100:.1f}%")
    print(f"{'='*60}\n")
    
    # Exit code
    if passed_tests == total_tests:
        print(f"{Colors.GREEN}{Colors.BOLD}✓ ALL TESTS PASSED{Colors.ENDC}\n")
        sys.exit(0)
    else:
        print(f"{Colors.RED}{Colors.BOLD}✗ SOME TESTS FAILED{Colors.ENDC}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
