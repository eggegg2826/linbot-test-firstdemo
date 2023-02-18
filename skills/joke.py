from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('我想請問')
def get(message_request: MessageRequest):
    msg = TextSendMessage('不給問')
    return [
        msg
    ]
