import getpass
import subprocess
from symbol import parameters

import hexdump
from pathlib import Path


subprocess.run([r"grep.bat"], shell=True)

# for item in folder_path.iterdir():
#     print(item.name)

def run_ls(path):
    subprocess.run([r"ls.bat", path], shell=True)

def get_username():
    username = getpass.getuser()
    print("hello, " + username)

def run_hexDump(path):
    subprocess.run([r"hexDump.bat", path], shell=True)

commands = {"hello": get_username, "ls":run_ls, "cd":None, "hexdump":run_hexDump, "exit": None}
path = r"C:\Users\talmid"
running = True
while running:
    user_input = input(f"{path}>>> ").split(" ")
    command = user_input[0].lower()
    print(command)
    parameters = user_input[1:]


    if command in commands:
        if command == "ls":
            commands[command](path)
        elif command == "hexdump":
            commands[command](parameters[0])
        elif command == "cd":
            if parameters:
                tempPath = path + "\\" +parameters[0]
                if Path(tempPath).exists():
                    path = tempPath
                    print("worked")
                else:
                    print("file not found")
        elif command.upper() == "EXIT":
            print("exiting...")
            running = False
        else:
            commands[command]()

