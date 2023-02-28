from linebot.models import TemplateSendMessage
from linebot.models.template import ConfirmTemplate
from linebot.models.actions import MessageAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('測試')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='Are you sure?',
            actions=[
                 MessageAction(
                     label='a',
                     text='message text'
                 ),
                MessageAction(
                     label='b',
                     text='message text'
                 )
            ]
        )
    )

    return [
        msg
    ]
