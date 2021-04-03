from user import User
from database import DataBase, G_DataBase
from channel import fetch

print(f"{G_DataBase.Count()} Guilds")
print(f"{DataBase.Count()} Users\n")
print("1- Add new guild")
print("2- Fetch users from guilds")
print("3- Send message to users")
print("4- Reset sent data")

choice = int(input("Choose by number: "))

if choice == 1:
	while True:
		guild_id = input("\nGuild: ")
		channel_id = input("Channel: ")
		newGuild = G_DataBase(guild_id, channel_id)
		newGuild.GoToDB()
		print("Data added")
elif choice == 2:
	fetch()
elif choice == 3:
	for user in DataBase.GetFromDB():
		message = User(user[2])

		if not int(user[3]) and message.create() and message.send():
			DataBase.SendUpdate(user[2])
			print(f"Sending to {user[1]} "+"\033[32m"+"Success"+"\033[0m")
		elif not int(user[3]):
			print(f"Sending to {user[1]} "+"\033[31m"+"Failed"+"\033[0m")
elif choice == 4:
	print("Reseting...")
	DataBase.Reset()