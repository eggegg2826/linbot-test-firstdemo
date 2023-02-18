from linebot.models import TemplateSendMessage,TextSendMessage
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
            text='112年推動企業數位共好計畫即日起開放提案。\n◆提案截止時間：112/03/16(四)17:00截止\n※線上提案，請提早至線上提案系統申辦帳號及填寫相關資料，並且於收件截止前進行線上繳件唷！',
            actions=[
                URIAction(
                    label='點擊查看規範',
                    uri='file:///C:/Users/arthur.wu/Downloads/9109cb1b-a72e-4613-9d8a-249cc43fa74b.pdf'
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
        return[rule]
    elif "報名" or "分享會" or "說明會" in mg_st:
        return[share]
    else:
        return[TextSendMessage(text="抱歉，我不曉得您說的問題。若還有疑問，歡迎在服務時間來電本協會。")]
