from linebot.models import ImageSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('抽黃皓')
def get(message_request: MessageRequest):

    msg = ImageSendMessage(
        #點開後的圖片
        original_content_url='https://drive.google.com/file/d/1_7NGhE0ER9cmp4VdIiAfsGrVziqx3DGm/view?usp=share_link',
        #預覽圖
        preview_image_url='https://drive.google.com/file/d/1_7NGhE0ER9cmp4VdIiAfsGrVziqx3DGm/view?usp=share_link')

    return [
        msg
    ]
