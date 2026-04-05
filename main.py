import logging
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- ИМПОРТЫ ТВОИХ ФАЙЛОВ ---
import keyboards as kb           # Исправляет ошибку "kb" is not defined
from config import TOKEN         # Убедись, что токен в config.py
from payments import create_payment_url 

# --- ИНИЦИАЛИЗАЦИЯ (Исправляет "dp" is not defined) ---
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Состояния для доната
class DonateState(StatesGroup):
    waiting_for_amount = State()

# --- ХЕНДЛЕРЫ ---

# Кнопка "Поддержать проект"
@dp.callback_query(F.data == "buy_key")
async def buy_key_start(cb: types.CallbackQuery, state: FSMContext):
    try:
        await cb.message.edit_text(
            "💎 **Поддержка проекта**\n\nВведите сумму пожертвования в рублях (минимум 100):", 
            reply_markup=kb.back_to_menu_kb(),
            parse_mode="Markdown"
        )
        await state.set_state(DonateState.waiting_for_amount)
    except Exception as e:
        logging.error(f"Ошибка в buy_key_start: {e}")

# Хендлер на ввод текста (суммы)
@dp.message(DonateState.waiting_for_amount)
async def process_donate_amount(message: types.Message, state: FSMContext):
    # Проверка: число ли это и больше ли оно 100
    if not message.text.isdigit() or int(message.text) < 100:
        await message.answer("❌ Пожалуйста, введите корректное число (минимум 100).")
        return
    
    amount = int(message.text)
    
    # Генерируем ссылку на оплату
    try:
        url, payment_id = await create_payment_url(amount, message.from_user.id)
        
        pay_kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💳 Оплатить", url=url)],
            [InlineKeyboardButton(text="« Назад", callback_data="to_main")]
        ])
        
        await message.answer(
            f"✅ Сумма: **{amount}₽**\nНажмите кнопку ниже, чтобы перейти к оплате:", 
            reply_markup=pay_kb,
            parse_mode="Markdown"
        )
        # Очищаем состояние только после успешной генерации ссылки
        await state.clear()
        
    except Exception as e:
        await message.answer("⚠️ Произошла ошибка при создании платежа. Попробуйте позже.")
        logging.error(f"Ошибка оплаты: {e}")

# --- ЗАПУСК БОТА ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())