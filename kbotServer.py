import requests, json
server = input("서버 카운트> ")
shards = input("봇 샤드> ")

token = 'KoreanBotList Token' # str
bot_ID = BOT_ID # int


headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}
body = {
    "servers": int(server),
    "shards": int(shards),
}
url = f'https://koreanbots.dev/api/v2/bots/{bot_id}/stats'

response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))

print(response)

