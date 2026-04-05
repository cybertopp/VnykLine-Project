BOT_TOKEN = "8377215857:AAEO-pqlqrAvSpUAl_9xBu14Bq5bHXsU594"
DB_NAME = "vnykline.db"
ADMIN_ID = 8313482374

# Данные ЮKassa
SHOP_ID = "1289437"
SHOP_API_KEY = "live_LFZm3j4vKRYkgrR7KHncvsiEAFWb04Ve0tTq5ANNQl4"

# Данные панели
PANEL_URL = "http://167.17.181.252:2053/sub"
PANEL_LOGIN = "admin"
PANEL_PASSWORD = "B2DB0Yfu65uDjsIb"

ENABLED_INBOUNDS = [1, 3]

# Настройки для генерации ссылок
# Инбаунд №1 (Обычный Reality)
INBOUND_1 = {
    "ip": "167.17.181.252",
    "port": 39656,
    "sid": "36",
    "pbk": "8PBErDe6pigy1AKACc9iY1o_bFM1pLatn6XMQ0M6B3I",
    "sni": "aws.amazon.com",
    "fp": "chrome"
}

# Инбаунд №3 (gRPC для обхода глушилок)
INBOUND_3 = {
    "ip": "167.17.181.252",
    "port": 443,
    "sid": "59",
    "pbk": "0xExv6ZJJgyUfQ7Az8Uu_RsizPPqK6hp1jD1wgugzS4",
    "sni": "max.ru",
    "fp": "random"
}