# CPSTemperatureApp

The **Temperature Regulation Application** is a dummy service designed to simulate an edge device for edge computing scenarios. It generates random temperature measurements from multiple sources at regular intervals and provides APIs for interaction and configuration.

---

## Features

- Simulates random temperature measurements from multiple sources (e.g., transformers, substations) every 10 minutes by default.
- Allows the user to adjust the measurement interval (5–30 minutes) via a REST API.
- Stores all generated measurements in a local JSON file for persistence.
- Provides RESTful APIs to:
  - Retrieve all temperature measurements.
  - Update the frequency of temperature measurements.

---

## API Endpoints

### 1. **Fetch All Measurements**
- **Endpoint**: `/measurements`
- **Method**: `GET`
- **Description**: Returns all recorded temperature measurements.
- **Response Example**:
  ```json
  [
    {
      "source": "Transformer A",
      "temperature": 35.25,
      "timestamp": "2025-01-01 10:00:00"
    },
    {
      "source": "Transformer B",
      "temperature": 28.75,
      "timestamp": "2025-01-01 10:00:00"
    }
  ]
  ```

---

### 2. **Adjust Measurement Frequency**
- **Endpoint**: `/settings/frequency`
- **Method**: `POST`
- **Description**: Updates the interval (in minutes) at which temperature measurements are generated.
- **Request Body**:
  ```json
  {
    "frequency": 15
  }
  ```
- **Response Example**:
  ```json
  {
    "message": "Frequency updated to 15 minutes"
  }
  ```

---

### 3. **Get Current Frequency**
- **Endpoint**: `/settings`
- **Method**: `GET`
- **Description**: Returns the current measurement frequency in minutes.
- **Response Example**:
  ```json
  {
    "frequency": 15
  }
  ```

---

## Local Setup

### Prerequisites
- **Python 3.9+**
- **Flask**

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the application at `http://localhost:5000`.

---

## Docker Setup

### Build the Docker Image
```bash
docker build -t temperature-regulation-app .
```

### Run the Docker Container
```bash
docker run -d -p 5000:5000 --name temp-reg-app temperature-regulation-app
```

### Interact with the Application
Use any API client (e.g., `curl`, Postman, or your browser) to interact with the application. For example:
- Fetch measurements:  
  ```bash
  curl http://localhost:5000/measurements
  ```
- Adjust frequency:  
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"frequency": 15}' http://localhost:5000/settings/frequency
  ```

---

## File Structure

```
.
├── app.py                # Application source code
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker build instructions
└── README.md             # Documentation
```

---

## Notes
- The application generates and stores temperature measurements in a local file called `data.json` for persistence.
- Measurements simulate realistic temperature ranges for medium voltage areas (20°C–45°C).
- Measurement sources include transformers and substations.

---

## License
This project is for demonstration purposes and does not include a license.
