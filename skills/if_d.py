from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('查詢 ')
def get(message_request: MessageRequest):
    qwe = {message_request.message}
    if "規範" in qwe:
        return[TextSendMessage(text="成功")]
    else:
        return[TextSendMessage(text="失敗")]
