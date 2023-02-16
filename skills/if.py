from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('查看 ')
def get(message_request: MessageRequest):
    if "規範" in {message_request.message}:
        return[TextSendMessage(text="成功")]
    else:
        return[TextSendMessage(text="失敗")]
