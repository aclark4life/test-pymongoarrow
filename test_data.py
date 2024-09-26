import pymongo
from pymongo import MongoClient
import random
from datetime import datetime, timedelta

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['Items']

# Function to generate a random date within the last 3 months
def generate_random_date():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)
    return start_date + (end_date - start_date) * random.random()

# Function to generate a single document
def generate_document():
    return {
        "Item": {
            "Price": round(random.uniform(10, 1000), 2),
            "Tax": round(random.uniform(1, 100), 2),
            "Date": generate_random_date()
        }
    }

# Generate and insert documents in batches
batch_size = 1000
total_documents = 8000000

for i in range(0, total_documents, batch_size):
    batch = [generate_document() for _ in range(batch_size)]
    collection.insert_many(batch)
    print(f'Inserted batch {i // batch_size + 1}')

print("Data generation complete.")
