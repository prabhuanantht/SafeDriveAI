
# Real-Time Drowsiness Detection System

A safety technology designed to prevent accidents caused by drowsy driving. This project implements a real-time drowsiness detection system using computer vision to monitor driver alertness via a live video stream and alerts users with an alarm notification when drowsiness is detected.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Motivation](#motivation)
3. [Built With](#built-with)
4. [Getting Started](#getting-started)
5. [Running the Application](#running-the-application)
6. [Algorithm](#algorithm)
7. [Testing and Results](#testing-and-results)
8. [Future Scope](#future-scope)
9. [References](#references)

---

## Introduction

This project aims to reduce road accidents caused by drowsy driving by developing a system that detects drowsiness in real-time using computer vision techniques and alerts drivers.

## Motivation

According to the National Highway Traffic Safety Administration, approximately 100,000 police-reported crashes involve drowsy driving annually, leading to over 1,550 fatalities and 71,000 injuries. The real number may be higher due to difficulty in determining drowsiness. This project seeks to address this issue by detecting and alerting drowsy drivers.

## Built With

- **OpenCV**: High-performance library for real-time image processing.
- **imutils**: Utilities to simplify working with OpenCV.
- **Dlib**: Advanced computer vision and machine learning library.
- **scikit-learn**: Machine learning tools in Python.
- **NumPy**: Fundamental package for scientific computing in Python.

## Getting Started

To set up the project locally for development and testing:

1. Install Python 3.
2. Install `cmake` on your system.

## Running the Application

1. Navigate to the project directory:
    ```bash
    cd Real-Time-Drowsiness-Detection-System
    ```
2. (Optional) Use a virtual environment:
    - Install `virtualenv`:
      ```bash
      pip install virtualenv
      ```
    - Create the environment:
      ```bash
      virtualenv -p python3 test_env
      ```
    - Activate the environment:
      - On Windows:
        ```bash
        test_env\Scripts\Activate
        ```
      - On Unix:
        ```bash
        source test_env/bin/activate
        ```
3. Install dependencies from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
4. Install the `dlib` library:
    - On Unix, follow specific installation guides if issues arise.
    - On Windows, ensure `cmake` is installed and restart the terminal.
5. Run the application:
    ```bash
    python Real-Time-Drowsiness-Detection-System.py --shape-predictor shape_predictor_68_face_landmarks.dat --alarm Alert.wav
    ```

## Algorithm

1. Capture the driver’s image via camera.
2. Detect the face using the Haarcascade classifier.
    - If no face is detected, sound the alarm.
3. Detect eyes from the cropped face image.
    - If no eyes are detected, sound the alarm.
4. Analyze eye images using Hough transformations to determine whether they are open or closed.
5. If both eyes are closed for five consecutive frames, sound the alarm to alert the driver.

## Testing and Results

The system was tested under various conditions:

1. **Ambient Lighting**: Successfully detected face and eyes under adequate lighting.
2. **Driver's Position**:
    - Center, Left, and Right: Successfully detected drowsiness.
3. **Wearing Spectacles**: Successfully detected drowsiness.
4. **Head Tilt**: Detection failed when the driver’s head was tilted beyond 30 degrees.

### Real-World Testing

The system was tested in real-world scenarios with a camera placed on a car visor focusing on the driver. Results were positive unless direct light obscured the camera.

## Future Scope

- **Mobile Application**: Implementation as a smartphone app, enabling drivers to use the system via their phone's camera.

## References

1. *Facial Features Monitoring for Real-Time Drowsiness Detection*. 2016 International Conference on Innovations in Information Technology.
2. *Real-Time Drowsiness Detection Using Eye Blink Monitoring*. 2015 National Software Engineering Conference (NSEC 2015).

### Useful Resources
- [Real-Time Eye Tracking](https://www.codeproject.com/Articles/26897/TrackEye-Real-Time-Tracking-Of-Human-Eyes)
- [Face Detection with OpenCV](https://docs.opencv.org/3.4/d7/d8b/tutorial_py_face_detection.html)
- [Training Haar Cascade Detectors](https://www.learnopencv.com/training-better-haar-lbp-cascade-eye-detector-opencv/)
