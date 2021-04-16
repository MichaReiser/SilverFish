#!/bin/python

from telegram import Update, User, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, Updater, ConversationHandler
from option import Option, ChoiceOption, Options

import os
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

TOKEN = os.getenv('ACCESS_TOKEN')
HUH_FILE_ID = 'CgACAgQAAxkBAAMPYHno7oe6lq15sZRRudHW7aRfSeQAAisCAALMf5RSy6bOGPE0HKUfBA'
OHOH_FILE_ID = 'CgACAgQAAxkBAAOBYHnyx4IlMA69PINFGa7Zjub1_HYAAj0CAAK-4sRSwWafFSpUMNMfBA'

OPTIONS = Options([
    ChoiceOption(
        uri="/", 
        label="DON't offer this as an option or you'll be fired", 
        message="Was interessiert dich",
        choices=["/sisi", "/drinkinghabits"]
    ),
    ChoiceOption(
        uri="/sisi", 
        label="Sisi", 
        message="Du interessierst dich für die Kaiserin Elisabeth von Österreich. Ich habe ganz viele Objekte von ihr hier. Soll ich dir etwas über ihre Schuhe oder über ihr Klavier erzählen?",
        choices=["/",]
    ),
    ChoiceOption(
        uri="/drinkinghabits",
        label="Trinkgewohnheiten",
        message="Kaffee oder Alkohol?",
        choices=["/"]
    )
])

HANDLE_RESPONSE = range(1)

def send_welcome_message(update: Update, context: CallbackContext) -> int:
    update.message.reply_chat_action(action="typing")
    update.message.reply_animation(
        animation="CgACAgQAAxkBAANkYHntZf7AClZzlRQzg8GSvzQcc7YAAmgJAALbAclTnENXyJvfCgIfBA",
        caption="Oh, hallihallo {user}. Ich bin der Silberfisch vom Wintower. Ich lebe hier zwischen den Kisten, Büchern und allerlei alten Objekten. Gerne erzähle ich dir etwas über die Sammlung.".format(user=user_name(update.message.from_user)),
    )

    return enter_option(OPTIONS.options[0], update, context)

def enter_option(option: Option, update: Update, context: CallbackContext) -> int:
    context.user_data['option'] = option.uri

    option.reply(update, context, OPTIONS)

    return HANDLE_RESPONSE

def reply_with_buttoned_question(update: Update, context: CallbackContext, question: str, options: [str]) -> int:
    buttons = []
    for option in options:
        buttons.append(InlineKeyboardButton(text=option, callback_data=option))
	
    markup = InlineKeyboardMarkup([buttons])
    update.message.reply_text(text=question, reply_markup=markup)

def handle_topic_selection(update: Update, context: CallbackContext) -> int:
    update.message.reply_chat_action("typing")

    option = OPTIONS.get_option(context.user_data['option'])
    next_option = option.handle_response(update, context, OPTIONS)

    if not next_option:
        # No new option, stay in current option
        return HANDLE_RESPONSE

    enter_option(next_option, update, context)

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
