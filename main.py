import os
import requests
from datetime import datetime

# 環境変数から取得（ここが重要）
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def get_news():
    # 仮：今は固定メッセージ（あとでAPI接続に戻します）
    return "本日のAIニュースを要約しました。"

def send_to_discord(message):
    payload = {"content": message}
    r = requests.post(DISCORD_WEBHOOK, json=payload)
    return r.status_code

def main():
    today = datetime.now().strftime("%Y-%m-%d")
    news = get_news()
    msg = f"🧠 **{today}のニュース要約**\n{news}"
    status = send_to_discord(msg)
    print("Discord送信ステータス:", status)

if __name__ == "__main__":
    main()
