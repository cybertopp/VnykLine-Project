from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VnykLine - Официальный сайт</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; max-width: 900px; margin: 0 auto; padding: 20px; color: #333; background-color: #f4f7f6; }
            header { background: #2c3e50; color: white; padding: 20px; text-align: center; border-radius: 10px 10px 0 0; }
            .content { background: white; padding: 30px; border-radius: 0 0 10px 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            h1, h2 { color: #2c3e50; border-bottom: 2px solid #eee; padding-bottom: 10px; }
            .tariff { background: #e8f4fd; padding: 15px; border-left: 5px solid #3498db; margin: 10px 0; }
            footer { text-align: center; margin-top: 30px; font-size: 0.9em; color: #777; }
            .contact { color: #3498db; font-weight: bold; }
        </style>
    </head>
    <body>
        <header>
            <h1>VnykLine Service</h1>
        </header>
        <div class="content">
            <h2>О сервисе</h2>
            <p>VnykLine предоставляет услуги защищенного доступа в интернет через протоколы VLESS/Shadowsocks. Мы гарантируем высокую скорость и конфиденциальность ваших данных.</p>
            
            <h2>Наши тарифы</h2>
        <div class="tariff">
            <strong>Недельный драйв:</strong> 40 рублей / 7 дней (Безлимит, 1 устройство)
        </div>
        <div class="tariff">
            <strong>Месячный комфорт:</strong> 80 рублей / 30 дней (Безлимит, 1 устройство) - Экономия 50%!
        </div>

            <h2>Юридическая информация</h2>
            <p><strong>Политика конфиденциальности:</strong> Мы не храним логи ваших посещений. Для работы сервиса используется только ваш Telegram ID.</p>
            <p><strong>Условия возврата:</strong> Возврат средств возможен в течение 24 часов с момента оплаты, если сервис не работает по техническим причинам.</p>
            <p><strong>Безопасность:</strong> Оплата производится через защищенный шлюз Robokassa. Мы не имеем доступа к данным ваших карт.</p>

            <h2>Контакты</h2>
            <p>По всем вопросам: <span class="contact">@vnyyyyk</span> (Telegram)</p>
            <p>Email: reklamavkvideo@gmail.com (или твой личный email)</p>
        </div>
        <footer>
            &copy; 2026 VnykLine. Все права защищены. Индивидуальный предприниматель / Самозанятый.
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)