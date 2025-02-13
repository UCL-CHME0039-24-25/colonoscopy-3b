FROM nvcr.io/nvidia/pytorch:24.12-py3

# Poetry's configuration:
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.3

# Init repos
RUN apt-get update
RUN apt-get install -y -q software-properties-common apt-transport-https
RUN add-apt-repository ppa:deadsnakes/ppa # to support newer python versions
RUN apt-get update

# Install dev dependencies
RUN apt-get install -y -q build-essential gcc dirmngr ca-certificates dkms curl git vim tmux unzip nano x11-xserver-utils
RUN apt-get install -y python3 python-is-python3 python3-virtualenv python3-pip rsync yq

# Install poetry
RUN curl -sSL https://install.python-poetry.org -o /tmp/install-poetry.py && python3 /tmp/install-poetry.py && rm /tmp/install-poetry.py
WORKDIR /workspace

# Take care of dependencies through package management
COPY pyproject.toml /workspace/pyproject.toml
# For those who are fond of requirements.txt
COPY dev/requirements.txt /workspace/requirements.txt
RUN poetry config virtualenvs.in-project true --local
RUN cat requirements.txt | xargs -I % sh -c 'poetry add "%"'
RUN poetry install --without dev --no-interaction

# Just to keep a container running indefinitely
ENTRYPOINT ["tail", "-f", "/dev/null"]
