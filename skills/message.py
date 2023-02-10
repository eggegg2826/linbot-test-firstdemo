from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill
import random


@add_skill('抽水果')
def get(message_request: MessageRequest):

    # 處理字串
    foods = ("香蕉","葡萄","芒果")
    print(foods)

    # 隨機挑選一個項目
    result = random.choice(foods)
    print(result)

    # 處理回傳訊息
    meg = TextSendMessage(result)

    return [
        meg
    ]
