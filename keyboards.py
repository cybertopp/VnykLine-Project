from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Получить ключ", callback_data="get_trial")],
        [InlineKeyboardButton(text="👤 Профиль", callback_data="profile"),
         InlineKeyboardButton(text="🎁 Бонусы", callback_data="referral")],
        [InlineKeyboardButton(text="🏆 ТОП-10", callback_data="top_10")],
        [InlineKeyboardButton(text="💎 Поддержать проект", callback_data="buy_key")],
        [InlineKeyboardButton(text="👨‍💻 Инструкция", callback_data="support"),
         InlineKeyboardButton(text="⚖️ Юр. Инфо", callback_data="legal")]
    ])

def back_to_menu_kb():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="« В главное меню", callback_data="to_main")]])

def donate_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🍕 100₽ (+10 очков)", callback_data="pay_100")],
        [InlineKeyboardButton(text="☕️ 250₽ (+30 очков)", callback_data="pay_250")],
        [InlineKeyboardButton(text="« Назад", callback_data="to_main")]
    ])