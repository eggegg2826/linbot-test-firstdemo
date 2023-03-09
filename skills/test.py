from linebot.models import TemplateSendMessage
from linebot.models.template import CarouselColumn, CarouselTemplate
from models.message_request import MessageRequest
from linebot.models.actions import MessageAction
from skills import add_skill


@add_skill('測試')
def get(message_request: MessageRequest):

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    
                    title='this is menu1',
                    text='description1',
                    actions=[
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
                        MessageAction(
                            label='message1-1',
                            text='message text1-1'
                        ),
                        MessageAction(
                            label='message1-2',
                            text='message text1-2'
                        )
                    ]
                ),
                CarouselColumn(
                    
                    title='this is menu2',
                    text='description2',
                    actions=[
                        MessageAction(
                            label='message2',
                            text='message text2'
                        ),
                    ]
                )
            ]
        )
    )

    return [
        carousel_template_message
    ]
