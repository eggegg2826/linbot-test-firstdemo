from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('成為軟協會員')
def get(message_request: MessageRequest):
    msg = TextSendMessage('此功能建置中.../n歡迎E-mail來信本協會:cisaims@cisanet.org.tw')
    return [
        msg
    ]
