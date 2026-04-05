import requests, uuid, json
from config import PANEL_URL, PANEL_LOGIN, PANEL_PASSWORD, ENABLED_INBOUNDS, INBOUND_3

def get_session():
    session = requests.Session()
    login_url = f"{PANEL_URL.rstrip('/')}/login"
    try:
        res = session.post(login_url, data={"username": PANEL_LOGIN, "password": PANEL_PASSWORD}, timeout=10)
        if res.status_code == 200: return session
    except: return None

def add_user_to_server(user_id):
    session = get_session()
    if not session: return None
    uid_str = str(user_id)
    found_uuid = None

    for ib_id in ENABLED_INBOUNDS:
        try:
            res = session.get(f"{PANEL_URL.rstrip('/')}/panel/api/inbounds/get/{ib_id}")
            clients = json.loads(res.json()['obj']['settings']).get('clients', [])
            for c in clients:
                if uid_str in c.get('email', ''):
                    found_uuid = c.get('id')
                    break
        except: continue

    client_uuid = found_uuid if found_uuid else str(uuid.uuid4())
    remark = f"Vnyk_{user_id}"

    if not found_uuid:
        for ib_id in ENABLED_INBOUNDS:
            url = f"{PANEL_URL.rstrip('/')}/panel/api/inbounds/addClient"
            payload = {"id": int(ib_id), "settings": json.dumps({"clients": [{"id": client_uuid, "email": remark if ib_id == 1 else f"{remark}_sw", "enable": True, "tgId": uid_str, "limitIp": 2}]})}
            session.post(url, json=payload)

    c = INBOUND_3
    return f"vless://{client_uuid}@{c['ip']}:{c['port']}?security=reality&sni={c['sni']}&fp={c['fp']}&pbk={c['pbk']}&sid={c['sid']}&type=grpc&serviceName=grpc#{remark}"