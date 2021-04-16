#!/bin/python

from typing import List, Optional
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

from constants import HUH_FILE_ID, OHOH_FILE_ID

# Forward declaration?
class Options:
    pass

class Option:
    def __init__(self, uri: str, label: str):
        self.uri = uri
        self.label = label
    
    def reply(self, update: Update, context: CallbackContext, options: Options) -> None:
        raise NotImplementedError("Please implement reply")

    def handle_response(self, update: Update, context: CallbackContext, options: Options) -> bool:
        raise NotImplementedError("Please implement handle_response")

class Options:
    def __init__(self, options: List[Option]):
        self.options = options

    def get_option(self, uri: str) -> Optional[Option]:
        return next((option for option in self.options if option.uri == uri), None)

class ChoiceOption(Option):
    def __init__(self, uri: str, label: str, message: str, choices: List[str]):
        super().__init__(uri, label)
        self.message = message
        self.choices = choices

    def reply(self, update: Update, context: CallbackContext, options: Options):
        labels = [options.get_option(choice).label for choice in self.choices]
        reply_markup = ReplyKeyboardMarkup([
            [label] for label in labels],
        )

        update.message.reply_text(
            text=self.message,
            reply_markup=reply_markup
        )

    def handle_response(self, update: Update, context: CallbackContext, options: Options) -> Optional[Option]:
        topic = update.message.text

        choice_options = [options.get_option(choice) for choice in self.choices]
        selected = next((option for option in choice_options if option.label == topic), None)

        if not selected:    
            update.message.reply_animation(
                animation=HUH_FILE_ID,
            )
            return None

        return selected

