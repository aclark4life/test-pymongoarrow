from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import code
import os
import readline
import rlcompleter  # noqa

# DATABASE_URL = "mongodb+srv://<u>:<p>@db_host.mongodb.net"
uri = os.environ.get("DATABASE_URL")
readfunc = readline.parse_and_bind("tab: complete")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")

except Exception as e:
    print(e)

code.interact(local=globals(), readfunc=readfunc)
