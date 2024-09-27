from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongoarrow.api import Schema
from pymongoarrow.monkey import patch_all

import code
import os
import readline
import rlcompleter  # noqa

# DATABASE_URL = "mongodb+srv://<u>:<p>@<srv>.mongodb.net"
uri = os.environ.get("DATABASE_URL")

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

schema = Schema({"_id": int})
data_frame = movies.find_pandas_all({}, schema=schema)
arrow_table = movies.find_arrow_all({})

readfunc = readline.parse_and_bind("tab: complete")
code.interact(local=globals(), readfunc=readfunc)
