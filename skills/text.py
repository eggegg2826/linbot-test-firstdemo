from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('')
def get(message_request: MessageRequest):
    qwe = {message_request.message}
    if "查詢" in qwe:
        return[TextSendMessage(text="查詢")]
    else:
        return[TextSendMessage(text="錯誤")]
