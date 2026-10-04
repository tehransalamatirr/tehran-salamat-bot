import os
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL = "@tehransalamatir"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(
        url,
        data={
            "chat_id": CHANNEL,
            "text": text
        },
        timeout=30
    )
    response.raise_for_status()

if __name__ == "__main__":
    send_message("پیام آزمایشی ربات جهان سلامت ✅")
