import os
import json
from dotenv import load_dotenv

if not os.getenv('GITHUB_ACTIONS'):
    load_dotenv(dotenv_path='.ananbot.env', override=True)

config = {}
# 嘗試載入 JSON 並合併參數
try:
    configuration_json = json.loads(os.getenv('CONFIGURATION', '') or '{}')
    if isinstance(configuration_json, dict):
        config.update(configuration_json)
except Exception as e:
    print(f"⚠️ 無法解析 CONFIGURATION：{e}")



BOT_TOKEN = config.get('bot_token', os.getenv('BOT_TOKEN', ''))

MYSQL_HOST = config.get('db_host', os.getenv('MYSQL_DB_HOST', 'localhost'))
MYSQL_USER = config.get('db_user', os.getenv('MYSQL_DB_USER', ''))
MYSQL_PASSWORD = config.get('db_password', os.getenv('MYSQL_DB_PASSWORD', ''))
MYSQL_DB = config.get('db_name', os.getenv('MYSQL_DB_NAME', ''))
MYSQL_DB_PORT = int(config.get('db_port', os.getenv('MYSQL_DB_PORT', 3306)))

DB_CONFIG = {
    "host": MYSQL_HOST,
    "port": MYSQL_DB_PORT,
    "user": MYSQL_USER,
    "password": MYSQL_PASSWORD,
    "db": MYSQL_DB,
    "autocommit": True
}
