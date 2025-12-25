#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <map>
#include <ctime>
#include <iomanip>


struct Vendor {

    std::vector<std::string> ouis;
};


enum ProfileType { CORPORATE, CAFE, IOT, GAMER, RANDOM };


std::map<std::string, Vendor> db = {
    {"dell",    {{"00:14:22", "00:11:43", "F0:4D:A2", "90:B1:1C"}}}, // Laptops
    {"lenovo",  {{"00:59:07", "80:96:B1", "E0:2C:B2"}}},            // Laptops
    {"cisco",   {{"00:40:96", "00:00:0C", "E8:BA:70"}}},            // VoIP/Infra
    {"apple",   {{"F0:18:98", "00:1C:B3", "28:E1:4C"}}},            // MacBooks/iPhones
    {"samsung", {{"34:14:5F", "00:12:47"}}},                        // Phones
    {"intel",   {{"00:13:20", "00:27:10"}}},                        // Generic Chips
    {"espressif",{{"24:0A:C4", "30:AE:A4"}}},                       // IoT Chips (ESP32)
    {"amazon",  {{"74:C2:46", "F0:D2:F1"}}},                        // Echo/Ring
    {"sony",    {{"00:D9:D1", "00:04:1F"}}},                        // PlayStation
    {"nintendo",{{"98:B6:E9", "00:09:BF"}}}                         // Switch
};


std::string get_random_byte(std::mt19937& rng) {
    std::uniform_int_distribution<int> dist(0, 255);
    int val = dist(rng);
    std::stringstream ss;
    ss << std::hex << std::uppercase << std::setw(2) << std::setfill('0') << val;
    return ss.str();
}


std::string generate_smart_mac(std::string profile_str) {
    std::mt19937 rng(static_cast<unsigned int>(std::time(nullptr)));
    

    std::vector<std::string> candidates;
    std::vector<double> weights;

    if (profile_str == "corporate") {
        candidates = {"dell", "lenovo", "apple", "cisco", "intel"};
        weights =    { 35.0,   30.0,     20.0,    10.0,    5.0   }; 
    } 
    else if (profile_str == "cafe") {
        candidates = {"apple", "samsung", "intel"};
        weights =    { 60.0,    30.0,     10.0  }; 
    }
    else if (profile_str == "iot") {
        candidates = {"espressif", "amazon", "apple"};
        weights =    { 50.0,       30.0,     20.0 }; 
    }
    else if (profile_str == "gamer") {
        candidates = {"sony", "nintendo", "intel"};
        weights =    { 40.0,   40.0,      20.0 }; 
    }
    else {

        std::string b1 = get_random_byte(rng);
        const char hex_chars[] = {'2', '6', 'A', 'E'};
        b1[1] = hex_chars[rng() % 4]; 
        
        std::string mac = b1;
        for(int i=0; i<5; i++) mac += ":" + get_random_byte(rng);
        return mac;
    }


    std::discrete_distribution<int> dist(weights.begin(), weights.end());
    std::string selected_vendor = candidates[dist(rng)];
    

    Vendor& v = db[selected_vendor];
    std::uniform_int_distribution<int> oui_dist(0, v.ouis.size() - 1);
    std::string oui = v.ouis[oui_dist(rng)];


    std::string nic_part = get_random_byte(rng) + ":" + get_random_byte(rng) + ":" + get_random_byte(rng);

    return oui + ":" + nic_part;
}

int main(int argc, char* argv[]) {
    std::string mode = (argc > 1) ? argv[1] : "random";
    for (auto & c: mode) c = tolower(c);
    
    std::cout << generate_smart_mac(mode);
    return 0;
}