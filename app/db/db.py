from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client["recommender_db"]
products_collection = db["products"]
interactions_collection = db["interactions"]