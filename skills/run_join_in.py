from linebot.models import TemplateSendMessage
from linebot.models.template import ButtonsTemplate
from linebot.models.actions import URIAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('成為軟協會員')
def get(message_request: MessageRequest):

    buttons_template_message = TemplateSendMessage(
    alt_text='成為軟協會員',
    template=ButtonsTemplate(
            thumbnail_image_url='https://upload.cc/i1/2023/02/22/MupB5T.png',
            title='竭誠歡迎您成為軟協會員',
            text='請填寫表單，收到您填寫的表單後，我們將會盡快與您聯絡。',
            actions=[
                    URIAction(
                            label='加入成為軟協會員',
                            uri='https://forms.gle/5341yP5YqHsorWcC7'
                    )
            ]
    )
    )
    return [
        buttons_template_message
    ]
