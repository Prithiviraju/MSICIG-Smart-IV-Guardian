import numpy as np
from sklearn.ensemble import RandomForestClassifier
from micromlgen import port # Used to convert sklearn models to C++

# Simulated Dataset: 11-Channel Spectral Data
# Columns: F1, F2, F3, F4, F5, F6, F7, F8, Clear, NIR
# Target: 0 (Pure Saline), 1 (Contaminated/Turbid), 2 (Expired)

print("Loading spectral dataset...")
# X represents the raw AS7341 sensor readings
X = np.random.rand(1000, 10) * 65535 
# y represents the classification labels
y = np.random.randint(0, 3, 1000)    

print("Training Random Forest Classifier...")
clf = RandomForestClassifier(n_estimators=20, max_depth=5, random_state=42)
clf.fit(X, y)

accuracy = clf.score(X, y)
print(f"Model Training Complete. Accuracy: {accuracy * 100:.2f}%")

# Exporting the model to C++ for the ESP32 (TinyML)
print("Exporting model to ESP32 header file...")
c_code = port(clf)

with open('RandomForestModel.h', 'w') as f:
    f.write(c_code)

print("Successfully generated RandomForestModel.h for Edge Deployment.")
