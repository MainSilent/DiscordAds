from user import User
from database import DataBase, G_DataBase
from channel import fetch
from guild import guild
from friends import start_friend_requests

print(f"{DataBase.nCount()}/{DataBase.Count()} Users\n")
print("1- Get guilds")
print("2- Fetch users from guilds")
print("3- Send message to users")
print("4- Send message with friend request")
print("5- Reset sent data")
print("6- Truncate users")

choice = int(input("Choose by number: "))

if choice == 1:
	guild()
elif choice == 2:
	fetch()
elif choice == 3:
	users = DataBase.GetFromDB()
	for user in users:
		message = User(user[2])

		if not int(user[3]) and message.create() and message.send():
			DataBase.SendUpdate(user[2], 1)
			print(f"Sending to {user[1]} "+"\033[32m"+"Success"+"\033[0m")
		elif not int(user[3]):
			print(f"Sending to {user[1]} "+"\033[31m"+"Failed"+"\033[0m")
elif choice == 4:
	start_friend_requests()
elif choice == 5:
	print("Reseting...")
	DataBase.Reset()
elif choice == 6:
	print("Truncating...")
	DataBase.truncate()