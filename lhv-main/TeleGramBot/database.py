from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["local"]  # Replace with your database name
collection = db["lahav-project"]  # Replace with your collection name

def find_document_by_md5(md5_hash):
    return collection.find_one({"md5": md5_hash})
