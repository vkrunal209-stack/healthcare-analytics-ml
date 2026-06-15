import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(
    r"C:\Users\vkrun\OneDrive\Desktop\healthcare-analytics-ml\data\healthcare_dataset.csv.xlsx"
)

condition_counts = df["Medical Condition"].value_counts()

plt.figure(figsize=(8,5))
condition_counts.plot(kind="bar")

plt.title("Patient Distribution by Medical Condition")
plt.xlabel("Medical Condition")
plt.ylabel("Number of Patients")

plt.tight_layout()

plt.savefig(
    r"C:\Users\vkrun\OneDrive\Desktop\healthcare-analytics-ml\data\images\medical_condition_distribution.png"
)

plt.show()