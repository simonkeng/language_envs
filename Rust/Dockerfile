FROM debian

ENV DEBIAN_FRONTEND=noninteractive

# update debian packages, install curl
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get install -y git && \
    apt-get install -y curl && \
    apt-get install -y wget && \
    apt-get install -y vim && \
    apt-get install -y fish && \
    apt-get clean;


RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

ENV PATH="/root/.cargo/bin:${PATH}"
ENV USER="gandalf"

RUN rustup update
CMD ["rustc", "--version"]

WORKDIR /root
RUN git clone https://github.com/oh-my-fish/oh-my-fish
RUN cd oh-my-fish && bin/install --offline --noninteractive

RUN ["/usr/bin/fish", "-c", "omf update omf install toaster"]
