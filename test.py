from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongoarrow.api import Schema
from pymongoarrow.monkey import patch_all

import code
import os
import pymongo
import readline
import rlcompleter  # noqa
from bson.objectid import ObjectId

# DATABASE_URL = "mongodb+srv://<u>:<p>@<srv>.mongodb.net"
# uri = os.environ.get("DATABASE_URL")
uri = "mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")

except Exception as e:
    print(e)

sample_mflix = client["sample_mflix"]
movies = sample_mflix["embedded_movies"]

patch_all()  # add PyMongoArrow functionality directly to Collection instances

# Check the current number of movies
current_count = movies.count_documents({})
target_count = 8000000

if current_count < target_count:
    # Calculate the number of movies to copy
    movies_to_copy = target_count - current_count

    # Fetch all movies
    all_movies = list(movies.find())

    # Insert movies until the target count is reached
    while current_count < target_count:
        # Ensure unique _id for each document
        for movie in all_movies[:movies_to_copy]:
            movie["_id"] = ObjectId()

        try:
            movies.insert_many(all_movies[:movies_to_copy])
            current_count += len(all_movies[:movies_to_copy])
            print(
                f"Inserted {len(all_movies[:movies_to_copy])} movies. Current count: {current_count}"
            )
        except pymongo.errors.BulkWriteError as bwe:
            print(f"Bulk write error: {bwe.details}")
            break

schema = Schema({"_id": int})
data_frame = movies.find_pandas_all({}, schema=schema)
arrow_table = movies.find_arrow_all({})

readfunc = readline.parse_and_bind("tab: complete")
code.interact(local=globals(), readfunc=readfunc)
