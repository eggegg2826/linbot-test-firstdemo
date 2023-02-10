from linebot.models import ImageSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('抽黃皓')
def get(message_request: MessageRequest):

    msg = ImageSendMessage(
        #點開後的圖片
        original_content_url='https://via.placeholder.com/1024x768/333.png/fff',
        #預覽圖
        preview_image_url='https://via.placeholder.com/800x600/333.png/fff')

    return [
        msg
    ]
