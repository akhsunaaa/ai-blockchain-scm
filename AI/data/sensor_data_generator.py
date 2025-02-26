import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate timestamps
start_time = datetime.now()
timestamps = [start_time + timedelta(minutes=5 * i) for i in range(100)]

# Generate random sensor values
temperature = np.random.uniform(20, 40, 100)
humidity = np.random.uniform(40, 80, 100)
ethylene = np.random.uniform(0.5, 3.0, 100)  # Ethylene gas (for fruit ripeness)
latitude = np.linspace(19.0760, 19.2000, 100)
longitude = np.linspace(72.8777, 73.0000, 100)

# Create DataFrame
sensor_data = pd.DataFrame({
    "timestamp": timestamps,
    "temperature": temperature,
    "humidity": humidity,
    "ethylene": ethylene,
    "latitude": latitude,
    "longitude": longitude
})

# Save to CSV
sensor_data.to_csv("data/sensor_data.csv", index=False)

print("Sensor data saved as 'data/sensor_data.csv'")
