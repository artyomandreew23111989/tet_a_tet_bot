from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu(user_id: int, is_admin: bool = False) -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="🍕 Меню")],
        [KeyboardButton(text="📞 Контакты")]
    ]
    if is_admin:
        buttons.append([KeyboardButton(text="🛠 Админка")])
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )