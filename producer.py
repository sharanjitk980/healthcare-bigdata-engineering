# producer.py
import pandas as pd
from kafka import KafkaProducer
import json
import time

# Load your integrated dataset
file_path = r"C:\Users\shara\OneDrive\Desktop\GDDA707 advanced data engineering\New assessment 2files\integrated_final_df.csv"
df = pd.read_csv(file_path)


# Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send each row as a message
for idx, row in df.iterrows():
    message = row.to_dict()
    producer.send("hospital_admissions", value=message)
    print(f"Sent message: {message}")
    time.sleep(0.1)  # simulate streaming (100ms delay)

producer.flush()
producer.close()
