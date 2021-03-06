import random

from typing import List
from telegram import Update, ReplyMarkup, MessageEntity, InputMediaPhoto

class Message:
    def send(self, update: Update, reply_markup: ReplyMarkup = None):
        raise NotImplementedError("Please implement in your subclass")

class TextMessage(Message):
    """
    Sends a text message. You can use Markdown in the text if you set markdown to True.
    But make sure to escape all ASCII characters with codes in [1, 127] (e.g. .-_) with a backlsash
    """
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
    """
    Sends a message with a photo and caption
    """
    def __init__(self, photo_url: str, caption: str = None):
        super().__init__()
        self.photo = photo_url
        self.caption = caption
    
    def send(self, update: Update, reply_markup: ReplyMarkup = None) -> None:
        update.message.reply_chat_action('upload_photo')
        update.message.reply_photo(
            photo = self.photo,
            caption=self.caption,
            reply_markup=reply_markup,
        )

class AnimationMessage(Message):
    """
    Sends a animation (GIF or video)
    """
    def __init__(self, animation_url: str, caption: str = None):
        super().__init__()
        self.animation_url = animation_url
        self.caption = caption
    
    def send(self, update: Update, reply_markup: ReplyMarkup = None) -> None:
        update.message.reply_chat_action('upload_photo')
        update.message.reply_animation(
            animation = self.animation_url,
            caption=self.caption,
            reply_markup=reply_markup,
        )

class MedieGroupMessage(Message):
    """
    Sends multiple photos in a single message
    """
    def __init__(self, media: List[InputMediaPhoto]):
        super().__init__()

        if len(media) < 2:
            raise Exception("You must specify at least two items")

        self.media = media

    def send(self, update: Update, reply_markup: ReplyMarkup = None) -> None:
        update.message.reply_chat_action('upload_photo')
        update.message.reply_media_group(
            media=self.media,
        )

class RandomMessage(Message):
    """
    Sends a random message from the given list of messages
    """
    def __init__(self, messages: List[Message]):
        super().__init__()
        self.messages = messages

    def send(self, update: Update, reply_markup: ReplyMarkup = None) -> None:
        message= random.choice(self.messages)
        message.send(update, reply_markup)