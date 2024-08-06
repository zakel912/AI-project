# Interact with MongoDB on VsCode
from pymongo import MongoClient 
from config.settings import MONGODB_CONNECTION_STRING, DATABASE_NAME

# Connect to the Database
def get_database():
    try:
        client = MongoClient(MONGODB_CONNECTION_STRING)
        print("Successfully connected to MongoDB Atlas")
        return client[DATABASE_NAME]
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise

# Insert user into the Database
def insert_user(user_info):
    db = get_database()
    collection = db['Client']
    result = collection.insert_one(user_info)
    return result.inserted_id

# Delete user's account
def delete_user(first_name, last_name):
    db = get_database()
    collection = db['Client']
    result = collection.delete_one({"first_name": first_name, "last_name": last_name})
    return result.deleted_count

# Search for a user in the Database
def find_user_by_name(first_name, last_name):
    db = get_database()
    collection = db['Client']
    user = collection.find_one({"first_name": first_name, "last_name": last_name})
    return user

# Update user's info
def update_user(name, update_fields):
    db = get_database()
    collection = db['Client']
    result = collection.update_one({"name": name}, {"$set": update_fields})
    return result.modified_count