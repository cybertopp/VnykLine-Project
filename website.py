from flask import Flask
import os

app = Flask(__name__)

# --- НАСТРОЙКИ ---
MY_EMAIL = "reklamavkvideo@gmail.com"        # Твоя почта
BOT_LINK = "https://t.me/vnykpn_bot"    # Ссылка на твоего бота

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
            body {{ font-family: -apple-system, sans-serif; background-color: #ffffff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; color: #000; }}
            .container {{ text-align: center; padding: 20px; max-width: 400px; }}
            h1 {{ font-size: 2.5rem; letter-spacing: -1px; margin-bottom: 10px; }}
            p {{ font-size: 1.1rem; color: #666; margin-bottom: 40px; line-height: 1.4; }}
            .btn {{ background: #000; color: #fff; padding: 15px 30px; text-decoration: none; border-radius: 50px; font-weight: bold; display: inline-block; transition: 0.2s; }}
            .btn:hover {{ transform: scale(1.05); }}
            .contact {{ margin-top: 50px; font-size: 0.9rem; color: #aaa; }}
            .contact a {{ color: #aaa; text-decoration: none; border-bottom: 1px solid #eee; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>VnykLine</h1>
            <p>Удаленная настройка сетевого ПО и техническое сопровождение протоколов связи.</p>
            <a href="{BOT_LINK}" class="btn">Запустить помощника</a>
            <div class="contact">
                Support: <a href="mailto:{MY_EMAIL}">{MY_EMAIL}</a>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)