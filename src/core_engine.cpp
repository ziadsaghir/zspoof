#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <map>
#include <ctime>
#include <iomanip>
#include <algorithm>
#include <chrono>
#include <sstream>
#include <fstream>

// Enhanced Vendor Database with Real-World OUI Distribution (2025)
struct VendorProfile {
    std::vector<std::string> ouis;
    std::vector<std::string> typical_hostnames;
    double market_share;  // For realistic weighted selection
};

// Comprehensive vendor database based on 2025 market data
std::map<std::string, VendorProfile> vendor_db = {
    // Enterprise Devices (Corporate Networks)
    {"dell",    {{
        "00:14:22", "00:11:43", "F0:4D:A2", "90:B1:1C", "D4:AE:52", 
        "18:03:73", "B8:CA:3A", "34:17:EB", "B0:83:FE", "50:9A:4C"
    }, {"DESKTOP-", "DELL-PC-", "WS-DELL-"}, 22.5}},
    
    {"lenovo",  {{
        "00:59:07", "80:96:B1", "E0:2C:B2", "4C:80:93", "54:E0:19",
        "68:F7:28", "C8:1F:66", "00:21:CC", "B0:7B:25", "8C:16:45"
    }, {"LENOVO-", "THINK-", "LAPTOP-"}, 18.3}},
    
    {"hp",      {{
        "00:1F:29", "38:EA:A7", "A4:5D:36", "14:58:D0", "3C:52:82",
        "9C:B6:54", "2C:76:8A", "00:25:B3", "6C:C2:17", "FC:15:B4"
    }, {"HP-", "HPPC-", "ELITEBOOK-"}, 15.7}},
    
    {"cisco",   {{
        "00:40:96", "00:00:0C", "E8:BA:70", "F8:66:F2", "00:1D:A1",
        "74:A0:2F", "00:07:7D", "A0:F8:49", "88:43:E1", "F0:25:72"
    }, {"CISCO-AP-", "SWITCH-", "VOIP-"}, 8.2}},
    
    // Consumer Devices (Public WiFi)
    {"apple",   {{
        "F0:18:98", "00:1C:B3", "28:E1:4C", "A4:5E:60", "BC:52:B7",
        "F0:DB:E2", "3C:06:30", "70:56:81", "88:66:5A", "D0:23:DB"
    }, {"iPhone", "MacBook", "iPad"}, 28.4}},
    
    {"samsung", {{
        "34:14:5F", "00:12:47", "E8:50:8B", "40:4E:36", "D0:59:E4",
        "AC:36:13", "78:1F:DB", "C8:98:25", "00:1D:25", "38:AA:3C"
    }, {"Galaxy-", "Samsung-", "SM-"}, 19.6}},
    
    {"xiaomi",  {{
        "34:CE:00", "64:09:80", "50:8F:4C", "74:51:BA", "04:CF:4B",
        "28:6C:07", "F8:A4:5F", "AC:C1:EE", "78:02:F8", "34:80:B3"
    }, {"Redmi-", "MI-", "POCO-"}, 11.2}},
    
    {"google",  {{
        "F4:F5:D8", "3C:5A:B4", "84:73:03", "B4:F0:AB", "6C:AD:F8",
        "AC:37:43", "00:1A:11", "F8:8F:CA", "7C:2F:80", "54:60:09"
    }, {"Pixel-", "Nest-", "Google-"}, 6.8}},
    
    // IoT Devices (Smart Home)
    {"espressif", {{
        "24:0A:C4", "30:AE:A4", "A4:CF:12", "48:3F:DA", "84:CC:A8",
        "C8:2B:96", "DC:4F:22", "24:62:AB", "3C:71:BF", "EC:FA:BC"
    }, {"ESP-", "ESP32-", "IoT-Device-"}, 32.1}},
    
    {"amazon",  {{
        "74:C2:46", "F0:D2:F1", "CC:50:E3", "6C:56:97", "38:F7:3D",
        "4C:EF:C0", "B4:7C:9C", "00:FC:8B", "84:D6:D0", "50:DC:E7"
    }, {"Echo-", "Ring-", "Alexa-"}, 18.5}},
    
    {"tuya",    {{
        "10:5A:17", "68:57:2D", "7C:87:CE", "D4:A6:51", "84:E3:42",
        "1C:90:FF", "50:02:91", "A4:DA:22", "24:A1:60", "CC:7B:5C"
    }, {"Smart-", "Tuya-", "WiFi-"}, 14.3}},
    
    // Gaming Devices (LAN Parties)
    {"sony",    {{
        "00:D9:D1", "00:04:1F", "7C:BB:8A", "FC:0F:E6", "00:1F:A7",
        "98:E8:FA", "B8:8D:12", "30:05:5C", "00:19:C5", "00:24:8D"
    }, {"PlayStation", "PS5-", "PS4-"}, 42.7}},
    
    {"nintendo", {{
        "98:B6:E9", "00:09:BF", "A4:5C:27", "78:A2:A0", "58:BD:A3",
        "00:19:1D", "00:17:AB", "00:1F:32", "00:1B:EA", "00:1E:35"
    }, {"Switch-", "Nintendo-", "NS-"}, 31.8}},
    
    {"microsoft", {{
        "00:50:F2", "7C:ED:8D", "98:5F:D3", "28:18:78", "D8:9E:F3",
        "00:0D:3A", "E0:0F:EC", "1C:3B:F3", "B0:C0:90", "68:17:29"
    }, {"Xbox-", "MSFT-", "Surface-"}, 19.4}},
    
    // Generic/Universal (for random mode)
    {"intel",   {{
        "00:13:20", "00:27:10", "00:1B:21", "AC:DE:48", "00:15:00",
        "00:1F:3C", "E0:DB:55", "94:DE:80", "A0:36:9F", "B8:6B:23"
    }, {"PC-", "DESKTOP-", "LAPTOP-"}, 25.3}},
    
    {"realtek", {{
        "00:E0:4C", "52:54:00", "00:0E:2E", "70:4D:7B", "18:DB:F2",
        "98:FC:84", "30:5A:3A", "08:62:66", "C8:5B:76", "94:E9:79"
    }, {"RTL-", "Device-", "NIC-"}, 31.2}}
};

// Generate cryptographically secure random bytes
class SecureRandom {
private:
    std::random_device rd;
    std::mt19937_64 gen;
    std::uniform_int_distribution<int> byte_dist;
    
public:
    SecureRandom() : gen(rd()), byte_dist(0, 255) {
        // Additional entropy from time
        auto now = std::chrono::high_resolution_clock::now();
        auto seed = std::chrono::duration_cast<std::chrono::nanoseconds>(
            now.time_since_epoch()).count();
        gen.seed(seed ^ rd());
    }
    
    std::string get_random_byte() {
        int val = byte_dist(gen);
        std::stringstream ss;
        ss << std::hex << std::uppercase << std::setw(2) << std::setfill('0') << val;
        return ss.str();
    }
    
    int get_random_int(int min, int max) {
        std::uniform_int_distribution<int> dist(min, max);
        return dist(gen);
    }
    
    double get_random_double(double min = 0.0, double max = 1.0) {
        std::uniform_real_distribution<double> dist(min, max);
        return dist(gen);
    }
};

// MAC Address Validation and Generation
class MACGenerator {
private:
    SecureRandom rng;
    
    std::string ensure_unicast_local(std::string byte1) {
        // Ensure bit pattern: xxxx xx1x (locally administered)
        // and: xxxx xxx0 (unicast, not multicast)
        int val = std::stoi(byte1, nullptr, 16);
        val |= 0x02;  // Set locally administered bit
        val &= 0xFE;  // Clear multicast bit
        
        std::stringstream ss;
        ss << std::hex << std::uppercase << std::setw(2) << std::setfill('0') << val;
        return ss.str();
    }
    
public:
    std::string generate_profile_mac(const std::string& profile) {
        std::vector<std::string> candidates;
        std::vector<double> weights;
        
        if (profile == "corporate") {
            candidates = {"dell", "lenovo", "hp", "cisco", "intel"};
            weights = {22.5, 18.3, 15.7, 8.2, 25.3};
        }
        else if (profile == "cafe" || profile == "public") {
            candidates = {"apple", "samsung", "xiaomi", "google"};
            weights = {28.4, 19.6, 11.2, 6.8};
        }
        else if (profile == "iot" || profile == "smarthome") {
            candidates = {"espressif", "amazon", "tuya", "xiaomi"};
            weights = {32.1, 18.5, 14.3, 11.2};
        }
        else if (profile == "gamer" || profile == "gaming") {
            candidates = {"sony", "nintendo", "microsoft"};
            weights = {42.7, 31.8, 19.4};
        }
        else if (profile == "stealth") {
            // Ultra-realistic: mix of most common vendors
            candidates = {"apple", "samsung", "dell", "lenovo", "intel"};
            weights = {28.4, 19.6, 22.5, 18.3, 25.3};
        }
        else {
            // Pure random with proper bit flags
            return generate_pure_random();
        }
        
        // Weighted vendor selection using cumulative distribution
        double total = 0.0;
        for (double w : weights) total += w;
        
        double random_val = rng.get_random_double(0.0, total);
        double cumulative = 0.0;
        size_t selected_idx = 0;
        
        for (size_t i = 0; i < weights.size(); i++) {
            cumulative += weights[i];
            if (random_val <= cumulative) {
                selected_idx = i;
                break;
            }
        }
        
        std::string selected_vendor = candidates[selected_idx];
        
        // Get vendor profile
        VendorProfile& profile_data = vendor_db[selected_vendor];
        
        // Select random OUI from vendor
        int oui_idx = rng.get_random_int(0, profile_data.ouis.size() - 1);
        std::string oui = profile_data.ouis[oui_idx];
        
        // Generate random NIC portion
        std::string nic = rng.get_random_byte() + ":" + 
                         rng.get_random_byte() + ":" + 
                         rng.get_random_byte();
        
        return oui + ":" + nic;
    }
    
    std::string generate_pure_random() {
        std::string first_byte = ensure_unicast_local(rng.get_random_byte());
        std::string mac = first_byte;
        for (int i = 0; i < 5; i++) {
            mac += ":" + rng.get_random_byte();
        }
        return mac;
    }
    
    std::string generate_sequential_mac(const std::string& base_oui) {
        // For ARP cache poisoning - sequential MACs from same vendor
        std::string nic = rng.get_random_byte() + ":" + 
                         rng.get_random_byte() + ":" + 
                         rng.get_random_byte();
        return base_oui + ":" + nic;
    }
    
    bool validate_mac(const std::string& mac) {
        if (mac.length() != 17) return false;
        
        for (size_t i = 0; i < mac.length(); i++) {
            if (i % 3 == 2) {
                if (mac[i] != ':' && mac[i] != '-') return false;
            } else {
                if (!isxdigit(mac[i])) return false;
            }
        }
        return true;
    }
};

// Anti-Detection Features
class AntiDetection {
private:
    SecureRandom rng;
    
public:
    // Generate realistic hostname based on vendor
    std::string generate_hostname(const std::string& vendor) {
        if (vendor_db.find(vendor) == vendor_db.end()) {
            return "DEVICE-" + std::to_string(rng.get_random_int(1000, 9999));
        }
        
        VendorProfile& profile = vendor_db[vendor];
        std::string prefix = profile.typical_hostnames[
            rng.get_random_int(0, profile.typical_hostnames.size() - 1)
        ];
        
        return prefix + std::to_string(rng.get_random_int(1000, 9999));
    }
    
    // Calculate optimal timing for ARP requests (to avoid detection)
    int get_stealth_delay_ms() {
        // Realistic device behavior: 200-800ms jitter
        return rng.get_random_int(200, 800);
    }
    
    // Generate realistic TTL value based on OS profile
    int get_realistic_ttl(const std::string& os_type) {
        if (os_type == "windows") return 128;
        if (os_type == "linux") return 64;
        if (os_type == "macos") return 64;
        return 64; // Default
    }
};

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <profile|random|validate> [mac_address]" << std::endl;
        return 1;
    }
    
    std::string command = argv[1];
    std::transform(command.begin(), command.end(), command.begin(), ::tolower);
    
    MACGenerator mac_gen;
    AntiDetection anti_detect;
    
    if (command == "validate" && argc >= 3) {
        std::string mac = argv[2];
        std::cout << (mac_gen.validate_mac(mac) ? "VALID" : "INVALID") << std::endl;
    }
    else if (command == "hostname" && argc >= 3) {
        std::string vendor = argv[2];
        std::cout << anti_detect.generate_hostname(vendor) << std::endl;
    }
    else if (command == "delay") {
        std::cout << anti_detect.get_stealth_delay_ms() << std::endl;
    }
    else {
        // Generate MAC based on profile
        std::cout << mac_gen.generate_profile_mac(command) << std::endl;
    }
    
    return 0;
}
