from aiogram import Router, F
from aiogram.filters import Command
from handlers import start, user, admin

def setup_routers() -> list[Router]:
    routers = []

    # Start & Help
    start_router = Router()
    start_router.message.register(start.start_handler, Command("start"))
    start_router.message.register(start.help_handler, Command("help"))
    routers.append(start_router)

    # User Menu
    user_router = Router()
    user_router.message.register(user.show_menu, F.text == "🍕 Меню")
    user_router.callback_query.register(user.pizza_selected, F.data.startswith("pizza_"))
    routers.append(user_router)

    # Admin
    admin_router = Router()
    admin_router.message.register(admin.admin_panel_handler, Command("admin"))
    admin_router.message.register(admin.admin_button_handler, F.text == "🔧 Админка")
    admin_router.callback_query.register(admin.show_stats, F.data == "admin_stats")
    admin_router.callback_query.register(admin.ban_user, F.data == "admin_ban")
    routers.append(admin_router)

    return routers