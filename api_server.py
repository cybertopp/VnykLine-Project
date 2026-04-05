import requests
import json
import base64
import logging
# Импортируем все настройки из твоего файла config.py
try:
    from config import *
except ImportError:
    print("Ошибка: Создай файл config.py с настройками PANEL_URL, GH_TOKEN и т.д.")

# 1. Функция для авторизации в панелях 3x-ui
def get_session(url, login, password):
    session = requests.Session()
    try:
        login_url = f"{url.rstrip('/')}/login"
        res = session.post(login_url, data={"username": login, "password": password}, timeout=7)
        if res.status_code == 200:
            return session
    except Exception as e:
        logging.error(f"Ошибка логина в панель {url}: {e}")
    return None

# 2. Функция загрузки текстового конфига на GitHub
def upload_to_github(filename, content):
    # Очистка токена и репозитория от лишних пробелов
    clean_token = GH_TOKEN.strip()
    clean_repo = GH_REPO.strip()

    # Путь к файлу в репозитории (папка users)
    url = f"https://api.github.com/repos/{clean_repo}/contents/users/{filename}.txt"
    headers = {
        "Authorization": f"token {clean_token}", 
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        # Проверяем, существует ли файл, чтобы получить его SHA (нужно для обновления)
        res = requests.get(url, headers=headers, timeout=10)
        sha = res.json().get('sha') if res.status_code == 200 else None

        payload = {
            "message": f"Update config for {filename}",
            "content": base64.b64encode(content.encode('utf-8')).decode('utf-8'),
            "branch": "main" 
        }
        if sha:
            payload["sha"] = sha

        # Отправляем данные на GitHub
        put_res = requests.put(url, headers=headers, json=payload, timeout=10)
        print(f"--- GitHub Upload Status: {put_res.status_code} ---")
        
        if put_res.status_code in [200, 201]:
            # Возвращаем прямую ссылку на скачивание (Raw)
            return f"https://raw.githubusercontent.com/{clean_repo}/main/users/{filename}.txt"
    except Exception as e:
        print(f"Ошибка при работе с GitHub: {e}")
    
    return "ошибка_загрузки"

# 3. Основная функция: регистрация в панелях и создание ссылок
def get_or_create_user_link(user_id):
    uid_str = f"Vnyk_{user_id}"
    
    # Регистрация клиента в обеих панелях (Швейцария и Москва)
    targets = [
        (PANEL_URL, PANEL_LOGIN, PANEL_PASSWORD, ENABLED_INBOUNDS),
        (PANEL_MS_URL, PANEL_MS_LOGIN, PANEL_MS_PASS, [1]) # Предполагаем ID инбаунда в Москве = 1
    ]

    for p_url, p_log, p_pass, inbounds in targets:
        s = get_session(p_url, p_log, p_pass)
        if s:
            for ib in inbounds:
                # Добавляем клиента по SHARED_UUID
                payload = {
                    "id": ib, 
                    "settings": json.dumps({"clients": [{"id": SHARED_UUID, "email": uid_str, "enable": True}]})
                }
                s.post(f"{p_url.rstrip('/')}/panel/api/inbounds/addClient", json=payload)

    # 4. Формируем список VLESS ссылок (Формат для Happ Proxy)
    # Используем данные, которые мы проверили по твоим скриншотам
    links = [
        # МОСКВА (gRPC)
        f"vless://{SHARED_UUID}@46.29.167.16:443?encryption=none&security=reality&sni=max.ru&fp=random&pbk=Pd5Mw-ayiju1HACOCZ7MkGMub_5C-LhhV6XBxZAGhg&sid=1783b7&type=grpc&serviceName=vnyk-grpc#%F0%9F%87%B7%F0%9F%87%BA%20VnykLine%20%7C%20Moscow",
        
        # ШВЕЙЦАРИЯ MAIN (TCP)
        f"vless://{SHARED_UUID}@167.17.181.252:39656?encryption=none&security=reality&sni=aws.amazon.com&fp=chrome&pbk=8PBErDe6pigy1AKACc9iY1o_bFM1pLatn6XMQ0M6B3I&sid=36&type=tcp&headerType=none#%F0%9F%87%A8%F0%9F%87%AD%20VnykLine%20%7C%20Main",
        
        # ШВЕЙЦАРИЯ LTE (gRPC)
        f"vless://{SHARED_UUID}@167.17.181.252:443?encryption=none&security=reality&sni=max.ru&fp=random&pbk=0xExv6ZJJgyUfQ7Az8Uu_RsizPPqK6hp1jD1wgugzS4&sid=59&type=grpc&serviceName=vnyk-grpc#%F0%9F%87%A8%F0%9F%87%AD%20VnykLine%20%7C%20SW%20LTE"
    ]

    # Объединяем ссылки в один текстовый блок
    config_text = "\n".join(links)
    
    # Загружаем файл на GitHub
    final_link = upload_to_github(uid_str, config_text)
    
    return (
        f"🎯 **Твой конфиг VnykLine готов!**\n\n"
        f"Скопируй эту ссылку и добавь в приложение как подписку:\n\n"
        f"`{final_link}`\n\n"
        f"🚩 *В списке появится 3 локации: Москва и 2 Швейцарии.*"
    )