from ultralytics import YOLO
from PIL import Image
import torch

datapath = '/home/mdass8089/cs432/sec.v5i.yolov8/data.yaml'

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

# Train YOLOv8 model

model = YOLO('yolov8n.pt').to(device)
model.train(data=datapath, epochs=100)


# Print metrics of the model's performance

metrics = model.val()
print(metrics)

# Export model

model.export(format='onnx')

# Run inference

results = model.predict(source='https://cpl.org/wp-content/uploads/CellaKevin.png')
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen
    result.save(filename='result.jpg')  # save to disk