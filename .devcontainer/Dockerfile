FROM ubuntu:24.04
FROM python:3.12
#FROM nvidia/cuda:12.6.3-cudnn-runtime-ubuntu24.04

# ARGs passed by docker compose, ENV defined for local use
ARG USER
ENV USERNAME=${USER}

ENV DEBIAN_FRONTEND noninteractive

SHELL ["/bin/bash", "-cu"]

RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt install -y vim vim-gtk3
RUN apt install -y libegl1-mesa
# Update and install Blender
RUN apt-get install -y blender

# Set the default command to run Blender
CMD ["blender"]

RUN blender --version
RUN /usr/bin/python3.11 -m pip install numpy --break-system-packages
WORKDIR /blender_colon
COPY . /blender_colon
RUN git clone https://github.com/UCL/Blender_Randomiser.git
RUN pip install --upgrade pip
RUN pip install --editable ".[test, learning]"

ENTRYPOINT ["tail", "-f", "/dev/null"]

# Set default shell to /bin/bash
SHELL ["/bin/bash", "-cu"]
