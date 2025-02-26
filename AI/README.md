## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Generate Sensor Data:**
    ```sh
    python data/sensor_data_generator.py
    ```

2. **Run Demand Forecasting Model:**
    ```sh
    python models/demand_forecasting.py
    ```

3. **Run Delivery Route Optimization Model:**
    ```sh
    python models/delivery_route_optimization.py
    ```

4. **Run Food Spoilage Detection Model:**
    ```sh
    python models/food_spoilage_detection.py
    ```

5. **Start the Web Application:**
    ```sh
    python api/app.py
    ```

## Models

- **Demand Forecasting:** Uses LSTM to predict future demand based on historical data.
- **Delivery Route Optimization:** Uses graph algorithms to find the shortest path for delivery routes.
- **Food Spoilage Detection:** Uses a Random Forest Classifier to detect food spoilage based on sensor data.

## Web Application

The web application provides a user interface to visualize sensor data and predicted demand. Access it by navigating to `http://127.0.0.1:5000/` after starting the application.

## License

This project is licensed under the MIT License.