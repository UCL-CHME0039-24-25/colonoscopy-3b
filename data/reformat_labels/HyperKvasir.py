import os
import json
from pathlib import Path

# Define input and output paths
input_path = r""
output_path = r""

# Load JSON data
with open(input_path, "r") as f:
    data = json.load(f)

# Convert bounding box to yolo format
for image_id, image_data in data.items():
    img_width = image_data["width"]
    img_height = image_data["height"]
    file_name = image_id  

    yolo_annotations = []

    for bbox in image_data["bbox"]:
        xmin, ymin, xmax, ymax = bbox["xmin"], bbox["ymin"], bbox["xmax"], bbox["ymax"]
        center_x = (xmin + xmax) / 2 / img_width
        center_y = (ymin + ymax) / 2 / img_height
        norm_w = (xmax - xmin) / img_width
        norm_h = (ymax - ymin) / img_height

        # Class ID is 0 for "polyp"
        yolo_annotations.append(f"0 {center_x:.6f} {center_y:.6f} {norm_w:.6f} {norm_h:.6f}")

    # Write in .txt file
    if yolo_annotations:
        with open(os.path.join(output_path, f"{file_name}.txt"), "w") as t:
            t.write("\n".join(yolo_annotations))

print("Conversion completed successfully!")