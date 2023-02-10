from linebot.models import ImageSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('抽黃皓')
def get(message_request: MessageRequest):

    msg = ImageSendMessage(
        #點開後的圖片
        original_content_url='https://i.imgur.com/nlxEVPp.jpg',
        #預覽圖
        preview_image_url='https://i.imgur.com/nlxEVPp.jpg')

    return [
        msg
    ]
