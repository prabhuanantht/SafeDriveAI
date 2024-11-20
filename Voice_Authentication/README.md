# One-Shot Voice Authentication System

This project implements a **One-Shot Learning Siamese Neural Network** for speaker authentication using **LibriSpeech dataset**. The system uses audio embeddings derived from MFCC (Mel Frequency Cepstral Coefficients) features to compare speaker samples and perform authentication.

## Features

- **Speaker Authentication**: Authenticate speakers using their voice samples.
- **One-Shot Learning**: Requires minimal training data for speaker identification.
- **Voice Activity Detection (VAD)**: Filters silence in audio samples to focus on voice regions.
- **Data Augmentation**: Enhances training data with random pitch and speed transformations.
- **Visualization**: Embedding space visualization using t-SNE and similarity score distributions.

## Prerequisites

1. **Python 3.8 or later**
2. **GPU Support**: Optional but recommended for faster training and inference.

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/your-repo-name/one-shot-voice-auth.git
cd one-shot-voice-auth
```

### Step 2: Install dependencies

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

### Step 3: Download Required Models

Download the **LibriSpeech dataset** and **Dlib's shape predictor** (for optional tasks).

- LibriSpeech dataset is automatically downloaded by the script.
- If needed, download Dlib's 68 facial landmark predictor from [here](https://github.com/davisking/dlib-models).

## Usage

### 1. **Training the Model**

Train the Siamese Network using the preprocessed LibriSpeech data:

```bash
python train_one_shot_model.py
```

### 2. **Enrollment**

Enroll a user using their audio sample:

```python
stored_embedding = enroll_user(model, "path/to/enrollment_audio.wav")
```

### 3. **Verification**

Verify the user's identity with a new audio sample:

```python
is_authenticated, score = verify_user(model, stored_embedding, "path/to/verification_audio.wav", threshold)
```

### 4. **Visualization**

Plot embeddings and similarity score distributions for analysis:

```python
plot_embedding_space(model, val_loader)
plot_similarity_distributions(model, val_loader, threshold)
```

## Code Structure

- **`train_one_shot_model.py`**: Main script for training the Siamese Network.
- **`utils.py`**: Helper functions for preprocessing, MFCC extraction, and VAD.
- **`model.py`**: Definition of the Siamese Network and loss function.
- **`test.py`**: Test the model with enrollment and verification tasks.

## Dependencies

### Major Libraries:
- **PyTorch**: For deep learning model implementation.
- **Torchaudio**: For audio processing and transformations.
- **Librosa**: For advanced audio visualization and analysis.
- **Matplotlib & Seaborn**: For plotting graphs and distributions.
- **Scikit-Learn**: For computing metrics and visualizing embeddings.

### Install system dependencies for `torchaudio`:
- **Linux**:
  ```bash
  sudo apt-get update
  sudo apt-get install sox libsox-dev libsox-fmt-all
  ```

### TensorBoard:
To monitor the training process, run:
```bash
tensorboard --logdir=runs
```

## Example Results

### Training and Validation Loss
![Training Loss](images/loss_plot.png)

### Embedding Space Visualization
![t-SNE](images/tsne_plot.png)

### Similarity Score Distribution
![Similarity Scores](images/similarity_distribution.png)

## Acknowledgments

- **PyTorch** and **Torchaudio** for deep learning and audio processing tools.
- **LibriSpeech** for providing a rich dataset of audio samples.
- **TensorBoard** for visualizing training progress.
- **Scikit-Learn** for embedding space analysis and evaluation metrics.

## License

MIT License