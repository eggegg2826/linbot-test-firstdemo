from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('查詢')
def get(message_request: MessageRequest):
    msg = TextSendMessage("目前MENU功能如下:1.輸入『規範』查看最新規範,end='', 2.輸入『報名』報名案例分享會end=''")
    return [
        msg
    ]
