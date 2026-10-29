import getpass
from pathlib import Path



# for item in folder_path.iterdir():
#     print(item.name)


def get_username():
    username = getpass.getuser()
    print("hello " + username)

commands = {"hello": get_username}

while True:
    command = input(">>> ")
    if command in commands:
        commands[command]()
