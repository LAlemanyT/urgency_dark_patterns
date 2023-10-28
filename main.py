from ultralytics import YOLO
import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:21"

model = YOLO("yolov8m.yaml") #new model from scratch

results = model.train(data="config.yaml", epochs=1000, batch=8) #train model