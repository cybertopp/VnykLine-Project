# main.py
import logging
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import api_server
from config import TOKEN 

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

def main_menu():
    buttons = [
        [InlineKeyboardButton(text="🚀 Получить ключ", callback_data="get_key")],
        [InlineKeyboardButton(text="👤 Профиль", callback_data="profile"), InlineKeyboardButton(text="🎁 Бонусы", callback_data="bonuses")],
        [InlineKeyboardButton(text="🏆 ТОП-10", callback_data="top_10")],
        [InlineKeyboardButton(text="💎 Поддержать проект", callback_data="buy_key")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🦾 Добро пожаловать в **VnykLine**!", reply_markup=main_menu(), parse_mode="Markdown")

@dp.callback_query(F.data == "get_key")
async def handle_get_key(cb: types.CallbackQuery):
    await cb.answer("🛠 Генерирую...")
    try:
        res = api_server.get_or_create_user_link(cb.from_user.id)
        await cb.message.answer(res, parse_mode="Markdown")
    except Exception as e:
        logging.error(f"Ошибка при нажатии кнопки: {e}")
        await cb.message.answer("❌ Ошибка при создании ключа. Попробуй позже.")

async def main():
    print("--- БОТ ЗАПУЩЕН ---")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())