from telebot import TeleBot
from envparse import Env

env = Env()

TOKEN = env.str("TOKEN")

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    c = 1


while True:
    print("Bot starting!")
    try:
        bot.polling()
    except Exception as err:
        print(err)
