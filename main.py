import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import config
from utils.commands import setup_bot_commands
from routers import setup_routers

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

async def on_startup(bot: Bot):
    logging.info("Бот запускается...")
    await setup_bot_commands(bot)

async def on_shutdown(bot: Bot):
    logging.info("Бот завершает работу...")

async def main():
    try:
        await on_startup(bot)
        
        # Регистрация всех роутеров (handlers)
        for router in setup_routers():
            dp.include_router(router)
        
        logging.info("Маршрутизаторы зарегистрированы. Начинаем опрос...")
        await dp.start_polling(bot)
    except Exception as e:
        logging.exception(f"Непредвиденная ошибка: {e}")
    finally:
        await on_shutdown(bot)

if __name__ == "__main__":
    asyncio.run(main())