## Docker and data management

### Build
```bash
docker compose -f docker-compose.yml build #Building estimated time for 17 items ~1473s
	# => => # Downloading torch-2.6.0-cp312-cp312-manylinux1_x86_64.whl (766.6 MB)
	# => => # Downloading nvidia_cublas_cu12-12.4.5.8-py3-none-manylinux2014_x86_64.whl (363.4 MB)
	# => => # Downloading nvidia_cuda_nvrtc_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (24.6 MB)
	# => => # Downloading nvidia_cuda_runtime_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl (883 kB)
	# => => # Downloading nvidia_cudnn_cu12-9.1.0.70-py3-none-manylinux2014_x86_64.whl (664.8 MB)
	# => => # Downloading nvidia_cusparselt_cu12-0.6.2-py3-none-manylinux2014_x86_64.whl (150.1 MB)
docker images
	#REPOSITORY   TAG     IMAGE ID      CREATED         SIZE
	#blender_colonoscopy        latest  <ID>          current_time    12GB
```

### Launch, test, stop and remove image
```
bash launch_image.bash
bash stop_container_and_removeit.bash
```

## Save the built image into a tar file
```
DATE=$(date --iso-8601)
docker save -o blender_colonoscopy_image_${DATE}.tar blender_colonoscopy:latest
#├── [ 11G]  blender_colonoscopy_image_2025-02-19.tar
tar -czvf blender_colonoscopy_image_${DATE}.tar.gz blender_colonoscopy_image_${DATE}.tar
#├── [7.0G]  blender_colonoscopy_image_2025-02-19.tar.gz
#tar -xzvf *.tar.gz extract files
```

## Copy image to airlock
```
scp -s -r -i key.pem blender_colon-image.tar <USER>@<IP>>:inbound/
rsync -avz -e "ssh -i  key.pem source/ user@remote:/path/to/destination/ # in case of an error and you want to pick up from where it stopped.
```
After scp is completed successfully, you need to close the airlock in the page https://sp.tre-dev.arc.ucl.ac.uk/
See more https://docs.tre.arc.ucl.ac.uk/guides/airlock-rsync/

## Using rsync to import bulk datasets
```
rsync -avz -e "ssh -i key.pem" $HOME/datasets/chest-xrays-indiana-university <USER>@<IP>>:inbound/
```

### Commands
```
docker images
docker ps
docker attach <ID>
docker stop <ID>
docker stop $(docker ps -a -q) # stop all containers
docker rename keen_einstein mycontainer
docker rmi --force <ID>
docker image prune -a #clean unused images
docker system prune -f --volumes #clean unused systems
docker inspect <container-name> (or <container-id>) 
```

### References
* [python-docker-image-build-install-required-packages](https://dev.to/behainguyen/python-docker-image-build-install-required-packages-via-requirementstxt-vs-editable-install-572j)
* [speed-up-your-docker-builds-with-cache-from](https://lipanski.com/posts/speed-up-your-docker-builds-with-cache-from)
* [docker-cheatsheets](https://github.com/cheat/cheatsheets/blob/master/docker)
