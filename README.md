
# first version of the bot pretty basic stuff

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

````usernames
        pass in all the usernames u wish to sent a dm/follow/unfollow, each username each line
````


# for version 2
- for the usernames to be scraped based on location or wtv needs u have



# Running instrctions
- make sure u have python interpreter on your system, to check run $ python --version
- clone the repo either with git or download and extract the zip
- open your terminal and cd into the project directory $ cd path/to/ig-bot
- once in the directory run $ pip install -r requirements.txt
- once all ur configurations are setup properly
- then run $ python main.py
