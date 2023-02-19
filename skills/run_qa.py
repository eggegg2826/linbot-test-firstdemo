from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('計畫常見Q&A')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='計畫常見Q&A',
        template=ButtonsTemplate(
            title='計畫常見Q&A',
            text='列出幾項關於數位共好計畫常見的問題，若還有疑問，請於服務時間來電。',
            actions=[
                URIAction(
                    label='前往Q&A',
                    uri='https://liff.line.me/1657887101-1DxD04M9'
                )
            ]
        )
    )
    
    return [
        msg
    ]
