

# SETUP:

- in the config file, hope it's all pretty explanatory, for local tests set the proxy to false doesn't really matter
- do remmber to set use_proxy to true if u do have working proxies
- pass the username and password of the user from whom the dm is gonna be sent with the message
- just http and socks5 proxies allowed if using any 
- better the proxies, the more efficiency you get. ✅ 
````json 
{
    "instagram_settings": {
        "username": "username",
        "password": "password",
        "text_message": "message"
    },

    "script_settings": {
        "use_proxy": false,
        "proxy_type": "socsk5 / https",
        "threading": 5,
        "message_amount": 1
    }
}

````

usernames.txt 
pass in all the usernames u wish to sent a dm/follow/unfollow, each username each line
```
user1
user2
user3
```


# Running instrctions
- u can control all the run settings from the config file and run main.py
- for different user accounts to target different set of people u must add another set of usernames as a new file
- make sure u have python interpreter on your system, to check run
```commandline
python --version
```
- clone the repo either with git or download and extract the zip
```commandline
git clone https://github.com/algoomessiahs/igbot.git
```
- open your terminal and cd into the project directory
```commandline
cd path/to/ig-bot
```
- once in the directory run
```commandline
pip install -r requirements.txt
or
pip install instagrapi pymongo bs4
```
you can do the same with any missing packages
```commandline
pip install missingpackage
```
- once all ur configurations are setup properly
- then run
```commandline
python main.py
```
