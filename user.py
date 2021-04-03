import os
import json
import requests
from dotenv import load_dotenv; load_dotenv()

token = os.getenv("Token")
message = os.getenv("Message")

class User:
    def __init__(self, id):
        self.id = id

    # create a text channel to send the message
    def create(self):
        try:
            url = "https://discord.com/api/v8/users/@me/channels"
            payload = json.dumps({ 'recipients': [ self.id ] })
            headers = { 
                'authorization': token,
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            self.channel_id = json.loads(response.text)['id']
            return True
        except:
            return False

    # send the message
    def send(self):
        try:
            url = f"https://discord.com/api/v8/channels/{self.channel_id}/messages"
            payload = json.dumps({ 'content': message })
            headers = {
                'authorization': token,
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            if json.loads(response.text)['id']:
                return True
        except: 
            return False