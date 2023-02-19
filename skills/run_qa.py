from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('計畫常見Q&A')
def get(message_request: MessageRequest):
    msg = TextSendMessage('此功能建置中...\n若有相關問題，歡迎E-mail來信:cisaims@cisanet.org.tw')
    return [
        msg
    ]
