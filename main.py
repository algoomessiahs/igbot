import os
import json
import random
import threading
import requests
import time
import instagrapi
import traceback
import pymongo
import subprocess
from tabnanny import check
from instagrapi import Client
from bs4 import BeautifulSoup

import follow as fall
import unfollow as unfall

# Constants
CONFIG_FILE = "./config.json"
PROXIES_FILE = "./proxies.txt"
USERNAMES_FILE = "./usernames.txt"

class Color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET_ALL = "\033[0m"
    BLUE = '\033[96m'

def load_config():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as config_file:
            return json.load(config_file)
    except Exception as e:
        print(f"Error loading config file: {e}")
        return {}

def load_proxies():
    try:
        with open("./proxies.txt", "r", encoding="utf-8") as proxies_file:
            return proxies_file.read().splitlines()
    except Exception as e:
        print(f"Error loading proxies file: {e}")
        return []

def user_handler():
    try:
        with open("./usernames.txt", encoding="utf-8") as usernames_file:
            return [line.strip() for line in usernames_file]
    except Exception as e:
        print(f"Error loading usernames file: {e}")
        return []

def send_dm(username, password, proxy, userdm, message_text, count, i):
    try:
        cl = Client()
        config = load_config()
        if config.get("script_settings", {}).get("use_proxy"):
            cl.set_proxy(proxy["https"])
        cl.login(username, password)
        userid = cl.user_id_from_username(userdm)
        for x in range(count):
            a = cl.direct_send(message_text, [int(userid)])
            print(f"{Color.GREEN}[{i}] {Color.RESET_ALL}Message successfully sent to {Color.GREEN}@{userdm} {Color.RESET_ALL}with {Color.GREEN}@{username}{Color.RESET_ALL}.")
    except Exception as err:
        print(f"{Color.RED}[{i}]{Color.RESET_ALL} An error occurred when sending a message to {Color.RED}@{userdm} {Color.RESET_ALL}account. Passing. ERROR: {err}")
        pass




# ...
def startdm(username, password, usernames, textmessage):
    try:
        config = load_config()
        proxies = load_proxies()
        if textmessage == None or "":
            message = config.get("instagram_settings", {}).get("text_message"),
        else:
            message = textmessage

        tx = []

        for id, user_name in enumerate(usernames):
            pp = None
            if config.get("script_settings", {}).get("use_proxy"):
                while pp is None:
                    try:
                        proxy = {"http": f"http://{random.choice(proxies)}", "https": f"{config.get('script_settings', {}).get('proxy_type')}://{random.choice(proxies)}"}
                        response = requests.get("http://ip-api.com/json/", proxies=proxy, timeout=7, verify=False)
                        pp = proxy
                        print(f"{Color.GREEN}[{id+1}] Proxy is working. IP: {response.json()['query']} | COUNTRY: {response.json()['country']} {Color.RESET_ALL}")
                    except:
                        print(f"{Color.RED}[{id+1}] Bad proxy. {proxy['https']}")
                        pass

            if config.get("script_settings", {}).get("use_proxy"):
                if threading.active_count() <= config.get("script_settings", {}).get("threading"):
                    mT = threading.Thread(target=send_dm, args=(
                        username,
                        password,
                        pp,
                        user_name,
                        message,
                        config.get("script_settings", {}).get("message_amount"),
                        id+1))

                    mT.daemon = True
                    mT.start()
                    tx.append(mT)
            else:
                if threading.active_count() <= config.get("script_settings", {}).get("threading"):
                    mT = threading.Thread(target=send_dm, args=(
                        username,
                        password,
                        None,
                        user_name,
                        message,
                        config.get("script_settings", {}).get("message_amount"),
                        id+1))

                    mT.daemon = True
                    mT.start()
                    tx.append(mT)

        for t in tx:
            t.join(75)
    except Exception as e:
        traceback.print_exc()
        pass
# ...


def follow_users(account_config):
    usernames = user_handler()
    username = account_config["username"]
    password = account_config["password"]
    fall.startfollow(usernames, username, password)

def dm_users(account_config):
    usernames = user_handler()
    username = account_config["username"]
    password = account_config["password"]
    textmessage = account_config["message"]
    startdm(username, password, usernames, textmessage)



def main():
    config = load_config()

    for account_config in config.get("accounts", []):
        if account_config["action"] == "follow":
            # Call the function to follow users with this account_config
            follow_users(account_config)
        elif account_config["action"] == "dm":
            # Call the function to DM users with this account_config
            dm_users(account_config)
        elif account_config["action"] == "fd":
            follow_users(account_config)
            dm_users(account_config)
        # You can add more conditions for other actions as needed


if __name__ == "__main__":
    unfall.loaddata()
    os.system("cls" if os.name == "nt" else "clear")
    check = [True]
    if check[0]:
        print(f"{Color.GREEN}[+] main starting... {Color.RESET_ALL}")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        print(fr"""{Color.GREEN}
    .__                 __              .___       You don't exist ✝
    |__| ____   _______/  |______     __| _/_____  
    |  |/    \ /  ___/\   __\__  \   / __ |/     \ 
    |  |   |  \\___ \  |  |  / __ \_/ /_/ |  Y Y  \
    |__|___|  /____  > |__| (____  /\____ |__|_|  /
            \/     \/            \/      \/     \/ 

    Running . . . Hit a key and enter to start...
    {Color.RESET_ALL}    """)
        input("....")

        try:
            main()
            input("....")
        except:
            traceback.print_exc()
            input(".....")
    else:
        print(f"{Color.RED}[-] {check[1]} {Color.RESET_ALL}")
        input("....")
