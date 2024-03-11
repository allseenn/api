from tokens import SPOON # speenacular api key
import requests
import json

url = "https://api.spoonacular.com/recipes/complexSearch"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept":  "*/*"
}

params = {
    "apiKey": SPOON,
    "query": "cherry pie",
}

response = requests.get(url, params=params, headers=headers)

if response.ok:
    data = json.loads(response.text)
    count = 1
    for item in data["results"]:
        print(item["title"])
        print(item["image"])
else:
    print("Error")