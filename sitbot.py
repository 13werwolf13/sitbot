import telebot
import constants
import pinger

bot = telebot.TeleBot(constants.token)

"""
if pinger.alert1 == 1:
    bot.send_message(constants.chatid, pinger.text1)
if pinger.alert2 == 1:
    bot.send_message(constants.chatid, pinger.text2)
if pinger.alert3 == 1:
    bot.send_message(constants.chatid, pinger.text3)
if pinger.alert4 == 1:
    bot.send_message(constants.chatid, pinger.text4)
"""

@bot.message_handler(commands=['ping'])


def handle_text (message):
    pinger.startp()
    bot.send_message(constants.chatid, "pong")
    bot.send_message(constants.chatid, "pong")
    bot.send_message(constants.chatid, "pong")
    bot.send_message(constants.chatid, pinger.text1)
    bot.send_message(constants.chatid, pinger.text2)
    bot.send_message(constants.chatid, pinger.text3)
    bot.send_message(constants.chatid, pinger.text4)


bot.polling(none_stop=True, interval=0)