import torch
import cv2
import numpy as np

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Define navigation commands (you can connect these to robot hardware later)
def move_left():
    print("Move LEFT!")
    # Add actual hardware control for moving left here

def move_right():
    print("Move RIGHT!")
    # Add actual hardware control for moving right here

def move_forward():
    print("Move FORWARD!")
    # Add actual hardware control for moving forward here

def stop():
    print("STOP!")
    # Add actual hardware control for stopping here

# Start real-time object detection and navigation
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Make detections with YOLOv5
    results = model(frame)
    detections = results.xyxy[0].cpu().numpy()  # Get bounding boxes and labels

    # Set initial movement command
    movement_command = "forward"

    # Define center areas for navigation logic
    frame_center_x = frame.shape[1] / 2
    left_threshold = frame_center_x * 0.3
    right_threshold = frame_center_x * 1.7

    for det in detections:
        x1, y1, x2, y2, conf, cls = det  # Extract coordinates and confidence
        label = model.names[int(cls)]  # Get label name (e.g., 'person', 'car')

        # Filter out objects that are not relevant (like 'person' or 'car')
        if label in ['person', 'car'] and conf > 0.5:
            # Calculate object center
            object_center_x = (x1 + x2) / 2

            # Display bounding box and label on frame
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Determine the navigation direction based on object position
            if left_threshold <= object_center_x <= right_threshold:
                movement_command = "stop"
            elif object_center_x < left_threshold:
                movement_command = "right"
            elif object_center_x > right_threshold:
                movement_command = "left"

    # Execute movement command
    if movement_command == "left":
        move_left()
        cv2.putText(frame, "Move LEFT!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    elif movement_command == "right":
        move_right()
        cv2.putText(frame, "Move RIGHT!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    elif movement_command == "stop":
        stop()
        cv2.putText(frame, "STOP!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        move_forward()
        cv2.putText(frame, "Move FORWARD!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame with annotations
    cv2.imshow('YOLOv5 Object Detection with Navigation', frame)

    # Exit condition
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
