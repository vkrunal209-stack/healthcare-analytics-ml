import pandas as pd

df = pd.read_excel(r"C:\Users\vkrun\OneDrive\Desktop\healthcare-analytics-ml\data\healthcare_dataset.csv.xlsx")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())