from object_detector.yolov5_detector import YoloDetector

def main():
    detector = YoloDetector()

    while True:
        frame = detector.get_frame()
        if frame is None:
            break

        detections = detector.detect_objects(frame)
        detector.display_detections(frame, detections)

        if detector.exit_requested():
            break

    detector.close_windows()

if __name__ == "__main__":
    main()
