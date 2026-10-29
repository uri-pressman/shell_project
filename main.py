import getpass
from pathlib import Path

import subprocess

# הגדר את הנתיב המלא למקום שבו שמרת את קובץ ה-BAT שלך
bat_file_path = r"C:\Users\talmid\Downloads\test1.bat"

try:
    # הרצת קובץ ה-BAT ופתיחת חלון השרות (CMD)
    subprocess.run(bat_file_path, shell=True, check=True)

except subprocess.CalledProcessError as e:
    print(f"שגיאה בהרצת הקובץ: {e}")


# for item in folder_path.iterdir():
#     print(item.name)


def get_username():
    username = getpass.getuser()
    print("hello, " + username)

commands = {"hello": get_username}

while True:
    command = input(">>> ")
    if command in commands:
        commands[command]()
