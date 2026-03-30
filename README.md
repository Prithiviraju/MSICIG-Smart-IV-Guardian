# MSICIG: Multispectral Smart IV Contamination & Infusion Guardian

An advanced IoT medical device that attaches to standard IV drip chambers. It uses 11-channel light spectroscopy, capacitive sensing, and edge AI to detect fluid contamination, expired medications, and fatal air embolisms in real-time, autonomously halting the infusion to save patient lives.

## Tech Stack
* **Hardware:** ESP32 Microcontroller, ams OSRAM AS7341 Spectrometer, Coplanar Capacitive Electrodes, Solenoid Valve.
* **Edge AI:** TinyML (Random Forest & XGBoost) deployed directly on the ESP32 for zero-latency shut-offs.
* **Cloud & Telemetry:** MQTT Protocol, Google Firebase for remote monitoring.

## Repository Structure
* `/hardware_esp32` - C++ code for sensor data acquisition and valve actuation.
* `/edge_ai` - Python scripts for training the Random Forest models and exporting to TinyML.
* `/cloud_backend` - Python bridge connecting MQTT telemetry to Google Firebase.
