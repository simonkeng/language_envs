FROM centos

RUN yum update -y && \
    yum install -y \
        git \
        curl \
        java

RUN curl -O https://download.clojure.org/install/linux-install-1.10.2.796.sh && \
    chmod +x linux-install-1.10.2.796.sh && \
    ./linux-install-1.10.2.796.sh