from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('models/best.pt')

# Run predictions on the input video
results = model.predict('input_videos/08fd33_4.mp4', save=True)

# Print the results for the first image/frame
print(results[0])

print('==================')
# Iterate through the boxes and print them
for box in results[0].boxes:
    print(box)  # Fixed typo here: changed 'pirnt' to 'print'
