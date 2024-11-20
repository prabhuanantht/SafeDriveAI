# Import necessary libraries
import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras
from huggingface_hub import from_pretrained_keras
import matplotlib.pyplot as plt
import os

# Load the pre-trained MIRNet model from the Hugging Face Hub
model = from_pretrained_keras("keras-io/lowlight-enhance-mirnet", compile=False)

def enhance_image(image):
    """
    Enhances a given image using the MIRNet model.
    :param image: Input image in RGB format
    :return: Enhanced image
    """
    # Ensure the image is in RGB format
    if image.shape[2] == 4:
        # Convert RGBA to RGB
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    elif image.shape[2] == 1:
        # Convert Grayscale to RGB
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    # Resize the image to the model's expected input size (multiple of 4)
    height, width, _ = image.shape
    new_height = height - (height % 4)
    new_width = width - (width % 4)
    image = image[0:new_height, 0:new_width, :]

    # Normalize the image
    input_image = image.astype('float32') / 255.0
    input_image = np.expand_dims(input_image, axis=0)

    # Perform inference
    output = model.predict(input_image)

    # Post-process the output image
    output_image = output[0]
    output_image = np.clip(output_image, 0, 1)
    output_image = (output_image * 255).astype('uint8')

    return output_image

def process_image(image_path, output_path):
    """
    Processes an image by enhancing it and saving the output.
    :param image_path: Path to the input image
    :param output_path: Path to save the enhanced image
    """
    # Read the input image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if image is None:
        print(f"Error: Unable to read image from {image_path}")
        return

    # Enhance the image
    enhanced_image = enhance_image(image)

    # Save the enhanced image
    cv2.imwrite(output_path, enhanced_image)

    # Display the original and enhanced images side by side
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    enhanced = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)
    combined = np.hstack((original, enhanced))

    plt.figure(figsize=(10, 10))
    plt.imshow(combined)
    plt.axis('off')
    plt.title("Original (Left) vs Enhanced (Right)")
    plt.show()

if __name__ == "__main__":
    # Input image path
    input_image_path = "input.jpg"  # Replace with your input image path
    # Output image path
    output_image_path = "enhanced_image.jpg"  # Replace with your desired output image path

    # Process the image
    process_image(input_image_path, output_image_path)

    print(f"Enhanced image saved at {output_image_path}")
