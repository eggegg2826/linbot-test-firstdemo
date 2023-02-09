from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('報名')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='Actions',
        template=ButtonsTemplate(
            title='案例分享會報名',
            text='台中場-活動時間：2/15(三)14：00
                  高雄場-活動時間：2/16(四)14：00
                  台北場-活動時間：2/21(二)14：00',
            actions=[
                URIAction(
                    label='點擊報名',
                    uri='https://forms.gle/jKriGfsCVJ7pdpW47?openExternalBrowser=1'
                )
            ]
        )
    )

    return [
        msg
    ]
