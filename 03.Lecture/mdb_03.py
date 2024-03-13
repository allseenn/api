# импорт модуля
from pymongo import MongoClient
from tokens import ATLAS_USER, ATLAS_PASS, ATLAS_HOST

uri = f"mongodb+srv://{ATLAS_USER}:{ATLAS_PASS}@cluster0.{ATLAS_HOST}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

# подключение к базе данных "steam" на сервере MongoDB
db = client.steam

# определение функции, которая находит и выводит игры, соответствующие определенному запросу и проекции
def find():
    # определение запроса для поиска игр с разработчиком "Valve" и жанром "Action"
    query = {"developer" : "Valve",
             "genre" : "Action"}
    
    # определение проекции для исключения поля "_id" и включения только поля "name"
    projection = {"_id" : 0, "name" : 1}
    # поиск игр, соответствующих запросу и проекции
    games = db.games.find(query, projection)
    
    # вывод каждой игры в консоль
    for a in games:
        print(a)
# выполнение функции "find" при запуске скрипта        
if __name__ == '__main__':
    find()
