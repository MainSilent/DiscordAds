import os
import json
import websocket
from time import sleep
from database import DataBase, G_DataBase
from dotenv import load_dotenv; load_dotenv()

count = 0
online_count = 0
guild_id = ''
channel_id = ''
token = os.getenv("Token")

def fetch():
    for idx, guild in enumerate(G_DataBase.GetFromDB()):
        global guild_id 
        guild_id  = guild[1]
        global channel_id 
        channel_id = guild[2]

        ws = websocket.WebSocketApp('wss://gateway.discord.gg/?encoding=json&v=8',
                                    on_open=on_open, on_message=on_message)
        ws.run_forever()

        if idx != len(G_DataBase.GetFromDB()) - 1:
            print("Getting ready for the next guild...")
            sleep(4)

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
    global count
    global online_count
    data = json.loads(message)

    if data['op'] == 0 and data['t'] == 'READY':
        print('Login successful')
        getUsers = {
            "op": 14,
            "d": {
                "guild_id": guild_id,
                "channels": { channel_id: [[0,99]] }
            }
        }
        ws.send(json.dumps(getUsers))
    elif data['op'] == 0 and data['t'] == 'GUILD_MEMBER_LIST_UPDATE':
        for op in data['d']['ops']:
            if op['op'] == 'SYNC':
                online_count = int(data['d']['online_count'])
                for item in op['items']:
                    try:
                        user = item['member']['user']
                        id = user['id']
                        if 'bot' not in user.keys() and not DataBase.Status(id):
                            username = user['username']
                            print(f"Adding {username} to database")
                            newUser = DataBase(username, id, 0)
                            newUser.GoToDB()
                    except:
                        pass
                if count*100 <= online_count:
                    count += 1
                    print(f'Next range {count*100} - {(count*100)+99}')
                    getUsers = {
                        "op": 14,
                        "d": {
                            "guild_id": guild_id,
                            "channels": { channel_id: [[0,99], [count*100,(count*100)+99]] }
                        }
                    }
                    ws.send(json.dumps(getUsers))
                else:
                    ws.send("close")