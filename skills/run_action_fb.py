from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('頭家愛行銷')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='計畫FB粉絲團-頭家愛行銷',
        template=ButtonsTemplate(
            title='計畫FB粉絲團-頭家愛行銷',
            text='趕快按讚追蹤計畫FB粉絲團~取得最新計畫資訊',
            actions=[
                URIAction(
                    label='按讚追蹤FB',
                    uri='https://www.facebook.com/UneedIcare/?ref=page_internal&locale=zh_TW'
                )
            ]
        )
    )
    
    return [
        msg
    ]
