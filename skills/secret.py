from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('數位共好')
def get(message_request: MessageRequest):
    msg = TextSendMessage("企業更好")
    return [
        msg
    ]
