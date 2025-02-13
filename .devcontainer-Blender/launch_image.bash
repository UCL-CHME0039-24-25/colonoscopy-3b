docker run -v /path/to/folder/with/blend_files/:/blender_colon/datasets/blend_files/ --name blender_colon_container --detach blender_colon:latest
docker exec -it blender_colon_container bash

# docker run -d -v <local path>:<container-path> <docker-image-name>
# docker exec -it <> bash <docker-container-id> bash #or <NAME> bash

# /Users/ruaridhgollifer/repos/github.com/Blender_Randomiser/blend_files