import telebot
import constants
import pinger

bot = telebot.TeleBot(constants.token)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(constants.chatid, "In order to know the status of servers, use the /PING command.")
    bot.send_message(constants.chatid, "More bot itself every half hour pings the server and lets you know if one of them fell.")

@bot.message_handler(commands=['ping'])
def handle_text(message):
    pinger.startp()
    bot.send_message(constants.chatid, "pong")
    bot.send_message(constants.chatid, "pong")
    bot.send_message(constants.chatid, "pong")
    bot.send_message(constants.chatid, pinger.text1)
    bot.send_message(constants.chatid, pinger.text2)
    bot.send_message(constants.chatid, pinger.text3)
    bot.send_message(constants.chatid, pinger.text4)


bot.polling(none_stop=True, interval=0)
