import cv2
import os

def get_camera_feed():
    """
    Returns a VideoCapture object for the camera feed.
    Uses a local device for Ubuntu (e.g., /dev/video0) and an IP stream for Windows.
    """
    camera_source = os.getenv("CAMERA_SOURCE", "0")  # Default to 0 for local camera
    return cv2.VideoCapture(camera_source)
