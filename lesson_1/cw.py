from telebot import TeleBot
from envparse import Env

env = Env()

TOKEN = env.str("TOKEN")

bot = TeleBot(TOKEN)

while True:
    print("Bot starting!")
    try:
        bot.polling()
    except Exception as err:
        print(err)
