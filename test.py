
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os

uri = os.environ.get("DATABASE_URL")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    query = {'release_year': 2021}
    client.movies = collection.find(query)

except Exception as e:
    print(e)
