import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "4165961")
API_HASH = os.environ.get("API_HASH", "38ba6396e513b86e9ed7ea534023a9cc")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5809804854:AAHg_4gKzxC4h7yoFbbpe6wfeEkuz_CcvPE")
TO_CHANNEL_ID = os.environ.get("TO_CHANNEL_ID", "-1001843660143")
FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "-1001225782985")
