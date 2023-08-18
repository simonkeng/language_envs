FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y \
    build-essential \
    nasm \
    lsof \
    strace

RUN apt-get install -y \
    curl \
    dnsutils \
    iputils-ping \
    netcat \
    traceroute

RUN apt-get install -y \
    python3-dev \
    python3-pip

RUN apt-get install -y \
    neofetch \
    man-db \
    git \
    vim

RUN useradd -ms /bin/bash zelda
USER zelda
WORKDIR /home/zelda

