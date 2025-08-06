import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command

from config import config
from utils.commands import setup_bot_commands
from handlers.start import start_handler, help_handler
from handlers.user import show_menu, pizza_selected
from handlers.admin import admin_panel_handler, admin_button_handler, show_stats, ban_user


import asyncio


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

async def main():
    await setup_bot_commands(bot)

    dp.message.register(start_handler, Command("start"))
    dp.message.register(help_handler, Command("help"))
    dp.message.register(admin_panel_handler, Command("admin"))
    dp.message.register(admin_button_handler, F.text == "🛠 Админка")
    dp.message.register(show_menu, F.text == "🍕 Меню")

    dp.callback_query.register(pizza_selected, F.data.startswith("pizza_"))
    dp.callback_query.register(show_stats, F.data == "admin_stats")
    dp.callback_query.register(ban_user, F.data == "admin_ban")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
