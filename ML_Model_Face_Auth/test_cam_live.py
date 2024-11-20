import cv2
import face_recognition
import joblib
import numpy as np

# Load pre-trained model and face detection
model = joblib.load('/Users/ananth/Coding/Qualcomm/ML_Model_Face_Auth/final_knn_face_recognition_model.pkl')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def predict_identity(face_img, model, threshold=0.6):
    rgb_image = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb_image)

    if not encodings:
        return "No face detected"
    
    encoding = encodings[0]
    distances, _ = model.kneighbors([encoding], n_neighbors=1)
    return model.predict([encoding])[0] if distances[0][0] <= threshold else "Unknown"

# Webcam logic
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        name = predict_identity(face_img, model)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        print(f"Recognized: {name}")
        cap.release()
        cv2.destroyAllWindows()

    cv2.imshow("Webcam Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



#######################################################################################
# FETCHING DATA FROM DJANGO API AND AUTHENTICATING USERS USING FACE RECOGNITION MODEL #
#######################################################################################

import requests

# Simulated result from face recognition
user_name = name
if not user_name.strip():
    print("Error: User name is empty. Cannot send request.")
if user_name == "No face detected":
    print("No face detected, skipping API request.")
else:
    try:
        # Send POST request to the Django API
        print("Sending name:", user_name)
        response = requests.post(
            "http://127.0.0.1:8000/api/profiles/",
            json={"name": user_name}
        )
        
        # Handle the response
        if response.status_code == 201:
            print("Profile created successfully:", response.json())
        elif response.status_code == 400:
            print("Validation error:", response.json())  # Specific error message
        else:
            print("Unexpected error:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
exit()