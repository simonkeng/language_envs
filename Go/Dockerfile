FROM golang

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \ 
    apt-get install -y software-properties-common && \
    apt-add-repository ppa:fish-shell/release-3 && \
    apt-get install -y fish

RUN go get github.com/urfave/cli
RUN go get github.com/kr/pretty

RUN git clone https://github.com/oh-my-fish/oh-my-fish
RUN cd oh-my-fish && bin/install --offline --noninteractive

RUN ["/usr/bin/fish", "-c", "omf update && omf install batman"]




