import os
import json
import pymongo

from bson.objectid import ObjectId


def print_output(*args):
    for a in args:
        vals = [*a.values()]
        print(f"{vals[0]}: {vals[1]}")


if __name__ == "__main__":
    conn_str = "mongodb://root:secret@mongodb:27017/?authSource=admin&readPreference=primary&directConnection=true&ssl=false"
    client = pymongo.MongoClient(conn_str)

    db = client.db
    collection = db.transactions

    print(f"Number of unique ids: {len(collection.distinct('_id'))} ")
    print(f"Number of unique products: {len(collection.distinct('order.product'))} ")
    print("\n")

    pipeline = [{"$group": {"_id": 0, "avg_val": {"$avg": "$order.amount"}}}]
    output = collection.aggregate(pipeline)
    print("Avg value of order:")
    print(output.next()["avg_val"])
    print("\n")

    pipeline = [{"$group": {"_id": 0, "sum_val": {"$sum": "$order.amount"}}}]
    sum_val = collection.aggregate(pipeline)
    record = sum_val.next()["sum_val"]
    print(f"Sum of order values: {record} \n")

    pipeline = [{"$group": {"_id": "$website", "count": {"$sum": 1}}}]
    output = collection.aggregate(pipeline)
    print(f"Distribution of websites:")
    print_output(*output)
    print("\n")

    pipeline = [
        {
            "$group": {
                "_id": {"$dayOfWeek": {"$toDate": "$order.date"}},
                "count": {"$sum": "$order.amount"},
            }
        },
        {"$sort": {"_id": -1}},
    ]
    output = collection.aggregate(pipeline)
    print("Order.amount by day of week: \n")
    print_output(*output)
    print("\n")

    pipeline = [
        {"$group": {"_id": "$order.product", "count": {"$sum": "$order.amount"}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
    ]
    output = collection.aggregate(pipeline)
    print("Order.amount by product (top 10): \n")
    print_output(*output)
    print("\n")

    pipeline = [
        {
            "$group": {
                "_id": {"$month": {"$toDate": "$order.date"}},
                "count": {"$sum": "$order.amount"},
            }
        },
        {"$sort": {"_id": -1}},
    ]
    output = collection.aggregate(pipeline)
    print("Order.amount by month: \n")
    print_output(*output)
    print("\n")

    pipeline = [{"$group": {"_id": "$client.country", "count": {"$sum": 1}}}]
    output = collection.aggregate(pipeline)
    print(f"Distribution of countries:")
    print_output(*output)
    print("\n")
