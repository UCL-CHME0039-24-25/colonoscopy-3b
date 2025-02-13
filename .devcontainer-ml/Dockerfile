#FROM mcr.microsoft.com/devcontainers/python:3
FROM ubuntu:24.04

# ARGs passed by docker compose, ENV defined for local use
ARG USER
ENV USERNAME=${USER}

ARG HOST_UID
ENV HOST_UID=${HOST_UID}

ENV DEBIAN_FRONTEND=noninteractive

# Init repos
RUN apt-get update
RUN apt-get install -y software-properties-common build-essential
RUN add-apt-repository ppa:deadsnakes/ppa # to support newer python versions
RUN apt-get update
# Install dependencies
RUN apt-get install -y -q curl wget git gcc vim tmux unzip nano x11-xserver-utils rsync yq nodejs npm
RUN apt-get install -y python3 python-is-python3 python3-virtualenv python3-pip
RUN npm install -g mustache

# Install Poetry
# Poetry's configuration:
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.3
RUN curl -sSL https://install.python-poetry.org -o /tmp/install-poetry.py && python3 /tmp/install-poetry.py && rm /tmp/install-poetry.py

# Add repo for docker.ce
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update
RUN apt-get install -y docker.ce

# Post installation clean up
RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a user with the same name and uid as the host user
RUN useradd -u ${HOST_UID} --create-home ${USERNAME} -G docker

# Ensure Poetry cache directory is writable by the user
RUN mkdir -p /var/cache/pypoetry && \
    chown -R $USERNAME:$USERNAME /var/cache/pypoetry

# Copy init script
COPY .devcontainer/start.sh /usr/local/bin/start.sh
RUN chmod 777 /usr/local/bin/start.sh

ENV SHELL /bin/bash
USER ${USERNAME}
WORKDIR /home/${USERNAME}/workspace/
RUN git config --global --add safe.directory /home/${USERNAME}/workspace

# Produce a pyproject.toml based on the mustache template and the input json
COPY pyproject.toml.mustache .
COPY pyproject.json .
RUN mustache pyproject.json pyproject.toml.mustache > pyproject.toml

# Install Python dependencies
RUN touch README.md \
    && mkdir -p src/python_package \
    && poetry install --without dev --no-interaction

ENV PATH $PATH:/home/${USERNAME}/.local/bin

# Copy the vimrc file for consistent vim settings
COPY .devcontainer/vimrc /home/${USERNAME}/.vimrc

# Perform system-wide init, and keep the container running indefinitely
ENTRYPOINT ["/usr/local/bin/start.sh"]
CMD ["tail", "-f", "/dev/null"]