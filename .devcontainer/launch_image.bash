LOCAL_DATA_PATH="/path/to/folder/with/blend_files/blend_files/"
docker run -v ${LOCAL_DATA_PATH}:/blender_colonoscopy/datasets/blend_files/ --name blender_colonoscopy_container --detach blender_colonoscopy:latest
docker exec -it blender_colonoscopy_container bash
