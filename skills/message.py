from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('黃皓')
def get(message_request: MessageRequest):
    msg = TextSendMessage('帥哥')
    return [
        msg
    ]
