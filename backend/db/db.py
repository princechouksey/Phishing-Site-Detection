# db/db.py
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"  # Change this if needed
client = AsyncIOMotorClient(MONGO_URI)

db = client["phishing_detection_db"]
collection = db["results"]
