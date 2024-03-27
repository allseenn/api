#!/usr/bin/env python3
from wildberries import *
import json
import time

def main(keyword):
    start_time = time.time()
    goods_list = scraper.goods(keyword)
    print(f"Время выполнения: {time.time() - start_time} секунд")
    print(f"Всего найдено {len(goods_list)} товаров")
    unique_list = db.unique(goods_list)
    with(open(keyword + ".json", "w")) as file:
        json.dump(unique_list, file)
    print(f"Сохранено в {keyword}.json {len(unique_list)} уникальных товаров")
    return unique_list

if __name__ == "__main__":
    keyword = input("Введите товар для поиска: ")
    main_list = main(keyword)
    # db.upload("wildberries", "smartphones", main_list)