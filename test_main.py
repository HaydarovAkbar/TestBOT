"""

sana: 11/05/2021
tuzuvchi: Haydarov Akbar

"""
from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from testbot.testMethod import *

Token = "1840386758:AAGTbVRsJfgSFaVjLpWk1-RFWOgUbmPnl9I"

updater = Updater(Token,use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler("start",start)
help_handler = CommandHandler("help",help)
text_handler = MessageHandler(Filters.text,main)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(text_handler)

updater.start_polling()
print("bot ishladi")