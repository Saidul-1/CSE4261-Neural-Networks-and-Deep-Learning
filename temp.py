import os
import shutil
import random
from pathlib import Path

# === CHANGE THIS PATH ===
source_dir = "/home/saidul/Desktop/4-2/Deep Learning/data/monitor_detection/monitor-detection.yolov8/train"   # Your current train folder

# Create new structure
base_dir = "/home/saidul/Desktop/4-2/Deep Learning/data/monitor_detection"
os.makedirs(f"{base_dir}/images/train", exist_ok=True)
os.makedirs(f"{base_dir}/images/val", exist_ok=True)
os.makedirs(f"{base_dir}/images/test", exist_ok=True)
os.makedirs(f"{base_dir}/labels/train", exist_ok=True)
os.makedirs(f"{base_dir}/labels/val", exist_ok=True)
os.makedirs(f"{base_dir}/labels/test", exist_ok=True)

# Get all image files
image_files = [f for f in os.listdir(f"{source_dir}/images") if f.endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(image_files)

# Split ratios
total = len(image_files)
train_split = int(0.70 * total)
val_split = int(0.20 * total)

train_files = image_files[:train_split]
val_files = image_files[train_split:train_split+val_split]
test_files = image_files[train_split+val_split:]

def move_files(file_list, split):
    for img_file in file_list:
        label_file = img_file.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt')
        
        # Move image
        shutil.copy(f"{source_dir}/images/{img_file}", f"{base_dir}/images/{split}/{img_file}")
        # Move label
        if os.path.exists(f"{source_dir}/labels/{label_file}"):
            shutil.copy(f"{source_dir}/labels/{label_file}", f"{base_dir}/labels/{split}/{label_file}")

print("Moving files...")
move_files(train_files, "train")
move_files(val_files, "val")
move_files(test_files, "test")

print(f"Total images: {total}")
print(f"Train: {len(train_files)} | Val: {len(val_files)} | Test: {len(test_files)}")