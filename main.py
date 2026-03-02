import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# --- КОНФИГУРАЦИЯ (ВСТАВЬ СВОИ ДАННЫЕ) ---
BOT_TOKEN = "8377215857:AAEO-pqlqrAvSpUAl_9xBu14Bq5bHXsU594"
PAYMENT_TOKEN = "ВАШ_ТЕСТОВЫЙ_ТОКЕН_РОБОКАССЫ_ИЛИ_ЮKASSA"

# Настройка логирования (чтобы видеть ошибки в терминале)
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- ПРИВЕТСТВИЕ ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="💎 Купить key", callback_data="buy_menu"))
    builder.row(types.InlineKeyboardButton(text="👤 Мой профиль", callback_data="profile"))
    builder.row(types.InlineKeyboardButton(text="📖 Инструкция", callback_data="help"))
    
    await message.answer(
        f"привет, {message.from_user.first_name}! 👋\n"
        "Добро пожаловать в **VnykLine** — быстрый и надежный сервис.\n\n"
        "Выберите нужное действие в меню ниже:",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )

# --- МЕНЮ ТАРИФОВ ---
@dp.callback_query(F.data == "buy_menu")
async def show_tariffs(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    # Цены в копейках: 4000 = 40 руб, 8000 = 80 руб
    builder.row(types.InlineKeyboardButton(text="🚀 Неделя — 40₽", callback_data="pay_40"))
    builder.row(types.InlineKeyboardButton(text="🔥 Месяц — 80₽", callback_data="pay_80"))
    builder.row(types.InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_start"))
    
    await callback.message.edit_text(
        "Выбери подходящий тариф:\n\n"
        "🔹 **Неделя**: идеально для теста\n"
        "🔹 **Месяц**: самая выгодная цена",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )

# --- ПРОЦЕСС ОПЛАТЫ ---
@dp.callback_query(F.data.startswith("pay_"))
async def send_invoice(callback: types.CallbackQuery):
    amount = 4000 if callback.data == "pay_40" else 8000
    label = "VnykLine: 7 дней" if callback.data == "pay_40" else "VnykLine: 30 дней"
    payload = "week_sub" if callback.data == "pay_40" else "month_sub"

    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title=label,
        description=f"Доступ к сервису VnykLine на выбранный период",
        payload=payload,
        provider_token=PAYMENT_TOKEN,
        currency="RUB",
        prices=[types.LabeledPrice(label=label, amount=amount)],
        start_parameter="vnykline-sub"
    )
    await callback.answer()

# --- ПОДТВЕРЖДЕНИЕ ПЛАТЕЖА (PRE-CHECKOUT) ---
@dp.pre_checkout_query()
async def process_pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# --- УСПЕШНАЯ ОПЛАТА ---
@dp.message(F.successful_payment)
async def success_payment(message: types.Message):
    payload = message.successful_payment.invoice_payload
    days = 7 if payload == "week_sub" else 30
    
    await message.answer(
        f"✅ **Оплата прошла успешно!**\n\n"
        f"Вы приобрели подписку на {days} дней.\n"
        "Сейчас я создаю ваш персональный ключ доступа...",
        parse_mode="Markdown"
    )
    # ЗДЕСЬ БУДЕТ ЗАПРОС К 3X-UI СЕРВЕРУ ДЛЯ СОЗДАНИЯ КЛЮЧА
    print(f"Пользователь {message.from_user.id} оплатил тариф на {days} дней.")

# --- ВСПОМОГАТЕЛЬНЫЕ КНОПКИ ---
@dp.callback_query(F.data == "back_to_start")
async def back_to_start(callback: types.CallbackQuery):
    await cmd_start(callback.message)
    await callback.answer()

@dp.callback_query(F.data == "profile")
async def show_profile(callback: types.CallbackQuery):
    await callback.message.answer(
        f"👤 **Ваш профиль VnykLine**\n"
        f"ID: `{callback.from_user.id}`\n"
        "Статус: 🔴 Не активен\n\n"
        "Купите подписку, чтобы получить ключ.",
        parse_mode="Markdown"
    )
    await callback.answer()

# --- ЗАПУСК БОТА ---
async def main():
    print("--- VnykLine Бот запущен и готов к работе! ---")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")