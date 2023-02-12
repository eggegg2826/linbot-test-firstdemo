from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('{message_request.message}')
def get(message_request: MessageRequest):
    if "查詢" in TextSendMessage("{message_request.message}"):
        return ["你好"]
    else:
        return ["錯誤"]
