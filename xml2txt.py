import os
from tqdm import tqdm
import xml.etree.ElementTree as ET

# Function to get the data from XML Annotation
def extract_info_from_xml(xml_file):
    root = ET.parse(xml_file).getroot()

    # Initialise the info dict 
    info_dict = {}
    info_dict['bboxes'] = []

    # Get the file name 
    info_dict['filename'] = xml_file

    # Parse the XML Tree
    for elem in root:
        # Get the image size
        if elem.tag == "size":
            image_size = []
            for subelem in elem:
                image_size.append(int(subelem.text))

            info_dict['image_size'] = tuple(image_size)

        # Get details of the bounding box 
        elif elem.tag == "object":
            bbox = {}
            for subelem in elem:
                if subelem.tag == "bndbox":
                    for subsubelem in subelem:
                        bbox[subsubelem.tag] = int(subsubelem.text)            
            info_dict['bboxes'].append(bbox)

    return info_dict

def convert_to_yolov5(info_dict):
    print_buffer = []

    # For each bounding box
    for b in info_dict["bboxes"]:
        # Transform the bbox co-ordinates as per the format required by YOLO v5
        b_center_x = (b["xmin"] + b["xmax"]) / 2 
        b_center_y = (b["ymin"] + b["ymax"]) / 2
        b_width    = (b["xmax"] - b["xmin"])
        b_height   = (b["ymax"] - b["ymin"])

        # Normalise the co-ordinates by the dimensions of the image
        image_w, image_h, image_c = info_dict["image_size"]  
        b_center_x /= image_w 
        b_center_y /= image_h 
        b_width    /= image_w 
        b_height   /= image_h 

        #Write the bbox details to the file 
        print_buffer.append("0 {:.3f} {:.3f} {:.3f} {:.3f}".format(b_center_x, b_center_y, b_width, b_height))

    # Name of the file which we have to save 
    save_file_name = info_dict["filename"].replace("xml", "txt")

    # Save the annotation to disk
    print("\n".join(print_buffer), file= open(save_file_name, "w"))

if __name__ == "__main__":
    # Get the annotations
    labels = [os.path.join(paths, f) for paths, _, files in os.walk('mini_kansas/labels/') for f in files if f[-3:] == "xml"]
    print(labels)
    
    # Convert and save the annotations
    for ann in tqdm(labels):
        info_dict = extract_info_from_xml(ann)
        convert_to_yolov5(info_dict)
    