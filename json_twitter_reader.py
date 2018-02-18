def json_reader(url):
    """
    Function creates list with information from .json file
    (str) -> (list)
    """
    try:
        import json
        import urllib3
        import certifi
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = http.request('GET', url)
        data = json.loads(r.data.decode("utf-8"))
        friends_list = list()
        friends_list_1 = list()
        for i in range(len(data["users"])):
            friends_list.append(data["users"][i])
        for i in friends_list:
            lst = list()
            lst.append(i.get("screen_name"))
            lst.append(i.get("location"))
            lst.append(i.get("description"))
            lst.append(i.get("followers_count"))
            lst.append(i.get("created_at"))
            lst.append(i.get("lang"))
            friends_list_1.append(lst)
        return friends_list_1
    except:
        return None


def file_write(lst):
    """
    Function writes information from list in .txt file
    (list) -> None
    """
    try:
        f = open("friends_information.txt", "w")
        names = ["account name", "location", "account description", "followers", "creation time", "language"]
        for i in range(len(lst)):
            for j in range(6):
                f.write(str(names[j]) + ":" + " " + str(lst[i][j]) + "\n")
            f.write("\n")
        f.close()
    except:
        return None


import twitter2
acc = input()
file_write(json_reader(twitter2.twitter_api(acc)))
