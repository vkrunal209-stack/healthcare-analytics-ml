import pandas as pd

df = pd.read_excel(
    r"C:\Users\vkrun\OneDrive\Desktop\healthcare-analytics-ml\data\healthcare_dataset.csv.xlsx"
)

revenue = (
    df.groupby("Medical Condition")["Billing Amount"]
    .sum()
    .sort_values(ascending=False)
)

print(revenue)