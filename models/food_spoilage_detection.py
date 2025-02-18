import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
   
# Load sensor data
df = pd.read_csv("data/sensor_data.csv")

# Label spoilage based on ethylene level
df["spoilage"] = df["ethylene"].apply(lambda x: 1 if x > 2.0 else 0)

# Features
X = df[["temperature", "humidity", "ethylene"]]
y = df["spoilage"]

# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train a Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_scaled, y)

# Predict spoilage
df["spoilage_pred"] = model.predict(X_scaled)

print(df[["temperature", "humidity", "ethylene", "spoilage_pred"]].head())
