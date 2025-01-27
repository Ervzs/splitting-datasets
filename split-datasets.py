import os
import shutil
import random

# Paths to your images and labels (use raw strings to avoid issues with backslashes)
image_folder = r"C:\_Pycharm-projects\_Yolo-Test-TrainModel\Phaeton-Images\data\images"
label_folder = r"C:\_Pycharm-projects\_Yolo-Test-TrainModel\Phaeton-Images\data\labels"

# Directories for train and validation
train_image_folder = r"C:\_Pycharm-projects\_Yolo-Test-TrainModel\Phaeton-Images\data\train\images"
val_image_folder = r"C:\_Pycharm-projects\_Yolo-Test-TrainModel\Phaeton-Images\data\validation\images"
train_label_folder = r"C:\_Pycharm-projects\_Yolo-Test-TrainModel\Phaeton-Images\data\train\labels"
val_label_folder = r"C:\_Pycharm-projects\_Yolo-Test-TrainModel\Phaeton-Images\data\validation\labels"

# Get all image files
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]

# Shuffle the files to randomize the split
random.shuffle(image_files)

# Split the data (80% train, 20% validation)
split_ratio = 0.8
train_size = int(len(image_files) * split_ratio)

# Move files to train and validation directories
for i, image_file in enumerate(image_files):
    label_file = image_file.replace(".jpg", ".txt").replace(".png", ".txt")
    
    if i < train_size:
        shutil.move(os.path.join(image_folder, image_file), os.path.join(train_image_folder, image_file))
        shutil.move(os.path.join(label_folder, label_file), os.path.join(train_label_folder, label_file))
    else:
        shutil.move(os.path.join(image_folder, image_file), os.path.join(val_image_folder, image_file))
        shutil.move(os.path.join(label_folder, label_file), os.path.join(val_label_folder, label_file))

print("Dataset split complete!")
