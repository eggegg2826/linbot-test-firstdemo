from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('查詢')
def get(message_request: MessageRequest):
    msg = TextSendMessage("目前MENU功能:\n1.輸入『規範』查看最新規範\n2.輸入『報名』查看案例分享會")
    return [
        msg
    ]
