# **Secure Voice Authentication System for Automotive Applications**

## **Overview**
This project introduces a **Voice Authentication System** tailored for automotive environments, ensuring seamless and secure driver identification. Designed with **One-Shot Learning**, it uses a **ResNet-18 Backbone** combined with an **Attention Mechanism** to enhance feature extraction and focus on relevant audio signals, enabling highly accurate speaker verification.

This system paves the way for advanced car security and personalization by using biometric authentication to unlock, start, and adjust vehicle settings without manual intervention.

---

## **Key Features**
### **ResNet-18 Backbone**
- Employs ResNet-18 for robust feature extraction from audio signals.
- Uses residual connections to retain detailed features while preventing vanishing gradients.
- Ensures efficient and accurate processing of **MFCC** features.

### **Attention Mechanism**
- Integrates an attention module to dynamically prioritize the most relevant features.
- Enhances the system’s ability to focus on speaker-specific audio patterns.
- Reduces noise interference in challenging environments, like inside a moving car.

### **Comprehensive Workflow**
- **Speaker Enrollment**: Captures and stores unique voice embeddings during registration.
- **Speaker Verification**: Authenticates users by comparing real-time audio input with stored embeddings using similarity scores.
- **Threshold-Based Decisions**: Securely identifies speakers by setting an optimal similarity score threshold.

### **Real-World Applications**
1. **Automotive Security**:  
   - Prevents unauthorized access.  
   - Offers a seamless and secure alternative to physical keys.  

2. **Driver Personalization**:  
   - Automatically adjusts seat positions, music preferences, and climate control based on the authenticated driver.

3. **Biometric Access Control**:  
   - Enables voice-based authentication for offices, homes, and restricted areas.

---

## **How It Works**

### **1. Preprocessing Audio Signals**
- **Voice Activity Detection (VAD)**: Removes silence and background noise for clean audio input.
- **Resampling**: Converts audio signals to a consistent sampling rate of 16 kHz.
- **Feature Extraction**: Computes **Mel-Frequency Cepstral Coefficients (MFCCs)** as input for the deep learning model.

### **2. Neural Network Architecture**
#### **ResNet-18 with Attention**
- ResNet-18 processes MFCC features through a deep, residual network to learn hierarchical representations.
- Attention layers enhance the focus on speaker-specific features, reducing the impact of irrelevant signals.

#### **Siamese Neural Network**
- Compares three inputs:  
  - **Anchor**: Reference sample of the target speaker.  
  - **Positive**: Another sample from the same speaker.  
  - **Negative**: A sample from a different speaker.  
- Outputs similarity scores between pairs using **Triplet Loss** to maximize inter-speaker differences and minimize intra-speaker variations.

### **3. Authentication Flow**
1. **Enrollment**: Captures user audio and stores embeddings.
2. **Verification**: Compares real-time audio with stored embeddings:
   - Computes similarity scores using **cosine similarity** or **Euclidean distance**.
   - Verifies identity by comparing the score with a predefined threshold.

---

## **Implementation Details**
### **Technology Stack**
- **Programming Language**: Python
- **Deep Learning Framework**: PyTorch
- **Audio Processing**: Torchaudio, Librosa
- **Visualization**: Matplotlib, Seaborn
- **Pretrained Backbone**: ResNet-18

### **Dependencies**
Install the necessary libraries and tools:
```bash
apt-get update && apt-get install sox libsox-dev libsox-fmt-all -y
pip install torchaudio librosa matplotlib seaborn scikit-learn tensorboard
```

### **Data Used**
- **Dataset**: [Librispeech ASR Corpus](https://www.openslr.org/12)  
  - Preprocessed to ensure clean, mono-channel audio samples at 16 kHz.  
  - Used to train and validate the Siamese network.

### **Steps to Run**
1. **Data Preparation**: Preprocess the dataset to extract features.
   ```python
   preprocess_waveform(waveform, sample_rate)
   get_mfcc(waveform)
   ```

2. **Training the Model**:
   Train the **ResNet-18-powered Siamese Neural Network**:
   ```python
   model = OneShotSiameseNetwork(fixed_length=500).to(device)
   train_one_shot_model(model, train_loader, val_loader, num_epochs=10)
   ```

3. **Speaker Enrollment**:
   Capture and store the user’s unique embedding:
   ```python
   stored_embedding = enroll_user(model, '/path/to/enrollment_audio.wav')
   ```

4. **Speaker Verification**:
   Authenticate a user with real-time input:
   ```python
   is_authenticated, score = verify_user(
       model, 
       stored_embedding, 
       '/path/to/verification_audio.wav', 
       optimal_threshold
   )
   print(f"Authenticated: {is_authenticated}, Similarity Score: {score:.4f}")
   ```

---

## **Images**
### **Feature Extraction**
#### 1.![mfccsample1](https://github.com/user-attachments/assets/83bdc3e7-55d0-4a44-83bb-d71b834a2265)


#### 2.![mfccsample2](https://github.com/user-attachments/assets/d6412747-fac4-4496-b1bd-802b3dea3fba)


#### 3. ![mfccsample3](https://github.com/user-attachments/assets/2e1fdbac-9b12-435f-9dac-1b20cfc35449)

---

## **Applications**
1. **Driver Authentication**:
   - Enhances car security by ensuring only registered users can unlock and start the vehicle.
   - Prevents key theft or misuse by unauthorized users.

2. **Personalized Vehicle Settings**:
   - Automatically configures seat position, music playlists, climate control, and navigation preferences.

3. **Secure Home & Office Access**:
   - Extends functionality to secure access systems for homes, offices, and sensitive facilities.

---

## **Future Enhancements**
1. **Noise Robustness**:
   - Incorporate advanced denoising methods for handling high-noise environments.
2. **Multi-Language Support**:
   - Extend compatibility to various languages and accents for global adoption.
3. **Integration with Edge Devices**:
   - Optimize the model for low-power embedded systems in IoT devices.
