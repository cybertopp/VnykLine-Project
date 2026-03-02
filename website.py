from flask import Flask
import os

app = Flask(__name__)

# Данные для связи
MY_EMAIL = "reklamavkvideo@gmail.com"
BOT_LINK = "https://t.me/vnykpn_bot"

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
            body {{ 
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; 
                background-color: #f8f9fa; 
                display: flex; 
                justify-content: center; 
                align-items: center; 
                height: 100vh; 
                margin: 0; 
                color: #212529; 
            }}
            .card {{ 
                text-align: center; 
                background: #ffffff; 
                padding: 50px 30px; 
                border-radius: 20px; 
                box-shadow: 0 10px 30px rgba(0,0,0,0.05); 
                max-width: 450px; 
                width: 90%;
            }}
            h1 {{ font-size: 2rem; margin-bottom: 15px; font-weight: 700; }}
            p {{ font-size: 1.1rem; color: #6c757d; margin-bottom: 35px; line-height: 1.5; }}
            .btn {{ 
                background: #000000; 
                color: #ffffff; 
                padding: 16px 32px; 
                text-decoration: none; 
                border-radius: 12px; 
                font-weight: 600; 
                display: inline-block; 
                transition: transform 0.2s, background 0.2s; 
            }}
            .btn:hover {{ background: #222; transform: translateY(-2px); }}
            .contact {{ margin-top: 40px; font-size: 0.9rem; color: #adb5bd; border-top: 1px solid #eee; padding-top: 25px; }}
            .contact a {{ color: #007bff; text-decoration: none; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>VnykLine</h1>
            <p>Техническая поддержка, настройка сетевого оборудования и сопровождение ПО.</p>
            <a href="{BOT_LINK}" class="btn">Связаться в Telegram</a>
            <div class="contact">
                Электронная почта для связи:<br>
                <a href="mailto:{MY_EMAIL}">{MY_EMAIL}</a>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Render требует, чтобы приложение слушало порт из переменной окружения PORT
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' обязателен для работы внутри контейнера
    app.run(host='0.0.0.0', port=port)