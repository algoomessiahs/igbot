
import random
import requests
import json
import main as abs

def load_config():
    try:
        with open("./config.json", "r", encoding="utf-8") as config_file:
            return json.load(config_file)
    except Exception as e:
        print(f"Error loading config file: {e}")
        return {}


# proxies = []
proxies = abs.load_proxies()
config = load_config()
try:
    proxy = {"http": f"http://{random.choice(proxies)}",
             "https": f"{config.get('script_settings', {}).get('proxy_type')}://{random.choice(proxies)}"}
    response = requests.get("http://ip-api.com/json/", proxies=proxy, timeout=7, verify=False)
    pp = proxy
    print(
        f"{abs.Color.GREEN} Proxy is working. IP: {response.json()['query']} | COUNTRY: {response.json()['country']}")
except:
    print(f"{abs.Color.RED} Bad proxy. ")
    pass