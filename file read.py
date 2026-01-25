import pandas as pd

df = pd.read_csv(r"C:\Users\shara\OneDrive\Desktop\GDDA707 advanced data engineering\New assessment 2files\integrated_final_df.csv")

# Print all columns
print(df.columns.tolist())

# Select only numeric columns
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

print("Numeric columns found in the dataset:", numeric_columns)
