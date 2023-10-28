from ultralytics import YOLO
import os

model = YOLO('./runs/detect/train/weights/best.pt')
model.conf = 0.25
#files = [f'testing/{x}' for x in os.listdir('testing')]
files = [f'YOLO/images/Test/{x}' for x in os.listdir('YOLO/images/Test')]
for file in files:
    results = model(file)

    print(results)