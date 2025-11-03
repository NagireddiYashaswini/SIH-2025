from ultralytics import YOLO
import os
import cv2
from datetime import datetime

# Load model
model_path = "C:/SIH 2025/runs/elephant_detect6/weights/best.pt"
model = YOLO(model_path)

# Input and timestamped output folders
image_dir = "C:/SIH 2025/predict"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = f"C:/SIH 2025/predicted_outputs_DETECT6_VERSION5 {timestamp}"
os.makedirs(output_dir, exist_ok=True)

# Predict and save
for image_name in os.listdir(image_dir):
    if image_name.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        image_path = os.path.join(image_dir, image_name)
        results = model(image_path)

        for result in results:
            boxes = result.boxes
            if len(boxes) > 0:
                print(f"{image_name}: Elephant detected ✅")
            else:
                print(f"{image_name}: No elephant detected ❌")

        base_name, ext = os.path.splitext(image_name)
        output_path = os.path.join(output_dir, base_name + "_pred" + ext)
        results[0].save(filename=output_path)

print(f"\n✅ All predictions saved to: {output_dir}")
