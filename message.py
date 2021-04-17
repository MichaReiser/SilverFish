from typing import List
from telegram import Update, ReplyMarkup, MessageEntity

class Message:
    def send(self, update: Update, reply_markup: ReplyMarkup = None):
        raise NotImplementedError("Please implement in your subclass")

class TextMessage(Message):
    def __init__(self, text: str, markdown: bool = False):
        super().__init__()
        self.text = text
        self.markdown = markdown

    def send(self, update: Update, reply_markup: ReplyMarkup = None) -> None:
        update.message.reply_text(
            text=self.text,
            reply_markup=reply_markup,
            parse_mode="MarkdownV2" if self.markdown else None
        )
