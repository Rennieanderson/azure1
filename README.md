**Project Title**
Azure IoT Real-Time Sensor Monitoring System

**Project Description**
This project showcases a real-time IoT data streaming application using Microsoft Azure IoT Hub.
It provides a simulation of IoT sensor data like temperature and humidity, transmits the data to Azure IoT Hub, and shows the real-time data on a Node.js WebSocket server.
The application assists in real-time environmental monitoring of devices/assets.

**Features**

* Real-time IoT data simulation (temperature & humidity)

* Secure connection with Azure IoT Hub

*Continuous streaming of device telemetry

*Live data broadcast using WebSockets

*Ready for dashboard visualization (Grafana / Web UI)

** Project Architecture**

IoT Device Simulator (Python)
        ↓
Azure IoT Hub
        ↓
Event Hub (built-in endpoint)
        ↓
Node.js Server (WebSocket)
        ↓
Web Dashboard / Clients

****Technologies Used****

*Python
*Azure IoT Hub]
*WebSocket (ws)
*JSON

**** Project Structure****
azure1-main/
│
├── iot_script.py        # IoT data simulation script
├── temprature.py        # Temperature & humidity simulator
├── test_connection.py   # Test Azure IoT Hub connection
├── server.js            # Node.js WebSocket server
├── scripts/
│   └── event-hub-reader.js
├── public/              # Frontend files (if any)
└── README.md

**** Setup Instructions****
1️ Clone the Repository
git clone https://github.com/your-username/azure-iot-project.git
cd azure-iot-project

2️ Install Python Dependencies
pip install azure-iot-device

3️ Configure Azure IoT Device Connection
Open the file:

iot_script.py

Replace:

CONNECTION_STRING = "Your_Device_Connection_String"

4️ Test IoT Hub Connection
python test_connection.py

Expected output:

 Successfully connected to Azure IoT Hub!
 
5️ Run IoT Data Simulator
python iot_script.py

This will start sending data like:

{
  "temperature": 75,
  "humidity": 45.6
}

6️ Setup Node.js Backend

Install dependencies:

npm install

Set environment variables:

export IotHubConnectionString="Your_IoT_Hub_Connection_String"
export EventHubConsumerGroup="$Default"

7️ Start Server
node server.js

Output:

Listening on 3000

8️ View Live Data

Open browser:

http://localhost:3000

You will see real-time IoT data streaming.
Sample Output
Sending message: {'temperature': 78, 'humidity': 55.2}
Broadcasting data {"temperature":78,"humidity":55.2}

****Use Cases****

Smart Water Management System

Smart Home Monitoring

Industrial Equipment Monitoring

Environmental Monitoring

Asset Utilization Tracking

****Future Enhancements****

* Grafana dashboard integration

* Geo-location tracking of devices

* Alert system (email/SMS)

* Data storage using Azure Cosmos DB

* ML-based prediction system

  License

This project is for academic and learning purposes.

****Conclusion****

This project provides a complete end-to-end pipeline for IoT data collection, processing, and visualization using Azure Cloud services, making it ideal for real-time monitoring applications.
