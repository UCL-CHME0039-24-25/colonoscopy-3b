docker build -f dockerfile.yolo -t updated-tre-image .  # build the image - change dockerfile.yolo to required dockerfile
docker save -o updated-tre-image.tar updated-tre-image