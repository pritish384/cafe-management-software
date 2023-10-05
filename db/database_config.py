from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

conn = 'localhost:27017'

# Create a new client and connect to the server
client = MongoClient(conn, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# admin cafe database
admin_cafe = client['admin_cafe']
active_orders = admin_cafe['active_orders']
closed_orders = admin_cafe['closed_orders']