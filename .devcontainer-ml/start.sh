#!/bin/bash
# Wait for Docker daemon to be ready
( \
  while ! docker info > /dev/null 2>&1; do \
    echo "Waiting for Docker daemon to start..."; \
    sleep 1; \
  done \
)
# switch docker buildx to use a container-based driver for multi-platform build support
docker buildx create --use --name mpbuilder --driver docker-container
docker buildx inspect mpbuilder --bootstrap

# keep the container running by executing any command passed to the container from Dockerfile
exec "$@"
