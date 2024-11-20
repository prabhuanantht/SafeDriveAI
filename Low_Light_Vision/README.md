

# Low Light Vision Enhancement using MIRNet

This project uses the MIRNet model from Hugging Face to enhance low-light images. The program reads an input image, enhances it using the MIRNet model, and saves the output image while displaying a side-by-side comparison.

## Features

- Enhance low-light images using MIRNet, a state-of-the-art image enhancement model.
- Display original and enhanced images for visual comparison.
- Easily configurable input and output image paths.

## Requirements

- Python 3.8 or later
- TensorFlow 2.10 or later
- OpenCV for image processing
- Matplotlib for displaying images
- Hugging Face Hub for loading the pre-trained MIRNet model

## Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Place your input image in the same directory as the script or provide the correct path in the code.

## Usage

1. Edit the `input_image_path` and `output_image_path` variables in the script:
   ```python
   input_image_path = "input.jpg"
   output_image_path = "enhanced_image.jpg"
   ```

2. Run the script:
   ```bash
   python mirnet_enhancement.py
   ```

3. The enhanced image will be saved to the specified output path and displayed for comparison.

## Example

Original vs Enhanced Image:
![Example](example.png)

## Notes

- Ensure the input image has a resolution compatible with the MIRNet model. The resolution should be a multiple of 4.
- The MIRNet model may take some time to load initially due to its size and complexity.

## Acknowledgments

- MIRNet model from [Hugging Face](https://huggingface.co/keras-io/lowlight-enhance-mirnet)
- TensorFlow and OpenCV for image processing