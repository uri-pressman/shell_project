import getpass
import subprocess
from pathlib import Path


def run_ls(path):
    subprocess.run([r"ls.bat", path], shell=True)


def get_username():
    username = getpass.getuser()
    print("hello, " + username)


def run_hexDump(path):
    subprocess.run([r"hexDump.bat", path], shell=True)


def run_grep(params):
    if not params:
        echo_err = "Usage: grep <search_term> [file_path]"
        print(echo_err)
        return

    search_term = params[0]
    file_path = params[1] if len(params) > 1 else ""

    if file_path:
        subprocess.run([r"grep.bat", search_term, file_path], shell=True)
    else:
        subprocess.run([r"grep.bat", search_term], shell=True)


commands = {
    "hello": get_username,
    "ls": run_ls,
    "cd": None,
    "hexdump": run_hexDump,
    "grep": run_grep,
    "exit": None
}

path = r"C:\Users\talmid"
running = True

while running:
    user_input = input(f"{path}>>> ").strip().split(" ")
    if not user_input or not user_input[0]:
        continue

    command = user_input[0].lower()
    parameters = user_input[1:]

    if command in commands:
        if command == "ls":
            commands[command](path)
        elif command == "hexdump":
            if parameters:
                commands[command](parameters[0])
            else:
                print("Missing path for hexdump")
        elif command == "grep":
            commands[command](parameters)
        elif command == "cd":
            if parameters:
                tempPath = path + "\\" + parameters[0]
                if Path(tempPath).exists():
                    path = tempPath
                    print("worked")
                else:
                    print("file not found")
        elif command == "exit":
            print("exiting...")
            running = False
        else:
            commands[command]()
    else:
        print("Unknown command")