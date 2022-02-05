import requests, json
botID = int(input("Bot ID: "))
headers = {}
url = 'https://koreanbots.dev/api/v2/bots/932196994775121930'

response = requests.get(url, headers=headers)
data = response.json()
print(data)

