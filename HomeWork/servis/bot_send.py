import requests
from datetime import datetime


def send_msg(**kwargs):
    token = "7999997096:AAH1F5Bw0KSXvOhPq5Lbun9i4ZUojlyboVg"  # bot token

    user_id = "6047378434"  # user id
    url_req = (
        f"https://api.telegram.org/bot{token}/sendMessage"
        f"?chat_id={user_id}"
        f"&text={datetime.now().strftime(f'<b>%d/%m/%y  %H:%M:%S {kwargs}</b>')}"
        f"&parse_mode=HTML"
    )
    response = requests.get(url_req)
    print(response.json())