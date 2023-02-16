from linebot.models import TemplateSendMessage,TextSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('查查看 ')
def get(message_request: MessageRequest):
    msg = message_request.message.split()
    mg_st = msg[1]

    #規範
    rule = TemplateSendMessage(
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

    #案例分享會報名
    share = TemplateSendMessage(
        alt_text='案例分享會報名',
        template=ButtonsTemplate(
            title='案例分享會報名',
            text='台中場-2/15(三)下午兩點\n高雄場-2/16(四)下午兩點\n台北場-2/21(二)下午兩點',
            actions=[
                URIAction(
                    label='點擊報名',
                    uri='https://forms.gle/jKriGfsCVJ7pdpW47?openExternalBrowser=1'
                )
            ]
        )
    )

    #IF規則
    if "規範" in mg_st:
        return[rule]
    elif "報名" or "分享會" or "說明會" in mg_st:
        return[share]
    else:
        return[TextSendMessage(text="錯誤")]
