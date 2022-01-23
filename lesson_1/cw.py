from telebot import TeleBot, types
from envparse import Env

env = Env()

TOKEN = env.str("TOKEN")

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    c = 1


# todo luchanos сюда можно прикрутить эластик
@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


while True:
    print("Bot starting!")
    try:
        bot.polling()
    except Exception as err:
        print(err)
