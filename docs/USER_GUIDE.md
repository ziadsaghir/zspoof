# ZSPOOF User Manual

## 🔰 Getting Started for Beginners

**ZSPOOF** is a tool that changes your computer's "digital fingerprint" (MAC Address). This is useful for privacy, testing network security, or bypassing MAC filters.

### Step 1: Installation
You don't need to be a coder to install this. Just open your terminal (Ctrl+Alt+T) and copy-paste these 3 lines one by one:

```bash
# 1. Download the tool
git clone [https://github.com/YOUR_USERNAME/zspoof.git](https://github.com/YOUR_USERNAME/zspoof.git)

# 2. Enter the folder
cd zspoof

# 3. Start the engine (You will be asked for your password)
make run

The Modes Explained

Once the tool starts, you will see a menu. Here is what each option actually does:
[1] Manually enter a MAC address

Best for: Specific testing. If you know exactly what MAC address you want (e.g., 00:11:22:33:44:55), use this. The tool will check if you typed it correctly and apply it.
[2] Vendor Masquerade (Stealth Mode) - RECOMMENDED

Best for: Hiding in plain sight. Network admins often look for "weird" devices. This mode makes you look like a normal device that belongs there.

    Corporate: Makes you look like a Dell/Lenovo work laptop. Use this in offices.

    Cafe: Makes you look like an iPhone or Samsung. Use this in Starbucks/Airports.

    Gamer: Makes you look like a Nintendo Switch. Use this at LAN parties.

    IoT: Makes you look like a smart home device (Alexa/Smart Bulb).

[3] Randomize (YOLO Mode)

Best for: Maximum privacy at home. This generates a completely random identity. Note that some strict enterprise networks might block this if the vendor looks "unknown."
❓ Troubleshooting

"It says Command not found when I type make!" You need to install the builder. Run this: sudo apt install build-essential

"It says ModuleNotFoundError: No module named tqdm" You are missing the progress bar library. Run this: pip install tqdm

"My internet stopped working!" Don't panic. This happens if the new MAC isn't accepted by your router.

    Fix 1: Run the tool again and choose a legitimate profile (like "Apple").

    Fix 2: Restart your computer. Your original MAC is always restored on reboot.

# [Ziad SAGHIR] - 2025/26