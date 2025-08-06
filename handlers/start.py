from aiogram import types
from aiogram.filters import Command

from keyboards.main_menu import get_main_menu
from config import is_admin

async def start_handler(message: types.Message):
    await message.answer(
        "Добро пожаловать!",
        reply_markup=get_main_menu(message.from_user.id, is_admin(message.from_user.id))
    )

async def help_handler(message: types.Message):
    await message.answer("Доступные команды:\n/start - Начать\n/help - Помощь\n/settings - Настройки\n/check - Проверить статус")