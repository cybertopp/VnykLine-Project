import asyncio, sqlite3
from aiogram import Router, F, types
from yookassa import Configuration, Payment
from config import SHOP_ID, SHOP_API_KEY, DB_NAME

router = Router()
Configuration.configure(SHOP_ID, SHOP_API_KEY)

async def add_points(user_id, amount):
    pts = 30 if amount >= 250 else 10
    conn = sqlite3.connect(DB_NAME)
    conn.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (pts, user_id))
    conn.commit()
    conn.close()
    return pts

@router.callback_query(F.data.startswith("pay_"))
async def create_payment_handler(cb: types.CallbackQuery):
    amount = int(cb.data.split("_")[1])
    payment = Payment.create({
        "amount": {"value": str(amount), "currency": "RUB"},
        "confirmation": {"type": "redirect", "return_url": "https://t.me/vnykpn_bot"},
        "capture": True, "description": f"Донат от {cb.from_user.id}"
    })
    kb_pay = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="💳 Оплатить", url=payment.confirmation.confirmation_url)],
        [types.InlineKeyboardButton(text="« Назад", callback_data="buy_key")]
    ])
    await cb.message.edit_text(f"💎 Сумма: {amount}₽\nПосле оплаты вам придет уведомление.", reply_markup=kb_pay)
    asyncio.create_task(check_status(payment.id, cb.message, amount))

async def check_status(pid, msg, amount):
    for _ in range(40):
        await asyncio.sleep(15)
        try:
            p = Payment.find_one(pid)
            if p.status == "succeeded":
                pts = await add_points(msg.chat.id, amount)
                await msg.answer(f"✅ Оплата принята! +⭐️ {pts} очков в ваш профиль.")
                return
        except: continue