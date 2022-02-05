import requests, json
userId = input("유저 아이디> ")

token = 'KoreanBotList Token' # str
bot_ID = BOT_ID # int


headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}

url = f'url = 'https://koreanbots.dev/api/v2/bots/{bot_ID}/vote?userID={userID}'

response = requests.get(url, headers=headers)
data = response.json()
print(response)
print(data)

import time

tm = time.localtime(1643433733.950)
string = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)

print(string)
