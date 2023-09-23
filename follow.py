import os, json, random, threading, requests, time, instagrapi, traceback, os, pymongo, subprocess
from tabnanny import check
from instagrapi import Client
from bs4 import BeautifulSoup

import main as abs



def follow(username, password, proxy, userdm, i):
    try:
        username = username
        password = password

        cl = Client()
        config = abs.load_config()
        if config["script_settings"]["use_proxy"]:
            cl.set_proxy(proxy["https"])
        cl.login(username, password)
        userid = cl.user_id_from_username(userdm)

        a = cl.user_follow(userid)
        print(
            f"{abs.Color.GREEN}[{i}] {abs.Color.RESET_ALL}Followed succesfully {abs.Color.GREEN}@{userdm} {abs.Color.RESET_ALL}with {abs.Color.GREEN}@{username}{abs.Color.RESET_ALL}.")
    except Exception as err:
        print(
            f"{abs.Color.RED}[{i}]{abs.Color.RESET_ALL} An error occured when sending message to {abs.Color.RED}@{userdm} {abs.Color.RESET_ALL}account. Passing. ERROR: {err}")
        pass






# abstraction
def startfollow(username, password, usernames):
    try:
        config = abs.load_config()
        proxies = abs.load_proxies()
        tx = []

        for id, user_name in enumerate(usernames):
            pp = None
            if config.get("script_settings", {}).get("use_proxy"):
                while pp is None:
                    try:
                        proxy = {"http": f"http://{random.choice(proxies)}",
                                 "https": f"{config.get('script_settings', {}).get('proxy_type')}://{random.choice(proxies)}"}
                        response = requests.get("http://ip-api.com/json/", proxies=proxy, timeout=7, verify=False)
                        pp = proxy
                        print(
                            f"{abs.Color.GREEN}[{id + 1}] Proxy is working. IP: {response.json()['query']} | COUNTRY: {response.json()['country']} {abs.Color.RESET_ALL}")
                    except:
                        print(f"{abs.Color.RED}[{id + 1}] Bad proxy. {proxy['https']}")
                        pass

            if config.get("script_settings", {}).get("use_proxy"):
                if threading.active_count() <= config.get("script_settings", {}).get("threading"):
                    mT = threading.Thread(target=follow, args=(
                        username,
                        password,
                        pp,
                        user_name,
                        id + 1))

                    mT.daemon = True
                    mT.start()
                    tx.append(mT)
            else:
                if threading.active_count() <= config.get("script_settings", {}).get("threading"):
                    mT = threading.Thread(target=follow, args=(
                        username,
                        password,
                        None,
                        user_name,
                        id + 1))

                    mT.daemon = True
                    mT.start()
                    tx.append(mT)

        for t in tx:
            t.join(75)
    except Exception as e:
        traceback.print_exc()
        pass




# abstraction
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    check = [True]
    if check[0]:
        print(f"{abs.Color.GREEN}[+] follow starting... {abs.Color.RESET_ALL}")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        print(fr"""{abs.Color.GREEN}
    .__                 __              .___       You don't exist ✝
    |__| ____   _______/  |______     __| _/_____  
    |  |/    \ /  ___/\   __\__  \   / __ |/     \ 
    |  |   |  \\___ \  |  |  / __ \_/ /_/ |  Y Y  \
    |__|___|  /____  > |__| (____  /\____ |__|_|  /
            \/     \/            \/      \/     \/ 

    Running . . . Hit a key and enter to start...
    {abs.Color.RESET_ALL}    """)
        input("....")

        try:
            startfollow()
            input("....")
        except:
            traceback.print_exc()
            input(".....")
    else:
        print(f"{abs.Color.RED}[-] {check[1]} {abs.Color.RESET_ALL}")
        input("....")

