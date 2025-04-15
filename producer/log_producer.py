# log_producer.py

from kafka import KafkaProducer
import json
import time
from datetime import datetime
import random

# Log levels and services
log_levels = ['INFO', 'WARNING', 'ERROR']
services = ['auth-service', 'payment-service', 'order-service', 'user-service', 'inventory-service']

# Service-specific log messages
service_messages = {
    'auth-service': [
        'User login successful.',
        'User password changed.',
        'Failed login attempt.',
        'User registered successfully.'
    ],
    'payment-service': [
        'Payment processed successfully.',
        'Payment failed due to insufficient funds.',
        'Refund issued successfully.',
        'Payment gateway timeout error.'
    ],
    'order-service': [
        'Order placed successfully.',
        'Order cancellation requested.',
        'Out of stock error.',
        'Order shipped.'
    ],
    'user-service': [
        'User profile updated.',
        'User address added.',
        'User deleted.',
        'User verification email sent.'
    ],
    'inventory-service': [
        'Item added to inventory.',
        'Inventory check completed.',
        'Item stock level updated.',
        'Inventory error: negative stock.'
    ]
}

# Kafka Producer setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Producing logs with more variety...")



#making the custom data
def log_collate():
    service = random.choice(services)
    level = random.choice(log_levels)
    message = random.choice(service_messages[service])
    return {
        "service": service,
        "level": level,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }



if __name__=="main":
    log=log_collate()
    producer.send('logs', value=log)
    print(f"Sent log: {log}")
    time.sleep(2)  # Simulate log production every 2 seconds