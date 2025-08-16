
# Real-Time Object Detection with YOLOv8

## Features
- Real-time detection via webcam
- Upload videos to detect objects
- Displays FPS and annotated video feed
- Detects 80 common objects from COCO dataset
- Optional: Filter specific objects or use custom dataset

## Installation
1. Clone this repository:
```bash
git clone <repo-url>
cd RealTimeObjectDetection
```
2. Create virtual environment (optional):
```bash
python -m venv yolov8_env
source yolov8_env/bin/activate  # Linux/Mac
yolov8_env\Scripts\activate     # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Run Locally
```bash
streamlit run app.py
```
- Open browser → http://localhost:8501

## Deployment (Free)
### Streamlit Cloud
1. Push repo to GitHub
2. Go to https://share.streamlit.io
3. Click New App → Connect repo → Deploy

### Hugging Face Spaces
1. Go to https://huggingface.co/spaces
2. Select Streamlit → Upload files → Deploy

## Optional Enhancements
- Filter objects: `results = model(frame, classes=[0,2])` # 0=person, 2=car
- Custom dataset: Fine-tune YOLOv8 with Roboflow free dataset
