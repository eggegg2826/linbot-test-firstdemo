from fastapi import FastAPI, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage, MessageEvent, JoinEvent

app = FastAPI()

# 填入你的 Line 聊天機器人的「Channel access token」和「Channel secret」
line_bot_api = LineBotApi('6xPZ/U5hw/nVpjeZVpPBIwleHMuKNJ8bDvxvKrXc6h2Olu/7JVGImOzymMrBEaRAd/W3MdvVIU4D71hEXSucGECdaPr5nMuusL67QpSF2Pz5gkJvAaJeEPOnr05fs1XMm6uFI4AEfVqqiw13rP+lWwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ef6e6cd0b6edff4b54643c4d0e993eb8')

# 當有人加入聊天室時，自動發送公告訊息
@ app.post("/callback")
async def callback(request: Request):
    # 取得 X-Line-Signature HTTP 標頭
    signature = request.headers['X-Line-Signature']

    # 讀取 request body
    body = await request.body()

    try:
        # 處理 webhook event
        handler.handle(body.decode('utf-8'), signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        return "Invalid signature. Please check your channel access token/channel secret."

    return "OK"


@ handler.add(JoinEvent)
def handle_join_event(event):
    print(f"Join event: {event}")
    # 當有人加入聊天室時，event.source.type 為 "group" 或 "room"
    if event.source.type == "group" or event.source.type == "room":
        # 發送公告訊息
        line_bot_api.push_message(
            event.source.group_id if event.source.type == "group" else event.source.room_id,
            TextSendMessage(text="歡迎加入聊天室，這是公告訊息。")
        )
