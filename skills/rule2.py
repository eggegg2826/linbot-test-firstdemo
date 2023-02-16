from linebot.models import TemplateSendMessage,TextSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('查查看  ')
def get(message_request: MessageRequest):
    wemg = message_request.message.split()
    mg_st = wemg[1]

    msg = TemplateSendMessage(
        alt_text='111數位共好規範',
        template=ButtonsTemplate(
            title='111數位共好規範',
            text='目前112年數位共好規範尚未公佈，詳細規範請以112年數位共好規範為主。',
            actions=[
                URIAction(
                    label='點擊查看規範',
                    uri='https://www.moeasmea.gov.tw/files/7853/926E142A-7BF5-40DD-9080-534B8B8690CE?openExternalBrowser=1'
                )
            ]
        )
    )

    if "規範" in mg_st:
        return[msg]
    else:
        return[TextSendMessage(text="錯誤")]
