import requests

from envparse import Env

env = Env()
TOKEN = env.str("TOKEN")
ADMIN_CHAT_ID = env.str("ADMIN_CHAT_ID")

requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ADMIN_CHAT_ID}&text=завожу бота")
