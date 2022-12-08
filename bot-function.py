import telebot

from telegram import send_message, URL


TOKEN = "5913717117:AAGIJCq8J4hG_yGFWwhBWih8auy5NvdX_dQ"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the MABot, enter your trading pair", parse_mode="html")


@bot.message_handler()
def rating(message):
    try:
        bot.send_photo(message.chat.id, f"{URL}{send_message(message)}", "Trading pair rating", parse_mode="html")
    except IndexError:
        bot.send_message(message.chat.id, "Oops, something went wrong, please try again")


if __name__ == "__main__":
     bot.polling(none_stop=True)
