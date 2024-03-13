import json
with open('steam_games.json') as f:
    data = json.load(f)

my_list = list(data.keys())
print(len(my_list))
