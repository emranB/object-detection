# Object Detection with Proximity Warning

This project is a Dockerized YOLOv5-based object detection application that identifies humans and other objects in a live video feed from your camera. The app highlights humans with green bounding boxes, marks other nearby objects with red bounding boxes, and displays the distance between the human and each object on the side of the screen.

# Project Structure

OBJECT-DETECTION
│
├── docker-compose.ubuntu22.nvidia4060.yml  # For Ubuntu with NVIDIA GPU
├── docker-compose-win11.yml                # For Windows 11 without GPU
├── Dockerfile                              # Dockerfile for Ubuntu with GPU support
├── Dockerfile.win11.no_gpu                 # Dockerfile for Windows 11 without GPU support
├── README.md                               # Project documentation
├── pyproject.toml                          # Poetry configuration for dependencies
└── src                                     # Source folder containing application code
    ├── main.py                             # Main controller script
    ├── object-detector                     # Module folder for object detection
    │   ├── __init__.py       
    │   └── yolov5-detector.py              # YOLOv5 detector class
    └── utils                               # Utility functions folder
        ├── __init__.py       
        ├── distance-calculator.py          # Distance calculation utility
        └── get-camera-feed.py              # Utility to get the camera feed based on OS

## Features
- Real-time object detection using YOLOv5.
- Highlights humans with green bounding boxes.
- Marks objects within 5 meters of a detected human with red bounding boxes.
- Labels each detected object (if known) or as an unknown object if unidentified.
- Displays the distance between the human and each object.

## Prerequisites
- NVIDIA GPU with CUDA support (tested on NVIDIA 4060).
- Docker and Docker Compose installed.
- NVIDIA Container Toolkit for Docker to enable GPU support.

## Setup Instructions

1. **Clone the Repository**
   ```bash
    git clone https://github.com/emranB/object-detection
    cd object-detection
    ```

2. Build and Run the Docker Container
    ```bash
    docker-compose up --build
    ```
    This will start the object detection application, open your camera feed, and display the detections in real time.

3. Exit the Application Press q in the video window to stop the application.

## Files
Main files to analyze:

| File                    | Description                                                                  |
|-------------------------|------------------------------------------------------------------------------|
| `docker-compose.yml`    | Docker Compose configuration for setting up the service.                    |
| `Dockerfile`            | Dockerfile to set up the environment for YOLOv5 with CUDA support.          |
| `src/main.py`           | Main application file that handles video processing, object detection, and proximity warnings. |
| `yolov5-detector.py`    | YOLOv5 detector class for handling object detection.                        |
| `distance-calculator.py` | Utility function for calculating the distance to objects.                  |


## Customization
| Customization Option   | Description                                                                                                                                                                      |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Camera Source**      | Change `cv2.VideoCapture(0)` in `yolov5-detector.py` if you want to use a different camera source.                                                                              |
| **YOLO Model**         | You can switch to other YOLO models by modifying `model = torch.hub.load('ultralytics/yolov5', 'yolov5l', pretrained=True)` to use `yolov5s`, `yolov5m`, etc.                  |


## Notes
- Ensure you have granted camera permissions on your machine.
- GPU acceleration is essential for optimal performance.

## Troubleshooting
If you face any issues with Docker, verify that the NVIDIA Container Toolkit is correctly installed.
If the camera feed does not open, ensure that your webcam is properly connected and accessible on `/dev/video0`.

## License
This project is licensed under the MIT License.
