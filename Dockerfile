FROM nvcr.io/nvidia/pytorch:22.04-py3  # NVIDIA PyTorch base image for GPU support

RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
RUN pip install opencv-python-headless pyyaml requests  # Install dependencies

# Clone YOLO repository
RUN git clone https://github.com/ultralytics/yolov5.git && cd yolov5 && pip install -r requirements.txt

WORKDIR /yolov5

# Copy your application file
COPY app.py .

CMD ["python3", "app.py"]
