# print all files in a folder

import os
import json
import pymongo

conn_str = "mongodb://root:secret@mongodb:27017/?authSource=admin&readPreference=primary&directConnection=true&ssl=false"
client = pymongo.MongoClient(conn_str)

for file in os.listdir("/files/"):
    print("filename:", file)
    with open("/files/" + file, "r") as f:
        data = json.load(f)
        client.db.transactions.insert_many(data)
        print("inserted", len(data), "records")
