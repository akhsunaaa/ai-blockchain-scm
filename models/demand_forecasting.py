import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Generate dummy demand data
timestamps = pd.date_range(start="2024-01-01", periods=100, freq='D')
demand = np.random.randint(50, 200, size=(100,))  # Random demand values

# Convert to DataFrame
df = pd.DataFrame({"timestamp": timestamps, "demand": demand})

# Scale the data
scaler = MinMaxScaler()
df["demand_scaled"] = scaler.fit_transform(df[["demand"]])

# Create training sequences
X, y = [], []
for i in range(len(df) - 10):
    X.append(df["demand_scaled"].iloc[i:i+10].values)
    y.append(df["demand_scaled"].iloc[i+10])

X, y = np.array(X), np.array(y)

# Build LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(10, 1)),
    LSTM(50),
    Dense(1)
])
model.compile(optimizer="adam", loss="mse")

# Train the model
model.fit(X, y, epochs=20, batch_size=8)

# Predict future demand
predicted_demand = model.predict(X[-1].reshape(1, 10, 1))

print(f"Predicted Demand: {scaler.inverse_transform(predicted_demand)[0][0]}")
