import os
import json
import websocket
from time import sleep
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