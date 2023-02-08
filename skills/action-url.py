from linebot.models import TextSendMessage
from linebot.models.temlate import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message request import MessageRequest
from skills import add_skill


@add_skill('規範')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='Actions',
        template=ButtonsTemplate(
            title='111數位共好規範',
            text='點擊查看',
            actions=[
                URIAction(
                    label='111規範',
                    uri='https://www.moeasmea.gov.tw/files/7853/926E142A-7BF5-40DD-9080-534B8B8690CE'
                )
            ]
        )
    )

    return [
        msg
    ]
