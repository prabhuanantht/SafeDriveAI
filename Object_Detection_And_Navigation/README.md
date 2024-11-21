# Obstacle Detection and Navigation System

This project is an advanced obstacle detection and navigation system that utilizes **YOLOv5**, **OpenCV**, and **PyTorch** to detect obstacles in real-time and navigate accordingly. It is designed to work seamlessly with live webcam feeds, providing intelligent navigation commands that can be integrated with robot hardware or adapted for car-based autonomous navigation.

## Key Features

- **Real-Time Object Detection**: Utilizes the YOLOv5 model to accurately detect obstacles in a live video feed from a webcam or car-mounted camera, ensuring reliable real-time performance.
- **Dynamic Navigation Commands**: Provides adaptive navigation commands such as moving left, right, forward, and stopping based on detection results to effectively avoid obstacles.
- **Simple Robotics Integration**: The system can be easily integrated with existing robot or car hardware to allow autonomous obstacle avoidance and navigation.
- **Customizable and Extensible**: The navigation logic and detection capabilities can be modified to suit specific use cases or integrated with different hardware platforms.

## Technologies Used

- **YOLOv5**: A state-of-the-art object detection model capable of identifying multiple classes of objects in real-time. The YOLOv5 model is loaded directly from the PyTorch Hub, making it easy to use and flexible.
- **OpenCV**: Used for accessing the camera feed, frame processing, and image manipulation.
- **PyTorch**: Utilized for loading and running the YOLOv5 model, enabling efficient model inference.

## Setup and Installation

Follow these steps to set up and run the project:

1. **Install Dependencies** Make sure you have Python 3.x installed. Install the required Python packages using:

   ```sh
   pip install -r requirements.txt
   ```

2. **Run the Navigation Script** To start the obstacle detection and navigation, execute the Python script:

   ```sh
   python Object_Detection_And_Navigation.py
   ```

## How It Works

1. **Loading YOLOv5 Model**: The script loads the YOLOv5 model from the PyTorch Hub, using the following line of code:
   ```python
   model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)
   ```
   The model is pre-trained to recognize a wide variety of objects and is used here for obstacle detection.
2. **Accessing Camera**: The camera is initialized to provide a live video feed, which is processed frame by frame using OpenCV. The following line of code is used to initialize the camera:
   ```python
   cap = cv2.VideoCapture(0)
   ```
3. **Obstacle Detection and Navigation Commands**: Each frame from the video feed is analyzed to detect obstacles, such as pedestrians, vehicles, or other barriers. Based on the position of the detected obstacle, specific navigation commands are issued:
   - **Move Left**: If an obstacle is detected on the right side of the frame, the system instructs the vehicle or robot to move left to avoid it.
     ```python
     def move_left():
         print("Move LEFT!")
         # Add actual hardware control for moving left here
     ```
   - **Move Right**: If an obstacle is detected on the left side of the frame, the system instructs the vehicle or robot to move right to maintain a clear path.
     ```python
     def move_right():
         print("Move RIGHT!")
         # Add actual hardware control for moving right here
     ```
   - **Move Forward**: If no obstacles are detected directly ahead, the vehicle or robot continues to move forward.
     ```python
     def move_forward():
         print("Move FORWARD!")
         # Add actual hardware control for moving forward here
     ```
   - **Stop**: If an obstacle is detected directly in front of the vehicle or robot at a close range, the system issues a stop command to prevent a collision.
     ```python
     def stop():
         print("STOP!")
         # Add actual hardware control for stopping here
     ```
   - **Navigate Accordingly**: In more complex scenarios, the system can make decisions to navigate dynamically, such as slowing down or turning based on multiple obstacle detections and their proximity.
     ```python
     def navigate_complex():
         print("Navigating complex environment!")
         # Add logic for more advanced navigation here
     ```

The navigation commands are highly customizable, allowing developers to add hardware-specific control logic to connect with actual robotic or car systems.

## Customization Options

- **Hardware Integration**: The `move_left()`, `move_right()`, `move_forward()`, and `stop()` functions can be adapted to send control signals to your robot or car hardware. This can be done using GPIO pins, motor controllers, or other communication protocols suitable for automotive systems.
- **Model Tuning**: You can change the YOLOv5 model variant (e.g., `yolov5s`, `yolov5m`, `yolov5l`) to adjust the balance between performance and accuracy depending on your computational capabilities.
- **Detection Zones**: Modify the code to define custom detection zones for more granular control over movement decisions, improving navigation efficiency and ensuring smoother driving in a car context.

## Future Improvements

- **Advanced Obstacle Avoidance**: Implement more sophisticated decision-making algorithms, such as potential fields or reactive control, to handle complex environments with multiple obstacles.
- **Multi-Sensor Fusion**: Integrate additional sensors like ultrasonic, infrared, or LIDAR for increased reliability and redundancy in obstacle detection, especially in low-visibility conditions.
- **Path Planning**: Incorporate a path-planning algorithm, such as A\* or Dijkstra's, to enable the system to find optimal paths through complex environments.
- **SLAM Integration**: Add Simultaneous Localization and Mapping (SLAM) capabilities to create maps of unknown environments and navigate more autonomously.
- **Voice Commands**: Allow voice-based commands for manual control of the vehicle or robot in conjunction with autonomous navigation.
- **Adaptive Speed Control**: Introduce adaptive speed control where the vehicle can automatically adjust its speed based on obstacle distance and type, ensuring safe navigation.
