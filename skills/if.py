from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{not_match}')
def get(message_request: MessageRequest):
    qwe = {message_request.message}
    if "凱哥" in qwe:
        return[TextSendMessage(text="凱哥在")]
    else:
        return[TextSendMessage(text=" ")]
