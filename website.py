from flask import Flask
import os

app = Flask(__name__)

# --- ДАННЫЕ ДЛЯ МОДЕРАЦИИ (ЗАПОЛНИ СВОИ) ---
MY_FULL_NAME = "Иванов Иван Иванович"  # Твое ФИО
MY_INN = "123456789012"                # Твой ИНН
MY_EMAIL = "support@vnykline.ru"       # Твоя почта
BOT_URL = "https://t.me/ТВОЙ_БОТ"      # Ссылка на твоего бота

@app.route('/')
def index():
    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VnykLine IT-Support | Услуги настройки ПО</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; color: #333; margin: 0; padding: 20px; display: flex; flex-direction: column; min-height: 100vh; align-items: center; }}
            .container {{ background: white; padding: 2.5rem; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.08); max-width: 600px; width: 100%; text-align: center; flex-grow: 1; }}
            h1 {{ color: #2c3e50; margin-bottom: 1rem; border-bottom: 2px solid #3498db; display: inline-block; padding-bottom: 5px; }}
            p {{ line-height: 1.6; color: #7f8c8d; font-size: 1.1rem; }}
            .services {{ margin-top: 2rem; text-align: left; }}
            .service-item {{ background: #fdfdfd; padding: 1.2rem; border-left: 5px solid #3498db; margin-bottom: 1rem; border-radius: 5px; border: 1px solid #eee; }}
            .price {{ font-weight: bold; color: #2ecc71; font-size: 1.2rem; }}
            .btn {{ display: inline-block; background: #3498db; color: white; padding: 1rem 2rem; text-decoration: none; border-radius: 30px; margin-top: 2rem; font-weight: bold; transition: 0.3s; }}
            .btn:hover {{ background: #2980b9; transform: translateY(-2px); }}
            footer {{ margin-top: 3rem; text-align: center; font-size: 0.85rem; color: #95a5a6; border-top: 1px solid #ddd; padding-top: 20px; width: 100%; max-width: 600px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>VnykLine IT-Support</h1>
            <p>Профессиональные услуги по индивидуальной настройке сетевого ПО и конфигурации защищенных протоколов связи (VLESS/Reality).</p>
            
            <div class="services">
                <div class="service-item">
                    <strong>📦 Техническая настройка (Базовая)</strong><br>
                    Удаленная конфигурация и поддержка клиента в течение 7 дней.<br>
                    <span class="price">Стоимость: 40.00 ₽</span>
                </div>
                <div class="service-item">
                    <strong>🚀 Комплексное сопровождение (Max)</strong><br>
                    Полная настройка шлюза и мониторинг соединения на 30 дней.<br>
                    <span class="price">Стоимость: 80.00 ₽</span>
                </div>
            </div>
            
            <p>Все заказы обрабатываются автоматически через нашу систему в Telegram.</p>
            <a href="{BOT_URL}" class="btn">🚀 Перейти к настройке в Telegram</a>
        </div>
        
        <footer>
            <p>&copy; 2026 VnykLine. Все права защищены.</p>
            <p>
                <strong>Самозанятый:</strong> {MY_FULL_NAME}<br>
                <strong>ИНН:</strong> {MY_INN}<br>
                <strong>Email для связи:</strong> {MY_EMAIL}
            </p>
            <p style="font-size: 0.7rem;">Сайт не является публичной офертой. Оплата производится за консультационные и технические услуги.</p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)