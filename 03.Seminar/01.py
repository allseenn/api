from pprint import pprint
from pymongo import MongoClient
from tokens import ATLAS_USER, ATLAS_PASS, ATLAS_HOST

uri = f"mongodb+srv://{ATLAS_USER}:{ATLAS_PASS}@cluster0.{ATLAS_HOST}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
steam = client["steam"]
games = steam["games"]
# print(f'Docs count: {games.count_documents({"name" : {"$regex" : ".*[Pp]uzzle.*"}})}')

res = list(games.find(
    {
        'name' : {'$regex' : 'Puzzle Pirate'},
        
    }, {'_id': 0, 'appid': 0, 'categories': 0, 'tags': 0, 'short_description': 0}
    ))
pprint(res)

