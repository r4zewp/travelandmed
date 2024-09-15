from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import strings


def build_start_kb() -> ReplyKeyboardMarkup:
    button = KeyboardButton(text=strings.share_phone, request_contact=True)
    markup = ReplyKeyboardMarkup(keyboard=[[button]])
    return markup