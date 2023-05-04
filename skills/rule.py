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
            text='112年推動企業數位共好計畫入選名單目前已於軟協官網公告',
            actions=[
                URIAction(
                    label='112年數位共好規範',
                    uri='https://www.moeasmea.gov.tw/files/10106/562676DF-30D2-4818-9375-3D594A67D85E'
                ),
                URIAction(
                    label='前往軟協官網查看入選公告',
                    uri='https://www.cisanet.org.tw/News/Detail/5664'
                ), 
                URIAction(
                    label='計畫常見Q&A',
                    uri='https://liff.line.me/1657887101-1DxD04M9'
                ), 
                URIAction(
                    label='查詢受輔導業者是否符合資格',
                    uri='https://www.tcloud.gov.tw/sme-application'
                )
            ]
        )
    )

    #小微卡
    share = TemplateSendMessage(
        alt_text='小微卡/前測問卷',
        template=ButtonsTemplate(
            title='小微卡/前測問卷',
            text='1.小微卡/前測問卷需於MOU簽回兩禮拜內填寫\n2.小微卡/前測網址需確認為共好所提供之網址',
            actions=[
                URIAction(
                    label='小微卡',
                    uri='小微卡：https://cisatw365.pse.is/45jewh'
                ),
                URIAction(
                    label='前測問卷',
                    uri='https://cisatw365.pse.is/4t979d'
                )
            ]
        )
    )

    #計畫FB粉絲專頁
    ow = TemplateSendMessage(
        alt_text='計畫FB粉絲專頁',
        template=ButtonsTemplate(
            title='數位共好計畫FB粉絲專頁',
            text='按讚追蹤FB粉絲團-頭家愛行銷，取得最新計畫公告及資訊',
            actions=[
                URIAction(
                    label='按讚追蹤FB粉絲團',
                    uri='https://www.facebook.com/UneedIcare/?ref=page_internal&locale=zh_TW'
                )
            ]
        )
    )
    
    #IF規則
    if ("規範" in mg_st) or ("計畫" in mg_st) or ("問題" in mg_st) or ("資訊" in mg_st):
        return[rule]
    elif ("小微卡" in mg_st) or ("問卷" in mg_st):
        return[share]
    elif ("官網" in mg_st) or ("fb" in mg_st) or ("FB" in mg_st):
        return[ow]
    else:
        return[TextSendMessage(text="抱歉我不懂您的意思，目前MENU功能如下:\n1.輸入『查詢 共好計畫』查看最新規範與線上提案繳件\n2.輸入『查詢 fb粉絲團』查看計畫FB與官網")]
