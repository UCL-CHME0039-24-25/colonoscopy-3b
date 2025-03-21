""""
Prior to running this script ensure the data directory is structured as follows:
 data_folder/
   images/
   labels/

 The final split directory structure will be as follows:
 data_folder/
   images/
       train/
       valid/
       test/
   labels/
       train/
       valid/
       test/
"""""

import os
import shutil
import random
from glob import glob

# Define base paths
base_path = r""
image_folder = os.path.join(base_path, "images")  
label_folder = os.path.join(base_path, "labels")  

# Get all image files
image_files = glob(os.path.join(image_folder, "*.png"))  # Change to "*.jpg" if necessary

if not image_files:
    print(f"No images found in {image_folder}. Please check the folder and path.")
else:
    random.shuffle(image_files)

    # Specify your custom split ratio (e.g., 80% train, 10% valid, 10% test)
    train_ratio = 0.80
    valid_ratio = 0.10
    test_ratio = 0.10

    # Calculate split
    total_images = len(image_files)
    train_count = int(total_images * train_ratio)
    valid_count = int(total_images * valid_ratio)
    test_count = total_images - train_count - valid_count

    train_files = image_files[:train_count]
    valid_files = image_files[train_count:train_count + valid_count]
    test_files = image_files[train_count + valid_count:]

    def move_files(file_list, split):
        split_image_folder = os.path.join(image_folder, split)
        split_label_folder = os.path.join(label_folder, split)

        #Create split folders if not already in place in output directory
        os.makedirs(split_image_folder, exist_ok=True)
        os.makedirs(split_label_folder, exist_ok=True)

        for img_path in file_list:
            filename = os.path.basename(img_path) 
            label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + ".txt")

            try:
                shutil.move(img_path, os.path.join(split_image_folder, filename))
            except Exception as e:
                print(f"Error moving image {img_path} to {split_image_folder}: {e}")

            if os.path.exists(label_path):
                try:
                    shutil.move(label_path, os.path.join(split_label_folder, os.path.basename(label_path)))
                except Exception as e:
                    print(f"Error moving label {label_path} to {split_label_folder}: {e}")

    # Move files into train/valid/test
    move_files(train_files, "train")
    move_files(valid_files, "valid")
    move_files(test_files, "test")

    print(f"Dataset split completed successfully! ({train_ratio*100}% train, {valid_ratio*100}% valid, {test_ratio*100}% test)")