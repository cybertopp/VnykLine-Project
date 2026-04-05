import requests
import json
import base64
from config import *

def get_session(url, login, password):
    session = requests.Session()
    try:
        res = session.post(f"{url.rstrip('/')}/login", data={"username": login, "password": password}, timeout=7)
        if res.status_code == 200: return session
    except: return None

def upload_to_github(filename, content):
    # Функция для авто-загрузки конфига на твой Гитхаб
    url = f"https://api.github.com/repos/{GH_REPO}/contents/users/{filename}.json"
    headers = {"Authorization": f"token {GH_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    
    # Проверяем, есть ли уже такой файл (чтобы получить sha)
    res = requests.get(url, headers=headers)
    sha = res.json().get('sha') if res.status_code == 200 else None

    payload = {
        "message": f"Update config for {filename}",
        "content": base64.b64encode(content.encode()).decode(),
    }
    if sha: payload["sha"] = sha
    
    requests.put(url, headers=headers, json=payload)
    return f"https://raw.githubusercontent.com/{GH_REPO}/main/users/{filename}.json"

def get_or_create_user_link(user_id):
    uid_str = f"Vnyk_{user_id}"
    
    # 1. Регаем в панелях
    for p_url, p_log, p_pass, inbounds in [(PANEL_URL, PANEL_LOGIN, PANEL_PASSWORD, ENABLED_INBOUNDS), 
                                          (PANEL_MS_URL, PANEL_MS_LOGIN, PANEL_MS_PASS, [1])]:
        s = get_session(p_url, p_log, p_pass)
        if s:
            for ib in inbounds:
                payload = {"id": ib, "settings": json.dumps({"clients": [{"id": SHARED_UUID, "email": uid_str, "enable": True}]})}
                s.post(f"{p_url.rstrip('/')}/panel/api/inbounds/addClient", json=payload)

    # 2. Формируем текст файла (все сервера в кучу)
    config_content = (
        f"vless://{SHARED_UUID}@167.17.181.252:39656?security=reality&sni=aws.amazon.com&fp=chrome&pbk=8PBErDe6pigy1AKACc9iY1o_bFM1pLatn6XMQ0M6B3I&sid=36#SW_Main\n"
        f"vless://{SHARED_UUID}@167.17.181.252:443?security=reality&sni=max.ru&fp=random&pbk=0xExv6ZJJgyUfQ7Az8Uu_RsizPPqK6hp1jD1wgugzS4&sid=59&type=grpc#SW_LTE\n"
        f"vless://{SHARED_UUID}@46.29.167.16:443?security=reality&sni=ya.ru&fp=chrome&pbk=0xExv6ZJJgyUfQ7Az8Uu_RsizPPqK6hp1jD1wgugzS4&sid=59#RUS_Moscow"
    )

    # 3. Заливаем на GitHub и получаем ПЕРСОНАЛЬНУЮ ссылку
    final_link = upload_to_github(uid_str, config_content)

    return (
        f"🎯 **Твоя персональная подписка**\n\n"
        f"Ссылка (GitHub):\n`{final_link}`\n\n"
        f"🚀 *Внутри: Швейцария (2 узла) и Москва.*"
    )