from pymongo import MongoClient
import json

# MongoDB connection
client = MongoClient(mongo_uri)

# Path to your backup file
backup_file = "./backup.json"

# Read the backup file
with open(backup_file, 'r') as f:
    current_db = None
    current_collection = None
    for line in f:
        if line.startswith("Database:"):
            # Parse database and collection names
            parts = line.strip().split(", ")
            current_db = parts[0].split(": ")[1]
            current_collection = parts[1].split(": ")[1]
        else:
            # Insert the JSON data into the collection
            data = json.loads(line)
            
            # If the data is a list of documents
            if isinstance(data, list):
                for doc in data:
                    # Remove the _id field to avoid duplicates
                    if '_id' in doc:
                        del doc['_id']
                client[current_db][current_collection].insert_many(data)
            else:
                # Remove the _id field if it's a single document
                if '_id' in data:
                    del data['_id']
                client[current_db][current_collection].insert_one(data)

print("Restore completed successfully.")
