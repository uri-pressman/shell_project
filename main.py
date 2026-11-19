import getpass
import subprocess
from pathlib import Path


def resolve_file_path(file_path, current_dir):
    result = file_path
    candidate = Path(file_path)
    relative_candidate = Path(current_dir) / file_path
    if candidate.exists():
        result = str(candidate)
    elif relative_candidate.exists():
        result = str(relative_candidate)
    return result


def run_ls(path):
    return subprocess.run([r"ls.bat", path], shell=True)


def get_username():
    username = getpass.getuser()
    print("hello, " + username)
    return None


def run_hexDump(path):
    return subprocess.run([r"hexDump.bat", path], shell=True)


def run_grep(params, current_dir, stdin_data=None):
    result = None
    if not params:
        print("Usage: grep <search_term> [file_path]")
    else:
        search_term = params[0]
        if len(params) > 1:
            file_path = resolve_file_path(params[1], current_dir)
            result = subprocess.run([r"grep.bat", search_term, file_path], shell=True)
        else:
            result = subprocess.run(
                [r"grep.bat", search_term],input=stdin_data,text=True,shell=True,
            )
    return result


commands = {
    "hello": get_username,
    "ls": run_ls,
    "cd": None,
    "cd--": None,
    "hexdump": run_hexDump,
    "grep": run_grep,
    "exit": None,
}

path = r"C:\Users\talmid"
running = True

while running:
    raw_input = input(f"{path}>>> ").strip()
    if not raw_input:
        continue

    if "|" in raw_input:
        parts_left, parts_right = [p.strip() for p in raw_input.split("|", 1)]
        left_tokens = parts_left.split(" ")
        right_tokens = parts_right.split(" ")
        left_cmd = left_tokens[0].lower()
        right_cmd = right_tokens[0].lower()

        if left_cmd == "ls" and right_cmd == "grep":
            ls_proc = subprocess.run(
                [r"ls.bat", path], text=True,capture_output=True,shell=True,
            )
            run_grep(right_tokens[1:], path, stdin_data=ls_proc.stdout)
            print()
            continue

    user_input = raw_input.split(" ")
    command = user_input[0].lower()
    parameters = user_input[1:]

    if command in commands:
        if command == "ls":
            commands[command](path)
        elif command == "hexdump":
            if parameters:
                commands[command](resolve_file_path(parameters[0], path))
            else:
                print("Missing path for hexdump")
        elif command == "grep":
            commands[command](parameters, path)
            print()
        elif command == "cd":
            if parameters:
                tempPath = str(Path(path) / parameters[0])
                if Path(tempPath).exists():
                    path = tempPath
                else:
                    print("file not found")
        elif command == "cd--":
            path = str(Path(path).parent)
        elif command == "exit":
            print("exiting...")
            running = False
        else:
            commands[command]()
    else:
        print("Unknown command")