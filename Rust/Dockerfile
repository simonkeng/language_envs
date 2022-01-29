FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# update debian packages, install curl
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get install -y git && \
    apt-get install -y curl && \
    apt-get clean;

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

ENV PATH="/root/.cargo/bin:${PATH}"
ENV USER="ferrous"

RUN mkdir -p /scr
WORKDIR /scr

RUN rustup update
CMD ["rustc", "--version"]

