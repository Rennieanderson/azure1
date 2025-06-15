from azure.iot.device import IoTHubDeviceClient, Message
import json
import time
import random

# ✅ Replace with your actual connection string
CONNECTION_STRING = "HostName=iotassethub.azure-devices.net;DeviceId=mylaptopSim;SharedAccessKey=DJRMo3f5oq3AdGjR/OdjkrEpbK8adRwB+P7VRTyAJlA="

# Create client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

try:
    print("🔌 Connecting to IoT Hub...")
    client.connect()
    print("✅ Connected!")

    while True:
        # Generate fake sensor data
        data = {
           "deviceId": "myLaptopSim"
,
            "temperature": random.randint(65, 85),
            "humidity": round(random.uniform(30.0, 70.0), 2)
        }

        # Always use JSON dumps for Azure message body
        msg = Message(json.dumps(data))
        msg.content_encoding = "utf-8"
        msg.content_type = "application/json"

        print("📤 Sending message:", data)
        client.send_message(msg)

        # Add delay to avoid overloading the connection
        time.sleep(5)

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    print("🛑 Disconnecting...")
    client.disconnect()
