from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('{message_request.message}')
def get(message_request: MessageRequest):
    msg = TextSendMessage("查詢")
    msg1 = TextSendMessage("無此資料")
    if msg in message_request.message
        return [msg]
    else
        return [msg1]
