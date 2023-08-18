FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y \
    build-essential \
    lsof \
    strace

RUN apt-get install -y \
    man-db \
    vim

RUN useradd -ms /bin/bash zelda
USER zelda
WORKDIR /home/zelda

