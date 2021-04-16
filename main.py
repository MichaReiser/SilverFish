#!/bin/python

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

bot = telegram.Bot(token='TOKEN')

updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

def start_test(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start_test', start_test)
dispatcher.add_handler(start_handler)

updater.start_polling()
