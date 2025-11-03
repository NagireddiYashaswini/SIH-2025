from ultralytics import YOLO

model = YOLO("yolov8s.pt")


results = model.train(
    data="c:/SIH 2025/config.yaml", 
    epochs=150,                       
    project="c:/SIH 2025/runs",
    name="elephant_detect_v4"        
)
