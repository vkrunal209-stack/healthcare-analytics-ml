import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df = pd.read_excel(
    r"C:\Users\vkrun\OneDrive\Desktop\healthcare-analytics-ml\data\healthcare_dataset.csv.xlsx"
)

df["Cost_Category"] = pd.cut(
    df["Billing Amount"],
    bins=[-999999999, 10000, 30000, 999999999],
    labels=["Low", "Medium", "High"]
)

df = df.dropna(subset=["Cost_Category"])

df["Gender"] = LabelEncoder().fit_transform(df["Gender"])
df["Medical Condition"] = LabelEncoder().fit_transform(df["Medical Condition"])
df["Admission Type"] = LabelEncoder().fit_transform(df["Admission Type"])
df["Test Results"] = LabelEncoder().fit_transform(df["Test Results"])

X = df[
    ["Age", "Gender", "Medical Condition",
     "Admission Type", "Test Results"]
]

y = df["Cost_Category"]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

importance.sort_values().plot(
    kind="barh",
    figsize=(8,5)
)

plt.title("Feature Importance")
plt.tight_layout()
plt.show()