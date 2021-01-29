FROM centos

RUN yum -y update && \
    yum -y install gcc && \
    yum -y install gcc-c++ && \
    yum clean all

RUN mkdir /scr
WORKDIR /scr