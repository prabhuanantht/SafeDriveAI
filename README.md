### Qualcomm VisionX Hackathon Submission - Team ID: Qual-230310
---
# Safe Drive: An ML-Powered Driver Assistance System

**Safe Drive** is a next-generation machine learning system that transforms the driving experience. Our project addresses the growing need for **enhanced safety, luxury, and automation** in modern vehicles, leveraging intelligent systems to provide a safer, more connected driving experience.  

This vision aligns with **Qualcomm’s leadership in automotive AI** through their **Snapdragon Ride™** and **Snapdragon Elite™ platforms**, paving the way for smarter, connected cars. **Inspired by [this blog](https://www.qualcomm.com/news/onq/2019/02/artificial-intelligence-transforming-automotive-industry)**, Safe Drive integrates cutting-edge AI models to enhance the overall driving experience.

---

## 🔎 **What is Safe Drive?**

Driving isn't just about reaching your destination; it's about **how safely and comfortably you get there**. With Safe Drive, we’ve integrated advanced AI models to tackle challenges like **drowsiness detection**, **low-light driving**, and **voice-based automation**, creating a system that truly cares for the driver.

💡 **Built for Real Needs**: Modular design for enhanced flexibility and future updates.  
💡 **AI at Its Core**: Real-time detection, prediction, and decision-making powered by cutting-edge models.


---

https://github.com/user-attachments/assets/b917335f-30c1-4a05-b59b-e4e6c43d2690

Download the video from the drive: https://drive.google.com/file/d/16CmlSPQNxpy2xsP9rfr9S4vJ3fG4EAB5/view?usp=sharing

---

## 🎯 **Key Features**

Safe Drive integrates multiple AI models, many of which rely on **object detection** to ensure safety and performance. Below is an overview of its features and how object detection is utilized:

### 1. **Voice Authentication** 🗣  
   - 🔒 Verifies the driver using voice biometrics.  
   - **Object Detection**: Uses **feature detection** to identify unique voice patterns.  
   - **Feature Extraction**: MFCC for unique audio characteristics.  
   - **Model**: Siamese Network with a **ResNet-18 backbone** and attention mechanism for one-shot learning.  
   - 📁 Folder: `Voice_Authentication/`  

### 2. **Facial Recognition** 🧑‍💻  
   - 👤 Recognizes the driver and opens a personalized profile built with **Django** and frontend languages.  
   - **Object Detection**: Detects the driver’s face using a **KNN-based recognition system**.  
   - 📁 Folder: `Facial_Recognition/`  

### 3. **Speech Recognition** 🎤  
   - 🗨 Allows hands-free operation through voice commands.  
   - **Feature Extraction**: Embeddings generated via **Word2Vec**.  
   - 📁 Folder: `Speech_Recognition/`  

### 4. **Drowsiness Detection** 😴  
   - 🛡 Prevents fatigue-related accidents using live video analysis.  
   - **Object Detection**: Detects eyes and facial features with **YOLOv5** for real-time fatigue assessment.  
   - 📁 Folder: `Drowsiness_Detection/`  

### 5. **Object Detection and Navigation** 🚗  
   - 🚧 Identifies obstacles and assists in route navigation.  
   - **Model**: Built with **YOLOv5** for robust and accurate object detection.  
   - 📁 Folder: `Object_Detection_And_Navigation/`  

### 6. **Low Light Vision** 🌙  
   - 🌌 Enhances visibility during nighttime or low-light conditions.  
   - **Model**: Uses the **MIRNet model from Hugging Face** for low-light image enhancement.  
   - 📁 Folder: `Low_Light_Vision/`  

### 7. **Traffic Sign Detection** 🚦  
   - ⚠ Recognizes and interprets road signs in real time.  
   - **Object Detection**: Utilizes **YOLOv5** for high-speed detection of traffic signs.  
   - 📁 Folder: `Traffic_Sign_Detection/`  

---

## 📊 **Model Performance**

Each model has been rigorously tested to ensure reliability in real-world scenarios. Below are the models with their respective architectures and accuracies:

| **Feature**                | **Model/Architecture**                                     | **Accuracy** |
|----------------------------|----------------------------------------------------------|--------------|
| Voice Authentication       | Siamese Network (ResNet-18 Backbone + Attention)         | 82%          |
| Facial Recognition         | KNN-based System                                        | 96%          |
| Speech Recognition         | Word2Vec Embeddings                                    | 92.5%          |
| Drowsiness Detection       | YOLOv5                                                 | 90%          |
| Object Detection & Navigation | YOLOv5                                                 | 89.5%          |
| Low Light Vision           | MIRNet from Hugging Face                               | 75% clearence          |
| Traffic Sign Detection     | YOLOv5                                                 | 96%          |


---

## 🛠 **How to Use**

### **Clone the Repository**
```bash
git clone https://github.com/prabhuanantht/SafeDriveAI.git
cd SafeDriveAI
```
Further steps are explained inside the folders of each model.
## ⚡ **Performance Metrics and Efficiency**

### 🖥️ **Code Efficiency**
- **Resource Usage**:
  - Memory: ~3-4GB RAM
  - Disk Space: ~24GB for training
- **Training Time**:
  - On **Google Colab TPU**: ~20-30 minutes for 10 epochs
- **Inference Speed**:
  - ~5-10ms per file for most modules
  - Maximum latency: ~10 seconds during complex inference  

### 🎯 **Accuracy & Precision**
- Performance measured using:
  - **Precision**: Ensures correct predictions for minimal errors.
  - **Recall**: Effectively captures true positives in predictions.
  - **SSIM (Structural Similarity Index)**: Evaluates the quality of image enhancements in models like Low Light Vision.
  - **PSNR (Peak Signal-to-Noise Ratio)**: Measures the image enhancement performance to ensure high-quality outputs.

### 🚀 **Execution Speed**
- Designed for **real-time processing**:
  - Object detection and navigation systems achieve **latency under 10ms** per frame.
  - Driver authentication systems respond in less than **1 second**.

### 🛡️ **Robustness & Generalization**
- Trained on a **diverse, large-scale dataset**, enabling:
  - High adaptability to real-world scenarios.
  - Effective handling of various environmental conditions, such as low light, cluttered backgrounds, and diverse driver profiles.

### 💡 **Innovativeness**
- Combines multiple cutting-edge models to enhance:
  - **Driver safety**: Prevent accidents with proactive alerts.
  - **Automation**: Hands-free operation with advanced speech and object recognition.
  - **Luxury**: Personalized profiles, voice authentication, and intelligent vision systems.

### 🌐 **Scalability**
- Scalable design to support:
  - **Larger datasets** with increased computational resources.
  - Integration with future AI-powered features for next-gen automotive tech.
