import os
from PIL import Image
from glob import glob

input_folder = r""
output_folder = r""

# Get list of all JPG files
jpg_files = glob(os.path.join(input_folder, "*.jpg"))

for file in jpg_files:
    img = Image.open(file)
    filename = os.path.splitext(os.path.basename(file))[0]  
    output_path = os.path.join(output_folder, f"{filename}.png")

    # Convert and save as PNG
    img.save(output_path, "PNG")

print("Images successfully converted to .png format")