import json

with open("dania.json") as f:
  json_data = json.load(f)
  messages = json_data.get('messages')

  print(len(messages))

