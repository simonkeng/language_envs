FROM ubuntu

RUN apt-get update && \
    apt-get install -y lua5.3 && \
    apt-get install -y fish && \
    apt-get install -y curl && \
    apt-get install -y git && \
    apt-get install -y autoconf && \
    apt-get install -y build-essential && \
    apt-get install -y autotools-dev && \
    apt-get install -y automake && \
    apt-get install -y libtool && \
    apt-get install -y pkg-config && \
    apt-get install -y libdevil-dev && \
    apt-get install -y libfreetype6-dev && \
    apt-get install -y libluajit-5.1-dev && \
    apt-get install -y libphysfs-dev && \
    apt-get install -y libsdl2-dev && \
    apt-get install -y libopenal-dev && \
    apt-get install -y libogg-dev && \
    apt-get install -y libvorbis-dev && \
    apt-get install -y libflac-dev && \
    apt-get install -y libflac++-dev && \
    apt-get install -y libmodplug-dev && \
    apt-get install -y libmpg123-dev && \
    apt-get install -y libmng-dev && \
    apt-get install -y libturbojpeg0 && \
    apt-get install -y libtheora-dev && \
    apt-get clean

RUN add-apt-repository ppa:bartbes/love-stable

RUN ln -sf /usr/bin/lua5.3 /usr/bin/lua

ENV USER="vorelian"
WORKDIR /root

RUN git clone https://github.com/oh-my-fish/oh-my-fish
RUN cd oh-my-fish && bin/install --offline --noninteractive

RUN git clone https://github.com/love2d/love.git
RUN cd /root/love/ && /root/love/platform/unix/automagic && ./configure && make

