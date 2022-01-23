import requests
from datetime import datetime

from envparse import Env

env = Env()
TOKEN = env.str("TOKEN", default="2104221180:AAGmwLGyb1m8fTnePreXS5bruo_HaW2Vj_w")
ADMIN_CHAT_ID = env.str("ADMIN_CHAT_ID", default="362857450")

current_datetime = datetime.now()
msg = f"currend date and time: {current_datetime}"

requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ADMIN_CHAT_ID}&text={msg}")
