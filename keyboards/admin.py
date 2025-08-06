from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_panel() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔨 Забанить", callback_data="admin_ban")],
        [InlineKeyboardButton(text="📊 Статистика", callback_data="admin_stats")]
    ])