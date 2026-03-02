from flask import Flask
import os

app = Flask(__name__)

# --- ТВОИ ДАННЫЕ (ЗАПОЛНИ) ---
MY_EMAIL = "reklamavkvideo@gmail.com"  # Твоя почта
BOT_URL = "https://t.me/vnykpn_bot"

@app.route('/')
def index():
    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VnykLine IT-Support</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #ffffff; color: #333; margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
            .card {{ text-align: center; padding: 2rem; max-width: 400px; }}
            h1 {{ font-size: 2rem; margin-bottom: 1rem; color: #000; }}
            p {{ color: #666; line-height: 1.5; margin-bottom: 2rem; }}
            .btn {{ background: #000; color: #fff; padding: 12px 24px; text-decoration: none; border-radius: 8px; font-weight: 600; display: inline-block; transition: 0.3s; }}
            .btn:hover {{ opacity: 0.8; }}
            footer {{ position: absolute; bottom: 20px; font-size: 0.8rem; color: #999; text-align: center; width: 100%; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>VnykLine</h1>
            <p>Услуги по технической поддержке и настройке сетевого программного обеспечения.</p>
            <a href="{BOT_URL}" class="btn">Заказать в Telegram</a>
        </div>
        <footer>
            <p>Самозанятый: {MY_FULL_NAME}<br>
            ИНН: {MY_INN} | Email: {MY_EMAIL}</p>
            <p>&copy; 2026 VnykLine</p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)