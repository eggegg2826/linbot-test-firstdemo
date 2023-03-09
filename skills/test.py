from linebot.models import TemplateSendMessage
from linebot.models.template import CarouselTemplate, CarouselColumn
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
                    thumbnail_image_url='https://via.placeholder.com/300x300/333.png/fff',
                    title='this is menu1',
                    text='description1',
                    actions=[
                        MessageAction(
                            label='message1',
                            text='message text1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://via.placeholder.com/300x300/333.png/fff',
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
