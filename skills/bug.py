from linebot.models import FlexSendMessage
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('/匯率')
def get(message_request: MessageRequest):
    # /匯率 美金 1000
    msg_array = message_request.message.split()
    
    convert_currency = msg_array[1]
    twd = msg_array[2]
    
    result = convert(convert_currency, float(twd))
    
    return [TextSendMessage(text=result)]
  
def convert(code: str, twd: float):
  result = 30
  return result
