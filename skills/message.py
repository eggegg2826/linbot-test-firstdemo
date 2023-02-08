msg = TextSendMessage(text='Hello')
return [msg]
```

# 回傳LINE emoji

```python

txt = '$ LINE emoji $'
emoji = [
    {
        "index": 0,
        "productId": "5ac1bfd5040ab15980c9b435",
        "emojiId": "001"
    },
    {
        "index": 13,
        "productId": "5ac1bfd5040ab15980c9b435",
        "emojiId": "002"
    }
]
# print(txt.find('$',2))

emoji_message = TextSendMessage(text='$ LINE emoji $', emojis=emoji)
