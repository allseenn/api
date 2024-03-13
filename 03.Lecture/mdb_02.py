from pymongo import MongoClient
from tokens import ATLAS_USER, ATLAS_PASS, ATLAS_HOST

uri = f"mongodb+srv://{ATLAS_USER}:{ATLAS_PASS}@cluster0.{ATLAS_HOST}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

db = client.steam

def find():
   query = {"developer" : "Valve",
            "genre" : "Action"}

   games = db.games.find(query)
   for a in games:
       print(a)
      
if __name__ == '__main__':
   find()