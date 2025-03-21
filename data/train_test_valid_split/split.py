import os
import shutil
import random
from glob import glob

# Define base paths
base_path = r"C:\Users\Kate\OneDrive - TCDUD.onmicrosoft.com\Documents\UCL\Group Project\Data\hk_data"
image_folder = os.path.join(base_path, "images")  # Source images folder
label_folder = os.path.join(base_path, "labels")  # Source labels folder

# Get all image files (adjust extension if needed)
image_files = glob(os.path.join(image_folder, "*.png"))  # Change to "*.jpg" if necessary

# Check if image_files is empty
if not image_files:
    print(f"No images found in {image_folder}. Please check the folder and path.")
else:
    random.shuffle(image_files)  # Shuffle to ensure randomness

    # Assign splits
    train_files = image_files[:800]
    valid_files = image_files[800:900]
    test_files = image_files[900:1000]

    # Function to move images and corresponding labels
    def move_files(file_list, split):
        # Ensure the split folder exists
        split_image_folder = os.path.join(image_folder, split)
        split_label_folder = os.path.join(label_folder, split)

        os.makedirs(split_image_folder, exist_ok=True)
        os.makedirs(split_label_folder, exist_ok=True)

        for img_path in file_list:
            filename = os.path.basename(img_path)  # Get filename (e.g., "image1.png")
            label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + ".txt")  # Corresponding label

            try:
                # Move image to its split folder
                shutil.move(img_path, os.path.join(split_image_folder, filename))
            except Exception as e:
                print(f"Error moving image {img_path} to {split_image_folder}: {e}")

            # Move label if it exists
            if os.path.exists(label_path):
                try:
                    shutil.move(label_path, os.path.join(split_label_folder, os.path.basename(label_path)))
                except Exception as e:
                    print(f"Error moving label {label_path} to {split_label_folder}: {e}")

    # Move files into train/valid/test
    move_files(train_files, "train")
    move_files(valid_files, "valid")
    move_files(test_files, "test")

    print("Dataset split completed successfully!")