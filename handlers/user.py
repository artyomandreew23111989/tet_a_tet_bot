from aiogram import types
from keyboards.inline import pizza_menu

async def show_menu(message: types.Message):
    await message.answer("Выберите пиццу:", reply_markup=pizza_menu())

async def pizza_selected(callback: types.CallbackQuery):
    pizza_type = callback.data.split("_")[1]
    await callback.answer()  # уведомление без алерта
    await callback.message.edit_text(f"✅ Вы выбрали: {pizza_type}")