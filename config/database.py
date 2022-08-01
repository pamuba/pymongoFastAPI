from pymongo import MongoClient
import urllib.parse

# client = MongoClient("mongodb+srv://pymongo:"+ urllib.parse.quote_plus("pymongo@24")+"@cluster0.kxxmk.mongodb.net"+
# "/?retryWrites=true&w=majority", connect=False)

client = MongoClient("mongodb+srv://pymongo:"+ urllib.parse.quote_plus("pymongo@24")+"@cluster0.16kfr.mongodb.net/?retryWrites=true&w=majority")

db = client.pymongoDB

collection_name = db['todos_app']
