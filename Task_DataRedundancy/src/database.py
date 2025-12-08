import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASSWORD")
cluster = os.getenv("MONGO_CLUSTER")
database_name = os.getenv("DATABASE_NAME")

connection_string = f"mongodb+srv://{username}:{password}@{cluster}/{database_name}?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client[database_name]
collection = db['entries']

def insert_entry(name, email):
    if collection.find_one({'email': email}):
        return False  # Duplicate found
    else:
        collection.insert_one({'name': name, 'email': email})
        return True
