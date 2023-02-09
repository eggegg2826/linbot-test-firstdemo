from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('報名')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
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

    return [
        msg
    ]
