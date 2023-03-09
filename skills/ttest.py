from fastapi import FastAPI
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage, MessageEvent

app = FastAPI()

# 填入你的 Line 聊天機器人的「Channel access token」和「Channel secret」
line_bot_api = LineBotApi('Ud1bbcb5370338c023c727890cc71a7db')
handler = WebhookHandler('e50f65ab5cc4b8e2e07657372576abb0')

# 當有人加入聊天室時，自動發送公告訊息
@app.post("/webhook")
async def webhook_handler(request):
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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 當有人加入聊天室時，event.source.type 為 "group" 或 "room"
    if event.source.type == "group" or event.source.type == "room":
        # 發送公告訊息
        line_bot_api.push_message(
            event.source.group_id if event.source.type == "group" else event.source.room_id,
            TextSendMessage(text="歡迎加入聊天室，這是公告訊息。")
        )
