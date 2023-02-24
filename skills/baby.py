from linebot.models import ImageSendMessage
from models.message_request import MessageRequest
from skills import add_skill
import random


@add_skill('抽寶寶')
def get(message_request: MessageRequest):

    p1 = ImageSendMessage(original_content_url='https://i.imgur.com/pEjApKJ.jpg',
    preview_image_url='https://i.imgur.com/pEjApKJ.jpg')
    p2 = ImageSendMessage(original_content_url='https://i.imgur.com/4ODlvyI.jpg',
    preview_image_url='https://i.imgur.com/4ODlvyI.jpg')
    p3 = ImageSendMessage(original_content_url='https://i.imgur.com/85quJ4t.jpg',
    preview_image_url='https://i.imgur.com/85quJ4t.jpg')
    p4 = ImageSendMessage(original_content_url='https://i.imgur.com/K87b26Q.jpg',
    preview_image_url='https://i.imgur.com/K87b26Q.jpg')
    
    list1 = (p1,p2,p3,p4)
    image = random.choice([0,1,2,3])

    return [
        list1[image]
    ]
