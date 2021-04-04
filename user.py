import os
import json
import requests
from dotenv import load_dotenv; load_dotenv()

token = ""
guild_id = None
invite = os.getenv("invite")

with open("embed.json", "r") as f:
    embed = json.load(f)

def change_token():
    global token
    f_out = open("token/out.txt", "r+")
    used_token = f_out.read()

    with open("token/in.txt", "r") as f_in:
        for new_token in f_in.read().split('\n'):
            if new_token in used_token or not join(new_token):
                continue
            if token:
                leave()

            f_out.write(new_token+'\n')
            token = new_token
            break

    f_out.close()

def join(token):
    try:
        global guild_id
        url = "https://discord.com/api/v8/invites/" + invite
        headers = {
            'Cookie': '__cfduid=db07e6c454c1cb90e3b903a6500527f391617469496',
            'authorization': token,
            'x-super-properties': 'eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS45MCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiODkuMC40Mzg5LjkwIiwib3NfdmVyc2lvbiI6IiIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzY29yZC5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODEzMjksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers)
        guild_id = json.loads(response.text)['guild']['id']
        return True
    except:
        print("\033[31m"+"Failed to join the guild"+"\033[0m")
        return False

def leave():
        url = "https://discord.com/api/v8/users/@me/guilds/" + guild_id
        headers = {
            'Cookie': '__cfduid=db07e6c454c1cb90e3b903a6500527f391617469496',
            'authorization': token,
            'x-super-properties': 'eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS45MCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiODkuMC40Mzg5LjkwIiwib3NfdmVyc2lvbiI6IiIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzY29yZC5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODEzMjksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
            'Content-Type': 'application/json'
        }
        response = requests.request("DELETE", url, headers=headers)
        if response.status_code != 204:
            print("\033[31m"+"Failed to leave the guild"+"\033[0m")

class User:
    def __init__(self, id):
        self.id = id

    # create a text channel to send the message
    def create(self):
        try:
            url = "https://discord.com/api/v8/users/@me/channels"
            payload = json.dumps({ 'recipients': [ self.id ] })
            headers = { 
                'Cookie': '__cfduid=db07e6c454c1cb90e3b903a6500527f391617469496',
                'authorization': token,
                'Content-Type': 'application/json',
                'x-super-properties': 'eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS45MCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiODkuMC40Mzg5LjkwIiwib3NfdmVyc2lvbiI6IiIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzY29yZC5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODEzMjksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
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
            payload = json.dumps({ 'embed': embed })
            headers = {
                'authorization': token,
                'Content-Type': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            if json.loads(response.text)['id']:
                return True
        except: 
            return False