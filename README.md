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

---

## Features

- **ETL Operations:** Clean, preprocess, and integrate two datasets:  
  - `Patient_profile_lifestyle.csv` – patient demographics and lifestyle information.  
  - `Admission_clinical_data.csv` – hospital admission and clinical records.  
- **Big Data Storage:**  
  - Store processed data in **HDFS** for scalable access.  
  - Store structured data in **Hive** tables.  
  - Store semi-structured JSON-like data in **MongoDB** collections.  
- **Real-Time Streaming:**  
  - Kafka producer reads integrated dataset and sends messages to `hospital_admissions` topic.  
  - Kafka consumer receives messages and processes them in real-time for clustering.  
- **Data Analysis & Clustering:**  
  - Apache Spark Structured Streaming is used to monitor incoming data.  
  - K-Means clustering groups patients into risk categories.  

---
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


