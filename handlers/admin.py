from aiogram import types
from config import is_admin
from keyboards.admin import admin_panel

async def admin_panel_handler(message: types.Message):
    if not is_admin(message.from_user.id):
        await message.answer("❌ Доступ запрещен!")
        return
    await message.answer("Админ-панель:", reply_markup=admin_panel())

async def admin_button_handler(message: types.Message):
    if not is_admin(message.from_user.id):
        await message.answer("❌ Доступ запрещен!")
        return
    await admin_panel_handler(message)

async def show_stats(callback: types.CallbackQuery):
    if not is_admin(callback.from_user.id):
        await callback.answer("❌ Нет прав!", show_alert=True)
        return
    await callback.message.answer("📈 Статистика: 1000 пользователей")
    await callback.answer()

async def ban_user(callback: types.CallbackQuery):
    if not is_admin(callback.from_user.id):
        await callback.answer("❌ Нет прав!", show_alert=True)
        return
    await callback.message.answer("🔨 Функция бана пока не реализована.")
    await callback.answer()