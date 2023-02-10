from linebot.models import ImageSendMessage
from models.message_request import MessageRequest
from skills import add_skill
import random

@add_skill('抽水果')
def get(message_request: MessageRequest):

    p1 = ImageSendMessage(original_content_url='https://via.placeholder.com/1024x768/333.png/fff',
    preview_image_url='https://via.placeholder.com/800x600/333.png/fff')
    p2 = ImageSendMessage(original_content_url='https://i.imgur.com/nlxEVPp.jpg',
    preview_image_url='https://i.imgur.com/nlxEVPp.jpg')
        

    return [
        p1,p2
    ]
