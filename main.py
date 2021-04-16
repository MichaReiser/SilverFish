#!/bin/python

import telegram
from telegram import Update, User
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, Updater

import os
from dotenv import load_dotenv
import logging          

load_dotenv()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

TOKEN = os.getenv('ACCESS_TOKEN')

def start_test(update: Update, context: CallbackContext) -> int:
    update.message.reply_chat_action(action="typing")
    update.message.reply_text(text="Hallihallo {user}. Ich bin der Silberfisch vom Wintower!".format(user=user_name(update.message.from_user)))

def handle_text_message(update: Update, context: CallbackContext) -> int:
    update.message.reply_chat_action("typing")
    update.message.reply_text(text="Your text: " + update.message.text)

def handle_error(update: Update, context: CallbackContext):
    logger.warning('Handling the update "%s" caused an error "%s"', update, context.error)
    if update and update.message:
        update.message.send_animation(animation="CgACAgQAAxkBAAMVYHm__nCB5m5X5Ki0dphIG6CQHuoAAjYCAAKXztRSxnPha9rxZUQfBA")

def user_name(user: User) -> str:
    return user.first_name or user.last_name or user.username

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_test))
    dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=handle_text_message))
    dispatcher.add_error_handler(handle_error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
