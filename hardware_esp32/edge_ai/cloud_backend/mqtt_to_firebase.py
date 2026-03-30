import paho.mqtt.client as mqtt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Initialize Firebase
cred = credentials.Certificate("firebase-service-account.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# MQTT Settings
MQTT_BROKER = "test.mosquitto.org" # Public broker for hackathon demo
MQTT_TOPIC = "msicig/hospital1/bed4/telemetry"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    print(f"Received telemetry: {payload}")
    
    try:
        data = json.loads(payload)
        # Push real-time data to Google Firestore
        db.collection('live_infusions').document('bed4').set(data)
        print("Data successfully synced to Firebase Dashboard.")
    except Exception as e:
        print(f"Error parsing data: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Starting MSICIG Cloud Bridge...")
client.connect(MQTT_BROKER, 1883, 60)
client.loop_forever()
