import os
import json
import pymongo

from bson.objectid import ObjectId

conn_str = "mongodb://root:secret@mongodb:27017/?authSource=admin&readPreference=primary&directConnection=true&ssl=false"
client = pymongo.MongoClient(conn_str)
client.drop_database("transactions")

for file in os.listdir("/files/"):
    print("filename:", file)
    with open("/files/" + file, "r") as f:
        data = json.load(f)
        for item in data:
            oid = item["transaction_id"]["$oid"]
            item["transaction_id"] = ObjectId(oid)
        client.db.transactions.insert_many(data)
        print("inserted", len(data), "records")
