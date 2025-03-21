from PIL import Image
from tqdm import tqdm
import os

def get_image_size(image_path):
    img = Image.open(image_path)
    return img.size

def ld_txt_to_yolo(input_path, image_path, output_path):
  with open(input_path, 'r') as f:
    lines = f.readlines()

  with open(output_path, 'w') as f:
    for l in lines[1:]:
      # Transform datatype of the whole list from str to int
      l = l.split()
      l = [int(s) for s in l]

      # Transform the bbox co-ordinates as per the format required by YOLO v7
      # xmin, ymin, xmax, ymax
      b_center_x = (l[0] + l[2]) / 2
      b_center_y = (l[1] + l[3]) / 2
      b_width    = (l[2] - l[0])
      b_height   = (l[3] - l[1])

      # Normalise the co-ordinates by the dimensions of the image
      image_w, image_h = get_image_size(image_path)
      b_center_x /= image_w
      b_center_y /= image_h
      b_width    /= image_w
      b_height   /= image_h

      print_buffer = "0 {:.3f} {:.3f} {:.3f} {:.3f}\n".format(b_center_x, b_center_y, b_width, b_height)

      f.write(print_buffer)


if __name__ == "__main__":
    # Create folder for the new annotations
    # Define the base path
    base_path="~/allreadwrite/data/LDPolypVideo_data/LDPolypVideo_annotations/Annotations_yolov7"

    # Loop to create 100 folders (named 1 to 100)
    for i in range(1, 101):
        new_path = os.path.join(base_path, i)
        if not os.path.exists(new_path):
            os.makedirs(new_path)

    # Get paths to the annotations and images
    labels = [os.path.join(paths, f) for paths, _, files in os.walk('~/allreadwrite/data/LDPolypVideo_data/LDPolypVideo_annotations/Annotations/') for f in files if f[-3:] == "txt"]
    labels.sort()
    print("Show label paths:", labels[:3])

    images = [os.path.join(paths, f) for paths, _, files in os.walk('~/allreadwrite/data/LDPolypVideo_data/LDPolypVideo_annotations/Images/') for f in files if f[-3:] == "jpg"]
    images.sort()
    print("Show image paths:", images[:3])

    # Convert and save the annotations
    print("Converting annotations...")
    for ann, img in tqdm(zip(labels, images), total=len(labels)):
        ld_txt_to_yolo(ann, img, ann.replace('Annotations', 'Annotations_yolov7'))
    print("LDPolypVideo labels converted and saved to yolov7 format under: ", base_path)
