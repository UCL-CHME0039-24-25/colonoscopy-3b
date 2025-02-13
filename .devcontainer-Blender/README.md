## Docker and data management

### Build
```
docker compose -f docker-compose.yml build #Building estimated time #

#$docker images
#REPOSITORY   TAG     IMAGE ID      CREATED         SIZE
#blender_colon        latest  <ID>          current_time    16.8GB
```

### Launch and test image
```
bash launch_image.bash
```

## Save the built image into a tar file
```
docker save -o blender_colon-image.tar blender_colon:latest
#blender_colon-image.tar [16G]
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
