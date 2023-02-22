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
            text='此為計劃常見Q&A，若還有其他問題歡迎與我們聯絡。',
            actions=[
                URIAction(
                    label='查看計畫常見Q&A',
                    uri='https://liff.line.me/1657887101-1DxD04M9'
                )
            ]
        )
    )

    return [
        msg
    ]
