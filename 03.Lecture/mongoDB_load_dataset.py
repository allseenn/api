import json
import time
from pymongo import MongoClient
from tokens import ATLAS_USER, ATLAS_PASS, ATLAS_HOST
PARTS = 4

start_time = time.time()
uri = f"mongodb+srv://{ATLAS_USER}:{ATLAS_PASS}@cluster0.{ATLAS_HOST}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
  
db = client["steam"]

collection = db["games"]

data = {}
# Загрузка данных из файла в коллекцию
with open('steam_games.json') as f:
    data = json.load(f)

sum_from_file = len(data)
print(sum_from_file, "docs is loaded from file in", time.time() - start_time, "seconds")

my_list = list(data.keys())
quarter = len(my_list) // PARTS
extra = len(my_list) % PARTS  # Вычисляем количество дополнительных элементов
start = 0
sum_loaded = 0
for i in range(PARTS):
    extra_element = 1 if i < extra else 0  # Дополнительный элемент для первых extra частей
    quarter_list = my_list[start:start+quarter+extra_element]
    quarter_dict_list = [data.get(j) for j in quarter_list]
    collection.insert_many(quarter_dict_list)
    sum_loaded += len(quarter_dict_list)
    print(f"Part {i+1} from {PARTS} loaded in {time.time() - start_time:.2f} seconds. Total {sum_loaded} docs")
    start += quarter + extra_element

print(f"\nTotal {sum_loaded} docs loaded in {time.time() - start_time:.2f} seconds and {sum_from_file - sum_loaded} docs is lost")

