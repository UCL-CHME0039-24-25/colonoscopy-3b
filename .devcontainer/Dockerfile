FROM ubuntu:24.04
FROM python:3.12

# ARGs passed by docker compose, ENV defined for local use
ARG USER
ENV USERNAME=${USER}

ENV DEBIAN_FRONTEND noninteractive

SHELL ["/bin/bash", "-cu"]

RUN apt-get update && apt-get install -y python3 python3-pip sudo gdebi
RUN apt install -y vim vim-gtk3
# following three lines from https://github.com/PetrusNoleto/Error-in-install-cisco-packet-tracer-in-ubuntu-23.10-unmet-dependencies
RUN wget https://github.com/PetrusNoleto/Error-in-install-cisco-packet-tracer-in-ubuntu-23.10-unmet-dependencies/releases/download/CiscoPacketTracerFixUnmetDependenciesUbuntu23.10/libegl1-mesa_23.0.4-0ubuntu1.22.04.1_amd64.deb
RUN wget https://github.com/PetrusNoleto/Error-in-install-cisco-packet-tracer-in-ubuntu-23.10-unmet-dependencies/releases/download/CiscoPacketTracerFixUnmetDependenciesUbuntu23.10/libgl1-mesa-glx_23.0.4-0ubuntu1.22.04.1_amd64.deb
RUN  sudo gdebi libegl1-mesa_23.0.4-0ubuntu1.22.04.1_amd64.deb libgl1-mesa-glx_23.0.4-0ubuntu1.22.04.1_amd64.deb
# Update and install Blender
RUN apt-get install -y blender

## python package build
WORKDIR /blender_laparoscopy
COPY . /blender_laparoscopy
RUN pip install --upgrade pip
RUN pip install --editable ".[test, learning]"
## Blender setup
#Set the default command to run Blender
CMD ["blender"]
RUN /usr/bin/python3.11 -m pip install numpy --break-system-packages
RUN git clone https://github.com/UCL/Blender_Randomiser.git

ENTRYPOINT ["tail", "-f", "/dev/null"]

# Set default shell to /bin/bash
SHELL ["/bin/bash", "-cu"]
