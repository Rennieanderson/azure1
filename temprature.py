import random
import time
import json
from azure.iot.device import IoTHubDeviceClient, Message

# Set up your connection string here (from the Azure IoT Hub Device Registry)
CONNECTION_STRING = "HostName=iotanderson.azure-devices.net;DeviceId=ac001;SharedAccessKey=r0046uqdwTp7zlveRm3Ssz/13d08ARd6IoUbK21oP0U="

# Initialize the IoT Hub client
def create_client():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

# Simulate temperature and humidity data
def generate_sensor_data():
    temperature = round(random.uniform(20.0, 30.0), 2)  # Random temperature between 20.0 and 30.0 degrees Celsius
    humidity = round(random.uniform(30.0, 60.0), 2)  # Random humidity between 30% and 60%
    return {"temperature": temperature, "humidity": humidity}

# Send data to Azure IoT Hub
def send_data_to_iot_hub(client):
    while True:
        # Generate data
        sensor_data = generate_sensor_data()
        # Convert the data into a JSON string
        message_data = json.dumps(sensor_data)
        message = Message(message_data)
        
        # Set message properties if needed
        message.content_type = "application/json"
        message.content_encoding = "utf-8"
        
        # Send the message to the IoT Hub
        print(f"Sending data: {sensor_data}")
        client.send_message(message)
        
        # Wait for 5 seconds before sending the next message
        time.sleep(5)

if __name__ == "__main__":
    try:
        # Create client and send data
        client = create_client()
        send_data_to_iot_hub(client)
    except KeyboardInterrupt:
        print("IoT data simulation stopped.")
