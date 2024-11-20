# Safe Drive: An ML-Powered Driver Safety System

Safe Drive is an advanced machine learning-powered system designed to ensure driver safety and enhance the driving experience. This comprehensive solution integrates multiple AI-driven models, each tailored to address specific aspects of driver safety and personalization.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Models Implemented](#models-implemented)
4. [How to Use](#how-to-use)


---

## Introduction

Driving can be dangerous due to various factors such as distractions, drowsiness, or poor visibility. Safe Drive combines state-of-the-art AI and machine learning techniques to address these challenges, providing real-time alerts and assistance to drivers. The system is modular, allowing flexibility and scalability for future enhancements.

---

## Features

- **Voice Authentication:** Secure authentication of drivers using voice biometrics.
- **Facial Recognition:** Identify and authenticate drivers to personalize the driving experience.
- **Speech Recognition:** Enable voice-activated commands for hands-free operation.
- **Drowsiness Detection:** Prevent accidents by monitoring driver alertness and providing timely alerts.
- **Object Detection and Navigation:** Detect objects on the road to assist in navigation and obstacle avoidance.
- **Low Light Vision:** Enhance visibility in low-light or nighttime conditions.
- **Traffic Sign Detection:** Recognize and alert drivers about traffic signs in real time.

---

## Models Implemented

Each of the following models is stored in its own folder, with a dedicated `README.md` file explaining the procedure to set up, run, and utilize the model:

1. **Voice Authentication**  
   - Verifies the driver's identity using voice samples.  
   - Folder: `Voice_Authentication/`

2. **Facial Recognition**  
   - Recognizes the driver's face for personalization and security.  
   - Folder: `Facial_Recognition/`

3. **Speech Recognition**  
   - Converts spoken commands into actionable inputs for the system.  
   - Folder: `Speech_Recognition/`

4. **Drowsiness Detection**  
   - Detects signs of driver fatigue using live video analysis.  
   - Folder: `Drowsiness_Detection/`

5. **Object Detection and Navigation**  
   - Identifies obstacles and assists in route navigation.  
   - Folder: `Object_Detection_And_Navigation/`

6. **Low Light Vision**  
   - Improves visibility during nighttime or low-light conditions.  
   - Folder: `Low_Light_Vision/`

7. **Traffic Sign Detection**  
   - Detects and interprets traffic signs to assist drivers.  
   - Folder: `Traffic_Sign_Detection/`

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/safe-drive.git
   cd safe-drive
