from flask import Flask, jsonify, request # type: ignore
import threading
import time
import random
import json

app = Flask(__name__)

# Data storage
data_file = "data.json"
default_frequency = 10  # in minutes
measurement_frequency = default_frequency
measurements = []

# Simulated temperature sources
sources = ["Transformer A", "Transformer B", "Substation 1", "Substation 2"]

# Load data from file
def load_data():
    global measurements
    try:
        with open(data_file, "r") as f:
            measurements.extend(json.load(f))
    except FileNotFoundError:
        measurements = []

# Save data to file
def save_data():
    with open(data_file, "w") as f:
        json.dump(measurements, f)

# Generate random temperature measurements
def generate_measurements():
    while True:
        global measurement_frequency
        new_measurements = []
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        for source in sources:
            temperature = round(random.uniform(20, 45), 2)  # Reasonable medium voltage temperatures
            new_measurements.append({"source": source, "temperature": temperature, "timestamp": timestamp})
        measurements.extend(new_measurements)
        save_data()
        time.sleep(measurement_frequency * 60)

# Background thread to simulate measurements
def start_measurement_thread():
    thread = threading.Thread(target=generate_measurements)
    thread.daemon = True
    thread.start()

@app.route("/measurements", methods=["GET"])
def get_measurements():
    """Fetch all recorded measurements."""
    return jsonify(measurements), 200

@app.route("/settings/frequency", methods=["POST"])
def set_frequency():
    """Set measurement frequency (in minutes)."""
    global measurement_frequency
    try:
        data = request.json
        new_frequency = int(data.get("frequency"))
        if 5 <= new_frequency <= 30:
            measurement_frequency = new_frequency
            return jsonify({"message": f"Frequency updated to {new_frequency} minutes"}), 200
        else:
            return jsonify({"error": "Frequency must be between 5 and 30 minutes"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid frequency value"}), 400

@app.route("/settings", methods=["GET"])
def get_settings():
    """Get the current measurement frequency."""
    return jsonify({"frequency": measurement_frequency}), 200

if __name__ == "__main__":
    load_data()
    start_measurement_thread()
    app.run(host="0.0.0.0", port=5000)