# .devcontainer/Dockerfile
FROM python:3.11-slim

ENV PYTHONIOENCODING utf-8
ENV TZ="Asia/Tokyo"
ENV LANG=C.UTF-8
ENV LANGUAGE=en_US:en_US

# install tools
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    vim \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# install poetry
RUN curl -sSL https://install.python-poetry.org | python -

# set poetry path
ENV PATH /root/.local/bin:$PATH

# set poetry virtualization off
RUN poetry config virtualenvs.create false