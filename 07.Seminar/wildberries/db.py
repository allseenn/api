#!/usr/bin/env python3
from pymongo import MongoClient
from wildberries.tokens import ATLAS_USER, ATLAS_PASS, ATLAS_HOST

uri = f"mongodb+srv://{ATLAS_USER}:{ATLAS_PASS}@cluster0.{ATLAS_HOST}.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

def download(dbname: str, collection: str)->list:
    db = client[dbname]
    collection = db[collection]
    documents = list(collection.find())
    return documents

def upload(dbname: str, collection: str, dicts_list: list):
    db = client[dbname]
    collection = db[collection]
    unique_list = unique(dicts_list)
    collection.insert_many(unique_list)


def unique(dicts_list: list):
    return list({v['id']:v for v in dicts_list}.values())

if __name__ == '__main__':
    DB = 'wildberries'
    COLLECTION = 'smartphones'
    downloaded_list = download(DB, COLLECTION)
    print(len(downloaded_list))
    print(type(downloaded_list))