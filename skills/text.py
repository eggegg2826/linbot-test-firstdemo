from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{not_match}')
def get(message_request: MessageRequest):
    msg = TextSendMessage(text="查詢")
    msg1 = TextSendMessage(text="查詢2")
    if msg == "查詢":
        return[msg]
    else:
        return[msg1]
