#!/bin/python

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

import os
from dotenv import load_dotenv
import logging



load_dotenv()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TOKEN = os.getenv('ACCESS_TOKEN')

def start_test(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def main():
    # bot = telegram.Bot(token=TOKEN)
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start_test', start_test))

    updater.start_polling()

if __name__ == '__main__':
    print(TOKEN)
    main()






