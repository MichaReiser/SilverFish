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

class PhotoMessage(Message):
    def __init__(self, photo_url, caption):
        super().__init__()
        self.photo = photo_url
        self.caption = caption
    
    def send(self, update: Update, reply_markup: ReplyMarkup = None) -> None:
        update.message.reply_photo(
            photo = self.photo,
            caption=self.caption,
        )