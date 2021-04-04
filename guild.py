import os
import json
import websocket
from database import DataBase, G_DataBase
from dotenv import load_dotenv; load_dotenv()
from database import G_DataBase

token = os.getenv("token")

def guild():
	G_DataBase.truncate()

	ws = websocket.WebSocketApp('wss://gateway.discord.gg/?encoding=json&v=8',
                                    on_open=on_open, on_message=on_message)
	ws.run_forever()

def on_open(ws):
    print("WebSocket connection established")
    Auth = {
        "op": 2,
        "d": {
            "token": token,
            "properties": {}
        }
    }
    ws.send(json.dumps(Auth))

def on_message(ws, message):
	data = json.loads(message)

	if data['op'] == 0 and data['t'] == 'READY':
		for guild in data['d']['guilds']:
			print('\n'+guild['name'])
			channel_id = int(input("Channel: "))
			if not channel_id:
				continue
			newGuild = G_DataBase(guild['id'], channel_id)
			newGuild.GoToDB()
			print("Guild added")
		exit()