from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('購世代')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='-地方創生好物-購世代',
        template=ButtonsTemplate(
            title='購世代',
            text='「好吃、好玩、好買」購物情報與商品資訊的導購平台，匯集許多地方創生店家，趕快進來看看~',
            actions=[
                URIAction(
                    label='地方創生好物',
                    uri='https://gostyle.org.tw/'
                )
            ]
        )
    )
    
    return [
        msg
    ]
