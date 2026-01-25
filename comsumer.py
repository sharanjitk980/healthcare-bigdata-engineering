# consumer_clustering.py
from kafka import KafkaConsumer
import json
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Kafka consumer
consumer = KafkaConsumer(
    'hospital_admissions',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='hospital_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Collect incoming messages in a DataFrame
data_list = []

for message in consumer:
    data_list.append(message.value)
    print("Received:", message.value)

    # Once we have 10 records, run clustering
    if len(data_list) >= 10:
        df = pd.DataFrame(data_list)

        # Select numeric features for clustering
        features = ['age', 'weight_kg', 'height_cm', 'bmi', 'num_previous_admissions', 'medications_count', 'last_hemoglobin', 'last_glucose', 'last_creatinine', 'length_of_stay', 'procedures_count']
        X = df[features].astype(float)

        # Scale features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Apply KMeans clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        clusters = kmeans.fit_predict(X_scaled)

        df['cluster'] = clusters
        print("\nClustering Results:")
        print(df[['patient_id', 'cluster']])

        # Clear data_list for next batch
        data_list = []
