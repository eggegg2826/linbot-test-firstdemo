from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill
import random


@add_skill('抽黃皓的朋友')
def get(message_request: MessageRequest):

    # /吃什麼 烤雞.炸雞.鹹酥雞

    # 處理字串
    foods_str = message_request.message.replace("黃皓的朋友 ", "")
    foods = foods_str.split('.')
    print(foods)

    # 隨機挑選一個項目
    result = random.choice(foods)
    print(result)

    # 處理回傳訊息
    meg = TextSendMessage(result)

    return [
        meg
    ]
