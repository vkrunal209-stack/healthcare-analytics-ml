import pandas as pd

df = pd.read_excel(r"C:\Users\vkrun\OneDrive\Desktop\healthcare-analytics-ml\data\healthcare_dataset.csv.xlsx")

print("="*50)
print("DATASET OVERVIEW")
print("="*50)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

print("\nGender Distribution:")
print(df['Gender'].value_counts())

print("\nAdmission Type Distribution:")
print(df['Admission Type'].value_counts())

print("\nMedical Condition Distribution:")
print(df['Medical Condition'].value_counts())