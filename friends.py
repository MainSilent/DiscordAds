import os
import json
import requests
import websocket
from time import sleep
from user import User
from multiprocessing import Process
from database import DataBase

token = os.getenv("Token")

def start_friend_requests():
    # Send friend requests
    for user in DataBase.GetFromDB():
        if not int(user[3]):
            DataBase.SendUpdate(user[2], 1)
            if send_request(user[2])
                print(f"Sending Friend Request to {user[1]} "+"\033[32m"+"Success"+"\033[0m")
            else:
                print(f"Sending Friend Request to {user[1]} "+"\033[31m"+"Failed"+"\033[0m")

    # Listen for channel creation events
    ws = websocket.WebSocketApp('wss://gateway.discord.gg/?encoding=json&v=8',
                                on_open=on_open, on_message=on_message)
    ws.run_forever()

def send_request(user_id):
    url = f"https://discord.com/api/v9/users/@me/relationships/{user_id}"
    payload = json.dumps({})
    headers = {
        'Cookie': '__cfduid=db07e6c454c1cb90e3b903a6500527f391617469496',
        'authorization': token,
        'Content-Type': 'application/json',
        'x-super-properties': 'eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS45MCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiODkuMC40Mzg5LjkwIiwib3NfdmVyc2lvbiI6IiIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzY29yZC5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODEzMjksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    if response.status_code == 204:
        DataBase.SendUpdate(user_id, 2)
        return True
    else:
        return False

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
            DataBase.SendUpdate(user_id, 2)
            print(f"Sending Message to {username} "+"\033[32m"+"Success"+"\033[0m")
        else:
            print(f"Sending Message to {username} "+"\033[31m"+"Failed"+"\033[0m")