#!/bin/python

from telegram import Update, User, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, Updater, ConversationHandler, CallbackQueryHandler
from options import get_option, OPTIONS
from option import Option
from constants import HUH_FILE_ID, OHOH_FILE_ID

import os
from dotenv import load_dotenv
import logging
import random

load_dotenv()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

TOKEN = os.getenv('ACCESS_TOKEN')
GO_BACK_TO_QUESTION = "Nein, bitte erzähle weiter"
HANDLE_RESPONSE, GO_BACK_TO_START = range(2)

def send_welcome_message(update: Update, context: CallbackContext) -> int:
    update.message.reply_chat_action("upload_photo")
    update.message.reply_animation(
        animation="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/fish_hi_gif.gif",
        caption="Oh, hallihallo {user}. Ich bin der Silberfisch vom Wintower. Ich lebe hier zwischen den Kisten, Büchern und allerlei alten Objekten. Gerne erzähle ich dir etwas über die Sammlung.".format(user=user_name(update.message.from_user)),
    )

    return enter_option(OPTIONS[0], update, context)

def enter_option(option: Option, update: Update, context: CallbackContext) -> int:
    context.user_data['option'] = option.uri

    update.message.reply_chat_action(action="typing")
    context.job_queue.run_once(lambda _c: option.reply(update, context, get_option), random.randrange(1, 3))
    
    return HANDLE_RESPONSE

def handle_topic_selection_inline(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    option = get_option(context.user_data['option'])
    next_option = option.handle_response(update, context, get_option)
    enter_option(next_option, update, context)
    return HANDLE_RESPONSE

def handle_topic_selection(update: Update, context: CallbackContext) -> int:
    update.message.reply_chat_action("typing")

    option = get_option(context.user_data['option'])
    next_option = option.handle_response(update, context, get_option)

    if not next_option:    
        update.message.reply_animation(
            animation=HUH_FILE_ID,
            reply_markup=ReplyKeyboardMarkup([["Ja"], [GO_BACK_TO_QUESTION]], one_time_keyboard=True),
            caption="Das habe ich nicht verstanden, möchtest du ein anders Thema auswählen?"
        )

        return GO_BACK_TO_START

    enter_option(next_option, update, context)

def go_back_start(update: Update, context: CallbackContext) -> int:
    update.message.reply_chat_action("typing")
    answer = update.message.text

    if answer == GO_BACK_TO_QUESTION:
        option = get_option(context.user_data['option'])
    else:
        option = get_option("/restart")
    
    enter_option(option, update, context)
    
    return HANDLE_RESPONSE

def handle_unknown_message(update: Update, context: CallbackContext) -> int:
    # Huh
    update.message.reply_animation(
        animation=HUH_FILE_ID,
    )

    return ConversationHandler.END

def handle_error(update: Update, context: CallbackContext):
    logger.error('Handling the update "%s" caused an error "%s"', update, context.error, exc_info=context.error)
    if update and update.message:
        # Ohoh
        update.message.reply_animation(animation=OHOH_FILE_ID, caption="Ohoh... das habe ich jetzt nicht ganz verstanden. Entschuldige.")
        
                                                  
def user_name(user: User) -> str:
    return user.first_name or user.last_name or user.username

def main():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', send_welcome_message)],
        states = {
            HANDLE_RESPONSE: [
                CommandHandler('start', send_welcome_message),
                CallbackQueryHandler(handle_topic_selection_inline),
                MessageHandler(Filters.text, handle_topic_selection)
            ],
            GO_BACK_TO_START: [
                CommandHandler('start', send_welcome_message),
                MessageHandler(Filters.text, go_back_start)
            ]
        },
        fallbacks=[ MessageHandler(Filters.all, handle_unknown_message)]
    )

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(conv_handler)
    dispatcher.add_error_handler(handle_error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
