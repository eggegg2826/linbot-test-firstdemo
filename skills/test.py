from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('查查看 ')
def get(message_request: MessageRequest):
    x = message_request.message.split()
    y = x[1]
    
    if "規範" in y:
        return[TextSendMessage(text="有規範")]
    elif "報名" in y:
        return[TextSendMessage(text="有報名")]
    else:
        return[TextSendMessage(text="錯誤")]
