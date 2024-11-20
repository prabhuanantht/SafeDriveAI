# Traffic Sign Detection using YOLOv5

This project trains a YOLOv5 model to detect traffic signs in images using a custom dataset. The process includes data preparation, conversion of annotations, training, and testing on new images. The dataset comprises annotated traffic signs in Pascal VOC format, converted to YOLO format for training.

---

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Dataset Preparation](#dataset-preparation)
4. [Model Training](#model-training)
5. [Inference](#inference)
6. [Custom Image Testing](#custom-image-testing)
7. [Saving and Using the Model](#saving-and-using-the-model)
8. [Drive Integration](#drive-integration)

---

## Requirements
- Python 3.8 or later
- PyTorch and YOLOv5 dependencies
- Google Colab for training (recommended)
- A dataset of annotated traffic sign images in Pascal VOC format

---

## Installation
1. Update the system and install necessary tools:
   ```bash
   !apt-get update
   !apt-get install -y sox libsox-dev libsox-fmt-all
   ```
2. Install Python libraries:
   ```bash
   !pip install --upgrade pip
   !pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
   !pip install seaborn matplotlib opencv-python kaggle
   ```
3. Clone the YOLOv5 repository and install dependencies:
   ```bash
   !git clone https://github.com/ultralytics/yolov5.git
   %cd yolov5
   !pip install -r requirements.txt
   ```

---

## Dataset Preparation
1. Unzip your dataset:
   ```bash
   !unzip -o /content/road-sign-detection.zip -d /content/data/
   ```
2. Convert annotations from Pascal VOC to YOLO format:
   ```python
   def convert_voc_to_yolo():
       # Conversion logic
   convert_voc_to_yolo()
   ```
3. Split the dataset into training and validation sets:
   ```python
   train_images, val_images = train_test_split(all_images, test_size=0.2, random_state=42)
   copy_data(train_images, train_images_dir, train_labels_dir)
   copy_data(val_images, val_images_dir, val_labels_dir)
   ```

---

## Model Training
1. Create a `customVOC.yaml` file:
   ```python
   custom_yaml = {
       'train': 'data/train/images',
       'val': 'data/val/images',
       'nc': 4,
       'names': ['trafficlight', 'speedlimit', 'crosswalk', 'stop']
   }
   with open('customVOC.yaml', 'w') as file:
       yaml.dump(custom_yaml, file)
   ```
2. Train the YOLOv5 model:
   ```bash
   !python train.py --img 320 --batch 16 --epochs 100 --data customVOC.yaml --weights yolov5s.pt --workers 2 --cache
   ```

---

## Inference
1. Load the trained model:
   ```python
   model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp/weights/best.pt', force_reload=True)
   model.to(device)
   ```
2. Visualize predictions on validation data:
   ```python
   sample_images = random.sample(val_images, 8)
   # Visualization logic
   ```

---

## Custom Image Testing
1. Upload and test custom images:
   ```python
   from google.colab import files
   uploaded = files.upload()
   # Process uploaded images
   ```

---

## Saving and Using the Model
- Save your best weights (`best.pt`) and use them for inference.

---

## Drive Integration
1. Mount Google Drive to save results:
   ```bash
   from google.colab import drive
   drive.mount('/content/drive')
   ```
2. Save trained weights or datasets to the drive for future use.

---

## Output
The trained YOLOv5 model detects traffic signs, including **traffic lights, speed limits, crosswalks, and stop signs**, with predictions visualized on sample and custom images.

---

### Notes
- Ensure the dataset and annotations are correctly structured before training.
- Optimize hyperparameters like image size, batch size, and epochs for improved accuracy.
- Use a GPU environment for faster training and inference.