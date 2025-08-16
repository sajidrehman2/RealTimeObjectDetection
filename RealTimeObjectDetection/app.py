import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

st.title("YOLOv8 Live Webcam Detection")

# Activate webcam
cam_image = st.camera_input("Capture an image")

if cam_image:
    # Convert to OpenCV format
    frame = np.array(Image.open(cam_image))
    
    # Load YOLOv8 model
    model = YOLO("yolov8n.pt")  # or your custom model
    
    # Run detection
    results = model(frame)
    
    # Show results
    result_img = results[0].plot()
    st.image(result_img, caption='Detected Objects', use_container_width=True)
