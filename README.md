# -Player-Tracking-and-Action-Recognition-Model

⚽ Football Analysis System using YOLOv8, Computer Vision & Deep Learning

This project demonstrates how to build a Football Analysis System that combines machine learning, computer vision, and deep learning techniques to analyze football matches. It leverages YOLOv8 for object detection, KMeans for team classification, optical flow for camera motion estimation, and perspective transformation to measure real-world player movement.

The system detects players, referees, and footballs, tracks them across frames, assigns players to teams based on t-shirt colors, and calculates their speed and distance covered in meters.

🚀 Features

✅ Detect players, referees, and footballs using YOLOv8.

✅ Fine-tune and train YOLOv8 on a custom dataset.

✅ Use KMeans clustering to segment player t-shirts for team assignment.

✅ Apply Optical Flow to measure camera movement.

✅ Implement Perspective Transformation to convert pixel distances into real-world meters.

✅ Track players across frames and calculate:

🏃 Player speed

📏 Distance covered

📂 Project Structure
football-analysis/
│-- data/                  # Dataset & annotations
│-- models/                # YOLO weights & trained models
│-- src/
│   ├── detection.py        # YOLOv8 detection script
│   ├── tracking.py         # Object tracking logic
│   ├── team_clustering.py  # KMeans clustering for t-shirt colors
│   ├── optical_flow.py     # Camera movement estimation
│   ├── perspective.py      # Perspective transformation
│   ├── analysis.py         # Player speed & distance calculation
│   └── utils.py            # Helper functions
│-- notebooks/             # Jupyter notebooks for experiments
│-- requirements.txt       # Dependencies
│-- README.md              # Project documentation

🛠️ Installation

Clone the repository:

git clone https://github.com/your-username/football-analysis.git
cd football-analysis


Create a virtual environment & install dependencies:

pip install -r requirements.txt


Install Ultralytics YOLOv8:

pip install ultralytics

📊 Usage
1. Run Object Detection
python src/detection.py --source data/match.mp4 --weights models/yolov8_custom.pt

2. Train YOLOv8 on Custom Dataset
yolo detect train data=data/dataset.yaml model=yolov8n.pt epochs=50 imgsz=640

3. Run Player Team Assignment (KMeans)
python src/team_clustering.py --input outputs/detections/

4. Apply Optical Flow for Camera Movement
python src/optical_flow.py --input data/match.mp4

5. Perspective Transformation & Player Speed
python src/analysis.py --input outputs/tracked/

📦 Requirements

Python 3.8+

Ultralytics YOLOv8

OpenCV

NumPy

scikit-learn

Matplotlib

Install all requirements with:

pip install -r requirements.txt

📹 Demo

👉 [Add demo video or screenshots here]

🌟 Key Concepts Covered

YOLOv8 object detection

Custom dataset training

KMeans clustering for segmentation

Optical Flow for motion estimation

Perspective Transformation in OpenCV

Speed & distance measurement in real-world units

📌 Applications

Football match analysis

Sports analytics platforms

Player performance evaluation

Real-time broadcast enhancement

🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

📜 License

This project is licensed under the MIT License.
