This is an example pipeline on how to convert output from Blender Randomiser to correct format labelling in preperation of fine tuning polyps detection using YOLOv7

# Data Preperation
Once the segmentation of polyps are obtained. Use find_bounding_box.ipynb to output the bounding box information as text files.

show_bbox.ipynb can be used to show if the correct bounding boxes have been converted.

# Run Model on Google Colab
Download and run the notebook run_yolov7.ipynb (src/notebooks).

All file paths are written in line with the mini synthetic dataset uploaded to the shared Google Drive:
https://drive.google.com/drive/folders/1fnNzX_f9nYCxA347kb-HlZQIuCuCV2Zh?usp=drive_link




### High-level overview outlined below:

Mount drive:
``` shell
from google.colab import drive
drive.mount('/content/gdrive')
%cd /content/gdrive/MyDrive
```

Clone this repo:
``` shell
#If you've already cloned the repo in a previous session and it's in your Google Drive, you don’t need to clone it again

!git clone https://github.com/WongKinYiu/yolov7
```

Navigate to repo folder and install requirements
``` shell
%cd yolov7
!pip install -r requirements.txt
```

Train model
``` shell
#Update name (--name colon_run_X) with each run

!python train.py --epochs 100 --device 0 --workers 8 --batch-size 32 --data /content/gdrive/MyDrive/Colab_Notebooks/Group_Project/polyp_people/code/ml_code/data_yaml_files/mini_synthetic.yaml --img 512 512 --cfg config_train_yolov7.yaml --weights /content/gdrive/MyDrive/Colab_Notebooks/Group_Project/polyp_people/code/ml_code/yolov7_training.pt --name colon_run_X --hyp data/hyp.scratch.custom.yaml
```
Test model
``` shell
#Update weights path (--weights runs/train/colon_run_X/) with name as per previous cell with each run
#Update validation run name (--name colon_test_X)

!python test.py --data /content/gdrive/MyDrive/Colab_Notebooks/Group_Project/polyp_people/code/ml_code/data_yaml_files/mini_synthetic.yaml --img 512 --batch 32 --conf 0.001 --iou 0.65 --device 0 --weights runs/train/colon_run_X/weights/best.pt --name colon_test_X
```

Inference (generate bounding boxes)
``` shell
#Update source file path (--source) to image or folder of images for which you want to generate bounding boxes.
#Update weights path (--weights runs/train/colon_run_X/) for saved model.

!python detect.py --source /content/gdrive/MyDrive/Colab_Notebooks/Group_Project/polyp_people/data/Synthetic/mini_synthetic_data/images/valid/ --weights runs/train/colon_run_X/weights/best.pt --conf 0.25 --name polyp_detect_X
```

Save model
``` shell
#Update model path (colon_run_X) accordingly
#The first file path specifies where the file/folder is currently located
#The second file path specifies where it is to be saved down

#Save best model weights
!cp runs/train/colon_run_X/weights/best.pt /content/gdrive/MyDrive/Colab_Notebooks/Group_Project/polyp_people/runs/train/colon_run_X.pt

#Save test folder
!cp -r runs/test/colon_test_X /content/gdrive/MyDrive/Colab_Notebooks/Group_Project/polyp_people/runs/test/colon_test_X

#Save images with bounding boxes (inference)
!cp -r runs/detect/polyp_detect_X /content/gdrive/MyDrive/Colab_Notebooks/Group_Project/polyp_people/runs/detect/colon_detect_X
```