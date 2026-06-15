import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    r"C:\Users\vkrun\OneDrive\Desktop\healthcare-analytics-ml\data\healthcare_dataset.csv.xlsx"
)

revenue = (
    df.groupby("Medical Condition")["Billing Amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
revenue.plot(kind="bar")

plt.title("Revenue by Medical Condition")
plt.xlabel("Medical Condition")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()