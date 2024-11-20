import os
import cv2
import numpy as np
import joblib
from pathlib import Path
import face_recognition
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from itertools import chain
# Path to the dataset
DIR_PATH = 'final_face_auth_py/face-recognition-dataset/Original Images/Original Images'

def create_dataset(dir_path):
    X, y = [], []
    for subdir in os.listdir(dir_path):
        full_path = os.path.join(dir_path, subdir)
        if os.path.isdir(full_path):
            for img_path in chain(Path(full_path).glob('*.jpg'), Path(full_path).glob('*.jpeg')):
                img = face_recognition.load_image_file(str(img_path))
                face_locations = face_recognition.face_locations(img)
                
                # Process images with exactly one face
                if len(face_locations) == 1:
                    encoding = face_recognition.face_encodings(img, face_locations)[0]
                    X.append(encoding)
                    y.append(subdir)
    return X, y

# Load dataset and split into train-test sets
X, y = create_dataset(DIR_PATH)
print(f"Total samples: {len(X)}")
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the KNN classifier
model = KNeighborsClassifier(n_neighbors=1, weights='distance')
model.fit(x_train, y_train)
print("Model trained successfully.")

# Evaluate the model
y_pred = model.predict(x_test)
print(classification_report(y_test, y_pred))

# Save the model to a file
MODEL_PATH = 'final_knn_face_recognition_model.pkl'
joblib.dump(model, MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")
