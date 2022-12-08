import telebot

from telegram import send_message, URL


bot = telebot.TeleBot("TOKEN", parse_mode=None)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the MABot, enter your trading pair", parse_mode="html")


@bot.message_handler()
def rating(message):
    try:
        bot.send_photo(message.chat.id, f"{URL}{send_message(message)}", "Trading pair rating", parse_mode="html")
    except IndexError:
        bot.send_message(message.chat.id, "Oops, something went wrong, please try again")


bot.polling()
