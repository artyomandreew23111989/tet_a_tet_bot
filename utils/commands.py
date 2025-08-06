from aiogram.types import BotCommand, BotCommandScopeChat
from config import config

async def setup_bot_commands(bot):
    commands = [
        BotCommand(command="start", description="🚀 Начать работу с ботом"),
        BotCommand(command="help", description="🆘 Получить помощь"),
        BotCommand(command="settings", description="⚙️ Настройки профиля"),
        BotCommand(command="check", description="🔍 Проверить статус")
    ]
    
    for admin_id in config.ADMINS:
        await bot.set_my_commands(
            commands=[
                BotCommand(command="admin", description="🛠 Админ-панель"),
                BotCommand(command="stats", description="📈 Статистика")
            ],
            scope=BotCommandScopeChat(chat_id=admin_id)
        )
    
    await bot.set_my_commands(commands)