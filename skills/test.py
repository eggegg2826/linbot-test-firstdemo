from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('測試')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='123',
        template=ButtonsTemplate(
            title='123',
            text='竭誠歡迎您成為軟協會員，若收到您填寫的表單後，我們將盡快與您聯絡。',
            actions=[
                URIAction(
                    label='加入成為軟協會員',
                    uri='https://forms.gle/5341yP5YqHsorWcC7'
                ),
                URIAction(
                    label='了解更多軟協',
                    uri='https://gostyle.org.tw/'
                )
            ]
        )
    )
    
    return [
        msg
    ]
