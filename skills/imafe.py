from linebot.models import ImageSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('抽自己')
def get(message_request: MessageRequest):

    msg = p1
    
    p1 = ImageSendMessage(original_content_url='https://via.placeholder.com/1024x768/333.png/fff',preview_image_url='https://via.placeholder.com/800x600/333.png/fff')

    return [
        p1
    ]
