import telebot
from datetime import datetime
from flask import Flask
from threading import Thread

# 🔑 ضع توكن البوت هنا
BOT_TOKEN = input("PUT_YOUR_BOT_TOKEN_HERE")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def countdown(message):
    today = datetime.now()
    next_year = datetime(today.year + 1, 1, 1)
    remaining_days = (next_year - today).days

    bot.reply_to(
        message,
        f"⏳ باقي {remaining_days} يوم على بداية سنة {today.year + 1} 🎉"
    )

# ====== Web server for UptimeRobot ======
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=8080)

Thread(target=run).start()

# ====== Start bot ======
bot.infinity_polling()
