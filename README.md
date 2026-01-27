# Healthcare Big Data Engineering Project

**Author:** Sharanjit Kaur  
**GitHub:** [sharanjitk980](https://github.com/sharanjitk980)  
**Date:** January 2026  

---

## Project Overview

This project simulates a **real-time hospital readmission risk analysis system** for a fictional hospital named **Rai Hospital**. 
The goal is to demonstrate **big data engineering and streaming techniques** by integrating two healthcare datasets, processing them 
using **Apache Spark**, storing data in **HDFS, Hive, and MongoDB**, and streaming data in real-time using **Apache Kafka** in **Docker** container.  

The system focuses on identifying patient readmission risks within 30 days after hospital discharge 
and clustering patients based on lifestyle, mental health, and clinical data.  

**Scenario- Hospital Readmission Risk**
In this Assessment, I used a fictional organisation name, Rai Hospital, to model a realistic hospital data environment, aimed at analysing and reducing hospital readmission rates within 30 days of discharge. Hospital readmission within a short period of time after discharge is a critical issue in the modern healthcare system. Readmission places a significant burden on hospitals by reducing bed availability and increasing operational costs. 
Rai Hospital generates a large volume of data across multiple systems, including patient demographic records, hospital admissions, and follow-up outcomes. Efficient analysis helps hospitals to gain a comprehensive understanding of factors contributing to hospital readmissions.

**The primary actors in the scenario:**
Hospital management: Use readmission insights to optimise resource allocation.
Patients: Interact with the healthcare system through hospital admissions and treatments. Health data analyst: Evaluate outcomes, identify risk factors and improve patient care.
Healthcare providers: collect and manage patient records and admission data.

**What questions do we want to answer with this data?**
1.	How do lifestyle factors such as alcohol_use and bmi relate to readmitted_within_30_days?
2.	How do chronic conditions and follow-up visits relate to length_of_stay?
3.	What is the relationship between social_support_score, mental_health_score, and readmission outcomes?

**Two datasets Selection:**
Two logically related datasets are used. Both datasets were derived from an original healthcare dataset and selected from publicly available datasets from Kaggle.com to support the hospital readmission, and were modified for this project. (Miah, 2025) 

**Dataset 1:**  Patient_profile_lifestyle.csv
Description: This dataset contains patients’ demographic, lifestyle, and background information related to health. Each row represents one unique patient.
Columns:
 

**Dataset 2:**  Admission_clinical_data.csv
Description: This dataset contains hospital admission level and clinical information. Each row represents one hospital admission associated with a patient. It is essential for understanding how in-hospital treatment and post-discharge behaviour relate to readmission outcomes.
 

Relationships between the datasets
They are connected through one shared key, patient_id. The patient profile dataset provides long-term demographic information, which remains relatively stable over time, and the admission dataset provides short-term clinical and operational details for each hospital visit. Integrating these datasets allows a complete view of patient risk factors and hospital outcomes.


---------------------------------------------------------------------------------------------------
**ETL Process**
Load Data: CSV files uploaded to Google Colab and loaded into Pandas DataFrames.

Preprocessing:

Check for missing values and duplicates.

Handle missing values using mean, median, or mode imputation based on skewness.

Detect and handle outliers using boxplots.

Standardize data types for numerical columns.

Integration:

Inner join datasets on patient_id to create a unified dataset.

Validate dataset: 9999 rows and 23 columns.

Save Files: Export as CSV and Parquet for scalable analytics.

**HDFS & Data Storage**

Setup Hadoop 3.3.6 in Google Colab.

Configure environment variables: JAVA_HOME, HADOOP_HOME, PATH.

save file to HDFS

**Hive & MongoDB**

Hive:

Store integrated dataset as a Hive table in Parquet format.

Execute SQL queries to analyse readmission risk and patient clusters.

MongoDB:

Store semi-structured datasets as JSON-like documents.

Use PyMongo to insert and query documents.

Combine

**Real-Time Data Clustering with Spark Streaming**

Simulate hospital event stream with integrated CSV dataset.

Spark Structured Streaming reads new records incrementally.

Feature Engineering Pipeline: scale features, prepare dataset for clustering.

K-Means Clustering: identify patient risk groups:

Cluster 0 – Low social support, high readmission risk.

Cluster 1 – High social support, low readmission risk, short length of stay.

Save results in Parquet for further analysis.

**Kafka Streaming Pipeline**

Kafka runs in Kraft mode inside Docker.

Producer.py: sends each row of CSV as a JSON message to the Kafka topic.

Consumer.py: reads messages, applies feature scaling, clusters patients using K-Means.

------------------------------------------------------------------------------------------------
# Project Structure

**PythonProject**/
│
├── **Raw+ETL**/
    ├──Raw files
    ├──Patient_profile_lifestyle.csv
    ├──Admission_clinical_data.csv
    ├──**After cleanning**
    ├── integrated_final_df.csv
    └── Assessment2_707.ipynb
|**Kafka Files**
├── producer.py
├── consumer.py
├── create_topic.py
├── README.md
└── .gitignore


