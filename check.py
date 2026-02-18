import requests
from datetime import datetime
import os

LINE_TOKEN = os.getenv("LINE_TOKEN")
USER_ID = os.getenv("USER_ID")

def send_line(message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_TOKEN}"
    }
    data = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": message}]
    }
    requests.post(url, headers=headers, json=data)

def check_availability():
    # 仮チェック（あとで実際のログイン処理を追加）
    today = datetime.now().strftime("%Y-%m-%d")
    return f"{today} チェック完了（テスト）"

if __name__ == "__main__":
    result = check_availability()
    send_line(result)
