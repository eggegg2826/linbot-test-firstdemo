from linebot.models import TextSendMessage, TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('查詢 ')
def get(message_request: MessageRequest):
    msg = message_request.message.split()
    mg_st = msg[1]

    #規範、數位共好計畫
    rule = TemplateSendMessage(
        alt_text='112年數位共好計畫',
        template=ButtonsTemplate(
            title='112年數位共好計畫',
            text='112年推動企業數位共好計畫即日起開放提案\n◆提案截止時間：112/03/16(四)17:00截止',
            actions=[
                URIAction(
                    label='112年數位共好規範',
                    uri='https://www.moeasmea.gov.tw/files/10106/562676DF-30D2-4818-9375-3D594A67D85E'
                ),
                URIAction(
                    label='計畫常見Q&A',
                    uri='https://liff.line.me/1657887101-1DxD04M9'
                ), 
                URIAction(
                    label='前往線上提案繳件',
                    uri='https://www.cisa.tw/365/login/index.php'
                ), 
                URIAction(
                    label='查詢受輔導業者是否符合資格',
                    uri='https://www.tcloud.gov.tw/sme-application'
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

    #計畫官網
    ow = TemplateSendMessage(
        alt_text='計畫FB粉專與官網',
        template=ButtonsTemplate(
            title='數位共好計畫FB粉專與官網',
            text='按讚追蹤FB粉絲團-頭家愛行銷，取得最新計畫公告及資訊',
            actions=[
                URIAction(
                    label='按讚追蹤FB粉絲團',
                    uri='https://www.facebook.com/UneedIcare/?ref=page_internal&locale=zh_TW'
                ),
                URIAction(
                    label='前往計畫官網',
                    uri='https://www.198.org.tw/'
                )
            ]
        )
    )
    
    #IF規則
    if ("規範" in mg_st) or ("計畫" in mg_st) or ("問題" in mg_st) or ("資訊" in mg_st):
        return[rule]
    elif ("A" in mg_st):
        return[share]
    elif ("官網" in mg_st) or ("fb" in mg_st) or ("FB" in mg_st):
        return[ow]
    else:
        return[TextSendMessage(text="抱歉我不懂您的意思，目前MENU功能如下:\n1.輸入『查詢 共好計畫』查看最新規範與線上提案繳件\n2.輸入『查詢 fb粉絲團』查看計畫FB與官網")]
