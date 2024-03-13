import json
from pymongo import MongoClient
from tokens import ATLAS_USER, ATLAS_PASS, ATLAS_HOST

uri = f"mongodb+srv://{ATLAS_USER}:{ATLAS_PASS}@cluster0.{ATLAS_HOST}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
  
db = client["steam"]

collection = db["games"]

data = {}
# Загрузка данных из файла в коллекцию
with open('steam_games.json') as f:
    data = json.load(f)

my_list = list(data.keys())
# 999990
for i in my_list:
    try:
        collection.insert_one(data.get(i))
    except:
        print(i)