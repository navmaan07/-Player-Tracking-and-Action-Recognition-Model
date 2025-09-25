**Player Tracking and Action Recognition Model**
**Overview**
This project enables player tracking and action recognition in sports videos using deep learning models. After training the models, provide input video files and receive output videos with tracking and action labels automatically generated.

**Table of Contents**
*Features

*Installation

*Dataset Preparation

*Model Training

*Inference (Run on Videos)

*Output and Results

*Troubleshooting


**Features**
Player detection and tracking in input videos

Action recognition using trained deep learning models

Generates output videos with player bounding boxes and action labels

**Installation**
Clone the repository
git clone https://github.com/navmaan07/-Player-Tracking-and-Action-Recognition-Model.git
cd -Player-Tracking-and-Action-Recognition-Model

Install dependencies
pip install -r requirements.txt

**Dataset Preparation**
Prepare or download a training dataset with annotated videos or frames.

Organize data according to the model’s requirements (check scripts/config for specific details).

Example structure:
data/
videos/
annotations/

**Model Training**
Configure training settings in the config file (e.g., config/train_config.yaml).

Train the model:
python train.py --config config/train_config.yaml

Trained model weights will be saved in the models/ directory.

**Inference: Running on Input Videos**
Place input videos in input_videos/ folder.

Run inference:
python inference.py --model models/model_weights.pth --input input_videos/sample.mp4

The output video, with player tracking and action recognition, will be saved in output_videos/.

**Output and Results**
Resulting videos will contain bounding boxes and action labels for tracked players.

Example output:
output_videos/
sample_output.mp4

**Troubleshooting**
Ensure that all project dependencies are installed.

Confirm data paths and config file locations.

For GPU support, verify correct CUDA/cuDNN installation.


