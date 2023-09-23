def start(thread):
    try:
        tx = []

        for id, user_name in enumerate(abs.user_handler()):

            pp = None
            while pp is None:
                try:
                    prox = {"http": f"http://{random.choice(proxies)}",
                            "https": f"{config['script_settings']['proxy_type']}://{random.choice(proxies)}"}
                    a = requests.get("http://ip-api.com/json/", proxies=prox, timeout=7, verify=False)
                    pp = prox
                    print(
                        f"{abs.color.GREEN}[{id + 1}] Proxy is working. IP: {a.json()['query']} | COUNTRY: {a.json()['country']} {abs.color.RESET_ALL}")
                except:
                    print(f"{abs.color.RED}[{id + 1}] Bad proxy. {prox['https']}")
                    pass

            if config["script_settings"]["use_proxy"]:

                if threading.active_count() <= thread:
                    mT = threading.Thread(target=follow, args=(
                        config["instagram_settings"]["username"],
                        config["instagram_settings"]["password"],
                        pp,
                        user_name,
                        id + 1))

                    mT.daemon = True
                    mT.start()
                    tx.append(mT)
            else:
                if threading.active_count() <= thread:
                    mT = threading.Thread(target=follow, args=(
                        config["instagram_settings"]["username"],
                        config["instagram_settings"]["password"],
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


