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
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [License](#license)

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

3. **Add Pre-trained Model**
   Ensure the `face_authentication_model.pkl` file is in the project directory.

## 🚀 Usage

1. **Prepare an Input Image**
   Place an image in the project directory, e.g., `mypic.jpg`.

2. **Run the Authentication Script**
   Execute `facerec.py` with the required paths:
   ```bash
   python facerec.py
   ```
   - The script allows you to specify paths for `model_path` and `image_path`.

3. **View Results**
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
pip install face_recognition joblib numpy opencv-python matplotlib
```

## 🔧 Configuration

- **Model Path**: Modify `model_path` in `facerec.py` to point to the KNN model file.
- **Image Path**: Update `image_path` to specify the location of your input image file.
- **Threshold Adjustment**: Adjust the `threshold` parameter in `predict_identity` for tuning authentication sensitivity.

## 🛠 Troubleshooting

- **Model Not Loading**: Verify the file path for the KNN model file.
- **No Faces Detected**: Ensure that the input image contains visible faces; consider adjusting lighting or resolution.
- **Misidentification**: Tweak the `threshold` to balance authentication accuracy.

## 🌱 Future Enhancements

- **Real-Time Video Authentication**: Expand functionality to allow face authentication in live video streams.
- **Optimized Model Training**: Incorporate additional encodings and improve KNN model accuracy.
- **Web or Mobile Interface**: Develop a web or mobile app for broader accessibility.

## 📝 License

This project is licensed under the MIT License – see the `LICENSE` file for details.

---

This template should make your project accessible, clear, and professional for hackathon reviewers and contributors. Let me know if you'd like more customization!
