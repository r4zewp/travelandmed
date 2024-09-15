from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config.models.country import Country
from config.models.city import City

def build_countries_kb(countries: [Country], selected_options: [str], uid: int) -> InlineKeyboardMarkup:
    """
    Creates a dynamic country keyboard with buttons arranged in rows of up to three buttons.
    :param uid:
    :param countries: List[Country]
    :param selected_options: List[str]
    :return: InlineKeyboardMarkup
    """
    buttons = []
    for country in countries:
        text = f"✅{country.name_ru}" if country.name in selected_options else country.name_ru
        callback_data = f"country_{country.name}"
        button = InlineKeyboardButton(text=text, callback_data=callback_data)
        buttons.append(button)

    keyboard = [buttons[i:i+3] for i in range(0, len(buttons), 3)]
    keyboard.append([InlineKeyboardButton(text='Подтвердить выбор', callback_data=f'confirm_{uid}')])
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup