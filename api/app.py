from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
@app.route('/')
def home():
    return "Flask app is running!"

@app.route('/get-sensor-data', methods=['GET'])
def get_sensor_data():
    df = pd.read_csv("data/sensor_data.csv")
    return jsonify(df.to_dict())

@app.route('/predict-demand', methods=['GET'])
def predict_demand():
    return jsonify({"predicted_demand": 150})

if __name__ == '__main__':
    app.run(debug=True)