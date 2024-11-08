import cv2
import torch
from utils.distance_calculator import calculate_distance
from utils.get_camera_feed import get_camera_feed

class YoloDetector:
    def __init__(self):
        # Load the YOLO model
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5l', pretrained=True)
        # Initialize camera
        self.cap = get_camera_feed()

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame if ret else None

    def detect_objects(self, frame):
        results = self.model(frame)
        predictions = results.xyxy[0].cpu().numpy()
        return predictions

    def display_detections(self, frame, predictions):
        for *box, conf, cls in predictions:
            label = self.model.names[int(cls)]
            distance = calculate_distance(box)
            color = (0, 255, 0) if label == 'person' else (0, 0, 255)
            cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), color, 2)
            cv2.putText(frame, f"{label} {distance}m", (int(box[0]), int(box[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.imshow("YOLO Object Detection", frame)

    def exit_requested(self):
        return cv2.waitKey(1) & 0xFF == ord('q')

    def close_windows(self):
        self.cap.release()
        cv2.destroyAllWindows()
