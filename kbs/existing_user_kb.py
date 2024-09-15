from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import strings as s

def build_existing_user_kb() -> ReplyKeyboardMarkup:
    applications=KeyboardButton(text=s.applications)
    settings=KeyboardButton(text=s.profile_settings)

    return ReplyKeyboardMarkup(keyboard=[[applications, settings]])