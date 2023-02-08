from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('規範')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='Actions',
        template=ButtonsTemplate(
            title='數位共好規範',
            text='目前112年數位共好規範尚未公佈，詳細規範請以112年數位共好規範為主。',
            actions=[
                URIAction(
                    label='點擊查看規範',
                    uri='https://www.moeasmea.gov.tw/files/7853/926E142A-7BF5-40DD-9080-534B8B8690CE?openExternalBrowser=1'
                )
            ]
        )
    )

    return [
        msg
    ]
