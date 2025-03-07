LOCAL_DATA_PATH="C:/Users/Alice.Piller/OneDrive - AHRI/Documents/_M.Sc. Health Data Science/Course work/Term 2/AIHGP - Artificial Intelligence in Healthcare Group Project/Blender"
docker run -v "${LOCAL_DATA_PATH}:/blender_colonoscopy/datasets/blend_files/" --name blender_colonoscopy_container --detach blender_colonoscopy:latest
docker exec -it blender_colonoscopy_container bash
