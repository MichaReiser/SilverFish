#!/bin/python

from typing import List, Optional, Callable
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

from constants import HUH_FILE_ID, OHOH_FILE_ID

OptionResolver = Callable[[str], Optional['Option']]

class Option:
    def __init__(self, uri: str, label: str):
        self.uri = uri
        self.label = label
    
    def reply(self, update: Update, context: CallbackContext, get_option: OptionResolver) -> None:
        raise NotImplementedError("Please implement reply")

    def handle_response(self, update: Update, context: CallbackContext, get_option: OptionResolver) -> bool:
        raise NotImplementedError("Please implement handle_response")


class ChoiceOption(Option):
    def __init__(self, uri: str, label: str, message: str, choices: List[str]):
        super().__init__(uri, label)
        self.message = message
        self.choices = choices

    def reply_with_buttoned_question(self, update: Update, context: CallbackContext, question: str, options: List[str]) -> int:
        buttons = []
        for option in options:
            buttons.append(InlineKeyboardButton(text=option, callback_data=option))
	
        markup = InlineKeyboardMarkup([buttons])
        update.message.reply_text(text=question, reply_markup=markup)

    def reply(self, update: Update, context: CallbackContext, get_option: OptionResolver, inline: bool):
        labels = [get_option(choice).label for choice in self.choices]
        print(labels)
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(label, callback_data=label) for label in labels]])

        if inline:
            if update.callback_query is not None:
                query = update.callback_query
                query.edit_message_text(self.message, reply_markup=reply_markup)
            else:
                self.reply_with_buttoned_question(update, context, self.message, labels)
        else:
            reply_markup = ReplyKeyboardMarkup([[label] for label in labels])

            update.message.reply_text(
                text=self.message,
                reply_markup=reply_markup
            )

    def handle_response(self, update: Update, context: CallbackContext, get_option: OptionResolver) -> Optional[Option]:
        topic = update.callback_query.data if update.callback_query is not None else update.message.text
        print(topic)
        choice_options = [get_option(choice) for choice in self.choices]
        selected = next((option for option in choice_options if option.label == topic), None)

        if not selected:    
            update.message.reply_animation(
                animation=HUH_FILE_ID,
            )
            return None

        return selected

