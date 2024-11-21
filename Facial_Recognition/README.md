# Face Authentication Model 🧑‍🤝‍🧑 | Hackathon Project Submission

Welcome to the **Face Authentication Model**, that leverages the power of the K-Nearest Neighbors (KNN) algorithm to identify faces in images. Using a trained classifier, this project efficiently matches input images with known faces, making face authentication accessible and accurate.

## 📜 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Future Enhancements](#future-enhancements)

## 🔍 About the Project

The **Face Authentication Model** identifies and labels faces in images by comparing them with a database of known face encodings. This project employs the `face_recognition` library to generate encodings and uses a KNN classifier for rapid and accurate predictions.

## ✨ Features

- **Real-Time Face Detection**: Quickly detects faces within input images.
- **KNN-Based Authentication**: Uses KNN to classify and label detected faces against a set of known face encodings.
- **Visual Output**: Displays the image with bounding boxes around recognized faces and labels for easy identification.

## 🎥 Demo

Coming soon! (Consider adding a GIF or video here to show the project in action.)

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/prabhuanantht/SafeDriveAI.git
   cd SafeDriveAI/Facial_Recognition
   ```

2. **Install Required Dependencies**
   Install dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```


## 🚀 Usage

1. **Prepare an Input Image**
   Place the training set images in a folder in the path `face-recognition-dataset/Original Images/Original Images`

2. **Run the Authentication Script**
   Execute `train_face_auth.py` with the required paths for training:
   ```bash
   python train_face_auth.py
   ```
   
3. **Set the model path and run the `test_cam_live.py` to recognise the face:
  ```bash
   python test_cam_live.py
   ```

4. **View Results**
   The output displays the image with bounding boxes around detected faces, labeled with the recognized identities.

## 🧩 Dependencies

The project requires the following Python packages:
- `face_recognition`
- `joblib`
- `numpy`
- `opencv-python`
- `matplotlib`

To install them, run:
```bash
pip install -r requirements.txt
```

## 🔧 Configuration

- **Dataset Path**: Modify `DIR_PATH` in `train_face_auth.py` to point to the Dataset folder.
- **Model Path**: Update `model` in `test_cam_live.py` to specify the location of your trained model.
- **Threshold Adjustment**: Adjust the `threshold` parameter in `predict_identity` for tuning authentication sensitivity.


## 🌱 Future Enhancements

- **Real-Time Video Authentication**: Expand functionality to allow face authentication in live video streams.
- **Optimized Model Training**: Incorporate additional encodings and improve KNN model accuracy.
- **Web or Mobile Interface**: Develop a web or mobile app for broader accessibility.

