from azure.iot.device import IoTHubDeviceClient

CONNECTION_STRING = "HostName=iotassethub.azure-devices.net;DeviceId=mylaptopSim;SharedAccessKey=DJRMo3f5oq3AdGjR/OdjkrEpbK8adRwB+P7VRTyAJlA="

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

try:
    client.connect()
    print("✅ Successfully connected to Azure IoT Hub!")
    client.disconnect()
except Exception as e:
    print("❌ Connection failed:", e)
