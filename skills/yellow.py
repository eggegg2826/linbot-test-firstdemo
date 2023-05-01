from linebot.models import ImageSendMessage
from models.message_request import MessageRequest
from skills import add_skill
import random


@add_skill('抽黃皓哦')
def get(message_request: MessageRequest):

    p1 = ImageSendMessage(original_content_url='https://i.imgur.com/CLOf0Vx.jpg',
    preview_image_url='https://i.imgur.com/CLOf0Vx.jpg')
    p2 = ImageSendMessage(original_content_url='https://i.imgur.com/nlxEVPp.jpg',
    preview_image_url='https://i.imgur.com/nlxEVPp.jpg')
    p3 = ImageSendMessage(original_content_url='https://i.imgur.com/d3xLd5R.jpg',
    preview_image_url='https://i.imgur.com/d3xLd5R.jpg')
    p4 = ImageSendMessage(original_content_url='https://i.imgur.com/GZVBe3u.jpg',
    preview_image_url='https://i.imgur.com/GZVBe3u.jpg')
    p5 = ImageSendMessage(original_content_url='https://i.imgur.com/Y3MbyS2.jpg',
    preview_image_url='https://i.imgur.com/Y3MbyS2.jpg')
    p6 = ImageSendMessage(original_content_url='https://i.imgur.com/QIdizT7.jpg',
    preview_image_url='https://i.imgur.com/QIdizT7.jpg')
    
    list1 = (p1,p2,p3,p4,p5,p6)
    image = random.choice([0,1,2,3,4,5])

    return [
        list1[image]
    ]
