import os
import json
import websocket
from time import sleep
from user import User
from multiprocessing import Process
from database import DataBase

token = os.getenv("Token")

def start_friend_requests():
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
    if data['t'] == "CHANNEL_CREATE":
        d = data['d']
        user_id = d['recipients'][0]['id']
        username = d['recipients'][0]['username']
        channel_id = d['id']

        message = User(user_id)
        if message.send(channel_id):
            DataBase.SendUpdate(user[2], 2)
            print(f"Sending to {username} "+"\033[32m"+"Success"+"\033[0m")
        else:
            print(f"Sending to {username} "+"\033[31m"+"Failed"+"\033[0m")