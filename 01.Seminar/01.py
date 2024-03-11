from tokens import GIPHY # import api key
import json
import requests

url = "https://api.giphy.com/v1/gifs/search"
params = {
    "api_key": GIPHY,
    "q": "programming",
    "limit": 5,
    "offset": 0,
    "rating": "pg-13",
    "lang": "ru",
    "bundle": "messaging_non_clips"
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept":  "*/*"
}

response = requests.get(url, params=params, headers=headers)

if response.ok:
    j_data = response.json()
    #print(j_data.get)
    for gif in j_data.get("data"):
        print(gif.get("images").get("original").get("url"))
    with open ("gifs.json", "w") as f:
        json.dump(j_data, f)
else:
    print("Error!")
