# log_to_mongo.py

from kafka import KafkaConsumer
import json
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client['logdb']  # Database
logs_collection = db['logs']  # Collection

# Kafka Consumer setup
consumer = KafkaConsumer(
    'logs',  # the topic to listen to
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',  # Start from the first log (if available)
    group_id='log_consumer_group'
)

print("Consuming logs and storing in MongoDB...")

# Consume logs and insert into MongoDB
for message in consumer:
    print(f"Received log: {message.value}")
    
    # Insert log into MongoDB
    logs_collection.insert_one(message.value)
    print("Log inserted into MongoDB.")
