import pymongo
from pymongoarrow.api import Schema
from pymongoarrow.monkey import patch_all
import pandas as pd
import pyarrow as pa

# Patch PyMongo to use Arrow
patch_all()

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['Items']

# Define the schema for the query
schema = Schema({
    'Item.Price': pa.float64(),
    'Item.Tax': pa.float64(),
    'Item.Date': pa.timestamp('ms')
})

# Query the collection and convert to a Pandas DataFrame
df = collection.find_pandas_all({}, schema=schema)

# Display the DataFrame
print(df.head())

# Count the total number of documents
total_documents = collection.count_documents({})
print(f'Total documents: {total_documents}')
