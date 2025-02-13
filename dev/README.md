# Using Docker to reconstruct the project's target environment

The command line instructions shown here are based on a Linux-based development environment. The .devcontainer at the root of this project template defines and provisions (through VS Code) all the dependencies necessary to run these commands. It is assumed that you run these commands by accessing the command line prompt either through the VS Code Terminal or through the Docker shell of the .devcontainer run by VS Code.

## Accessing the command line prompt
1. **VS Code Terminal:**
    ```
    View -> Terminal
    ```
2. **Execute a bash shell inside the running container:**
    ```sh
    docker exec -it <container-name> bash
    ```
    Replace `<container-name>` with the name or ID of the running container you want to access.

## Checking the Linux distro
Currently, the .devcontainer provisions Debian Linux, and running ```lsb_release -a``` should return:
```sh
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 12 (bookworm)
Release:        12
Codename:       bookworm
```

## Building and running the Docker container
We need to switch the context a little bit for dealing with the container defined under ```dev```. Here, we are building and running a container inside the container defined by ```.devcontainer```.

1. **Build the Docker container:**
    ```sh
    docker-compose build
    ```

2. **Start the Docker container in detached mode:**
    ```sh
    docker-compose up -d
    ```

## Saving and loading docker images

1. **Save a Docker image as a tar file:**
    ```sh
    docker save -o <path-to-save-tar-file> <image-name>
    ```
    Replace `<path-to-save-tar-file>` with the desired path and filename for the tar file, and `<image-name>` with the name of the Docker image you want to save.

2. **Load a Docker image from a tar file:**
    ```sh
    docker load -i <path-to-tar-file>
    ```
    Replace `<path-to-tar-file>` with the path to the tar file you want to load.
