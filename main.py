#!/bin/python

from telegram import Update, User, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext, Updater, ConversationHandler

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
TOPICS = ['Sisi', 'Trinkgewohnheiten']

CHOOSE_TOPIC = range(1)

def send_welcome_message(update: Update, context: CallbackContext) -> int:
    update.message.reply_chat_action(action="typing")
    reply_markup = ReplyKeyboardMarkup([
        [topic] for topic in TOPICS],
    )
    update.message.reply_animation(
        animation="CgACAgQAAxkBAANkYHntZf7AClZzlRQzg8GSvzQcc7YAAmgJAALbAclTnENXyJvfCgIfBA",
        caption="Oh, hallihallo {user}. Ich bin der Silberfisch vom Wintower. Ich lebe hier zwischen den Kisten, Büchern und allerlei alten Objekten. Gerne erzähle ich dir etwas über die Sammlung. Was interessiert dich?".format(user=user_name(update.message.from_user)),
        reply_markup=reply_markup,
    )
    return CHOOSE_TOPIC

def reply_with_buttoned_question(update: Update, context: CallbackContext, question: str, options: [str]) -> int:
    buttons = []
    for option in options:
        buttons.append(InlineKeyboardButton(text=option, callback_data=option))
	
    markup = InlineKeyboardMarkup([buttons])
    update.message.reply_text(text=question, reply_markup=markup)

def handle_topic_selection(update: Update, context: CallbackContext) -> int:
    update.message.reply_chat_action("typing")
    topic = update.message.text


    if not topic in TOPICS:
        # Huh
        update.message.reply_animation(
            animation=HUH_FILE_ID,
        )
        return CHOOSE_TOPIC

    update.message.reply_text(text="Du interessierst dich für die Kaiserin Elisabeth von Österreich. Ich habe ganz viele Objekte von ihr hier. Soll ich dir etwas über ihre Schuhe oder über ihr Klavier erzählen?", reply_markup=ReplyKeyboardRemove())
    context.user_data['topic'] = topic

    return ConversationHandler.END

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
