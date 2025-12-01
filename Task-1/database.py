from pymongo import MongoClient

client = MongoClient("mongodb+srv://mehulUser:mehul123@cluster0.0tz9o4j.mongodb.net/?appName=Cluster0")
db = client['RedundancyDB']
collection = db['entries']

def insert_entry(name, email):
    if collection.find_one({'email': email}):
        return False  # Duplicate found
    else:
        collection.insert_one({'name': name, 'email': email})
        return True

