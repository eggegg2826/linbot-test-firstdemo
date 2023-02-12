from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{message_request.message}')
def get(message_request: MessageRequest):
    return [
        TextSendMessage(text=f'You said: {message_request.message}')
    ]
