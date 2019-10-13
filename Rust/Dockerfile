FROM debian

# update debian packages, install curl
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y gcc && \
    apt-get clean;

# install cargo (rustup, rustc)
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

# add rust CLI tools to PATH
ENV PATH="/root/.cargo/bin:${PATH}"
ENV USER="guy"

RUN rustup update
CMD ["rustc", "--version"]