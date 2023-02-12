from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('')
def get(message_request: MessageRequest):
    msg = TextSendMessage(text="查詢")
    msg1 = TextSendMessage(text="查詢2")
    if "查詢" in TextSendMessage(text=f"{message_request.message}"):
        return[msg]
    else:
        return[msg1]
