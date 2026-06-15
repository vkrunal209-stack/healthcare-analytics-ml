import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_excel(
    r"C:\Users\vkrun\OneDrive\Desktop\healthcare-analytics-ml\data\healthcare_dataset.csv.xlsx"
)

# Check billing amount range
print("Minimum Billing Amount:", df["Billing Amount"].min())
print("Maximum Billing Amount:", df["Billing Amount"].max())

# Create Cost Category
df["Cost_Category"] = pd.cut(
    df["Billing Amount"],
    bins=[-999999999, 10000, 30000, 999999999],
    labels=["Low", "Medium", "High"]
)

# Remove blanks if any
df = df.dropna(subset=["Cost_Category"])

# Encode text columns
gender_encoder = LabelEncoder()
condition_encoder = LabelEncoder()
admission_encoder = LabelEncoder()
result_encoder = LabelEncoder()

df["Gender"] = gender_encoder.fit_transform(df["Gender"])
df["Medical Condition"] = condition_encoder.fit_transform(df["Medical Condition"])
df["Admission Type"] = admission_encoder.fit_transform(df["Admission Type"])
df["Test Results"] = result_encoder.fit_transform(df["Test Results"])

# Features
X = df[
    [
        "Age",
        "Gender",
        "Medical Condition",
        "Admission Type",
        "Test Results"
    ]
]

# Target
y = df["Cost_Category"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Train Model
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
print("\nTarget Distribution:")
print(y.value_counts())
# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")