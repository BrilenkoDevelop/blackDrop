import telebot
from telebot import types

bot_token = "1377056545:AAEygm1eKZ37bofir_icosP_OguzzzabPek"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=["start"])
def start_comand(message):
    bot.send_message(message.from_user.id, "Приветсвие")
 
bot.polling()
