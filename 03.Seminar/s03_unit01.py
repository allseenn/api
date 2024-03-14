import json
from pymongo import MongoClient
from tokens import ATLAS_USER, ATLAS_PASS, ATLAS_HOST

uri = f"mongodb+srv://{ATLAS_USER}:{ATLAS_PASS}@cluster0.{ATLAS_HOST}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

# Выбор базы данных и коллекции
db = client['town_cary']
collection = db['crashes']

# Чтение файла JSON
with open('crash-data.json', 'r') as file:
    data = json.load(file)

data = data['features']

# Функция разделения данных на более мелкие фрагменты
def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

# Разделение данных на фрагменты по 5000 записей в каждом
chunk_size = 5000
data_chunks = list(chunk_data(data, chunk_size))

# Вставка фрагментов в коллекцию MongoDB
for chunk in data_chunks:
    collection.insert_many(chunk)

print("Данные успешно вставлены.")
