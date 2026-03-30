#include <Wire.h>
#include <Adafruit_AS7341.h>
#include <WiFi.h>
#include <PubSubClient.h>

Adafruit_AS7341 as7341;

// Pin Definitions
const int SOLENOID_PIN = 4;      // Relay for the shut-off valve
const int CAPACITIVE_PIN = T0;   // Built-in ESP32 touch pin for bubble detection
const int PPG_PIN = 34;          // Analog pin for pulse sensor

// Thresholds
const int BUBBLE_THRESHOLD = 20; // Capacitance drop indicating air
int touchValue;

void setup() {
  Serial.begin(115200);
  pinMode(SOLENOID_PIN, OUTPUT);
  digitalWrite(SOLENOID_PIN, LOW); // Valve open by default

  if (!as7341.begin()){
    Serial.println("Could not find AS7341 sensor!");
    while (1) { delay(10); }
  }
  
  as7341.setATIME(100);
  as7341.setASTEP(999);
  as7341.setGain(AS7341_GAIN_256X);
}

void loop() {
  // 1. Read Spectral Data (Fluid Quality)
  uint16_t readings[12];
  if (!as7341.readAllChannels(readings)){
    Serial.println("Error reading spectrometer!");
  }
  
  // 2. Read Capacitive Sensor (Air Bubble Detection)
  touchValue = touchRead(CAPACITIVE_PIN);
  
  // 3. Read PPG Pulse (Hemodynamic status)
  int ppgValue = analogRead(PPG_PIN);

  // 4. Edge AI / Logic Actuation
  // If air bubble detected or spectral anomaly (simulated ML trigger)
  if (touchValue < BUBBLE_THRESHOLD || readings[1] > 5000) { 
    digitalWrite(SOLENOID_PIN, HIGH); // CLOSE VALVE IMMEDIATELY
    Serial.println("EMERGENCY: Valve Closed! Anomaly Detected.");
  }

  // TODO: Add MQTT Publish logic here to send readings array to Firebase
  
  delay(1000); 
}
