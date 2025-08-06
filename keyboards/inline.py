from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

def pizza_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="Пепперони", callback_data="pizza_pepperoni")
    builder.button(text="Маргарита", callback_data="pizza_margarita")
    return builder.as_markup()