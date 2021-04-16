#!/bin/python

from telegram import Update, User, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, Updater, ConversationHandler

import os
from dotenv import load_dotenv
import logging          

load_dotenv()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

TOKEN = os.getenv('ACCESS_TOKEN')
TOPICS = ['Sisi', 'Trinkgewohnheiten']

CHOOSE_TOPIC = range(2)

def send_welcome_message(update: Update, context: CallbackContext) -> int:
    update.message.reply_chat_action(action="typing")
    reply_markup = ReplyKeyboardMarkup([
        [topic] for topic in TOPICS],
    )

    update.message.reply_animation(
        animation="CgACAgQAAxkBAANkYHntZf7AClZzlRQzg8GSvzQcc7YAAmgJAALbAclTnENXyJvfCgIfBA",
        caption="Hallihallo {user}. Ich bin der Silberfisch vom Wintower!".format(user=user_name(update.message.from_user)),
        reply_markup=reply_markup,
    )

    return CHOOSE_TOPIC

def handle_topic_selection(update: Update, context: CallbackContext) -> int:
    update.message.reply_chat_action("typing")
    topic = update.message.text


    if not topic in TOPICS:
        # Huh
        update.message.reply_animation(
            animation="CgACAgQAAxkBAAMPYHno7oe6lq15sZRRudHW7aRfSeQAAisCAALMf5RSy6bOGPE0HKUfBA",
        )
        return CHOOSE_TOPIC

    update.message.reply_text(text="You selected the topic '{topic}'".format(topic=topic), reply_markup=ReplyKeyboardRemove())
    context.user_data['topic'] = topic

    return ConversationHandler.END

def handle_unknown_message(update: Update, context: CallbackContext) -> int:
    # Huh
    update.message.reply_animation(
        animation="CgACAgQAAxkBAAMPYHno7oe6lq15sZRRudHW7aRfSeQAAisCAALMf5RSy6bOGPE0HKUfBA",
    )

    return ConversationHandler.END

def handle_error(update: Update, context: CallbackContext):
    logger.error('Handling the update "%s" caused an error "%s"', update, context.error, exc_info=context.error)
    if update and update.message:
        # Ohoh
        update.message.reply_animation(animation="CgACAgQAAxkBAAMVYHm__nCB5m5X5Ki0dphIG6CQHuoAAjYCAAKXztRSxnPha9rxZUQfBA", caption="Ohoh....")
                                                  
def user_name(user: User) -> str:
    return user.first_name or user.last_name or user.username

def main():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', send_welcome_message)],
        states = {
            CHOOSE_TOPIC: [
                MessageHandler(Filters.text, handle_topic_selection)
            ]
        },
        fallbacks=[MessageHandler(Filters.all, handle_unknown_message)]
    )

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(conv_handler)
    dispatcher.add_error_handler(handle_error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
