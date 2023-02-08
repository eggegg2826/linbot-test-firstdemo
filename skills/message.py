from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('今年的規範')
def get(message_request: MessageRequest):
    msg = TextSendMessage(text='今年的規範還沒出來')
    return [
        msg
    ]
