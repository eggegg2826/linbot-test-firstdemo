from linebot.models import TextSendMessage, TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('查詢 ')
def get(message_request: MessageRequest):
    msg = message_request.message.split()
    mg_st = msg[1]

    #規範
    rule = TemplateSendMessage(
        alt_text='112年數位共好規範',
        template=ButtonsTemplate(
            title='112年數位共好規範',
            text='112年推動企業數位共好計畫即日起開放提案\n◆提案截止時間：112/03/16(四)17:00截止',
            actions=[
                URIAction(
                    label='點擊查看規範',
                    uri='https://www.moeasmea.gov.tw/files/10106/562676DF-30D2-4818-9375-3D594A67D85E'
                )
            ]
        )
    )

    #案例分享會報名
    share = TemplateSendMessage(
        alt_text='112年推動企業數位共好計畫提案說明會',
        template=ButtonsTemplate(
            title='112年推動企業數位共好計畫提案說明會',
            text='台中場-2/15(三)下午兩點\n高雄場-2/16(四)下午兩點\n台北場-2/21(二)下午兩點',
            actions=[
                URIAction(
                    label='報名說明會',
                    uri='https://forms.gle/jKriGfsCVJ7pdpW47?openExternalBrowser=1'
                )
            ]
        )
    )

    #IF規則
    if "規範" in mg_st:
        return[share]
    elif "報名" in mg_st:
        return[rule]
    else:
        return[TextSendMessage(text="錯誤")]
