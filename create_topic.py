# create_topic.py
from kafka.admin import KafkaAdminClient, NewTopic

# Connect to Kafka
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id="hospital_admin"
)

# Create topic
topic_list = [NewTopic(name="hospital_admissions", num_partitions=1, replication_factor=1)]
try:
    admin_client.create_topics(new_topics=topic_list, validate_only=False)
    print("Topic 'hospital_admissions' created successfully")
except Exception as e:
    print("Topic may already exist:", e)

# List topics to confirm
topics = admin_client.list_topics()
print("Current topics:", topics)
