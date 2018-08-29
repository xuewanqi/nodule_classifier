FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

# install base tools
# Install some dependencies
RUN apt-get update && apt-get install -y \
		build-essential \
		unzip \
		swig \
		wget \
		pkg-config \
		zip \
		g++ \
		zlib1g-dev \
		cmake \
		curl \
		dh-autoreconf \
		vim \
		git \
		gfortran \
		libfreetype6-dev \
		libxft-dev \
		libncurses-dev \
		libopenblas-dev \
		libblas-dev \
		liblapack-dev \
		libatlas-base-dev \
		libcurl3-dev \
		python-dev \
		python-pydot \
		python-matplotlib \
		python-pip \
		python-numpy \
		python-pandas \
		python-sklearn \
		linux-headers-generic \
		linux-image-extra-virtual 

# Install SINGA from source
RUN git clone https://github.com/apache/incubator-singa.git /root/incubator-singa && \
    cd /root/incubator-singa && \
    git checkout f8cd7e3846a0eb016f2d511f826c18730eeda4cc && \
    mkdir build && \
    cd build && \
    cmake -DUSE_CUDA=ON -DUSE_MODULES=ON .. && \
    make && \
    cd python && \
    pip install .

# create directory
RUN mkdir /root/params

# Expose Ports for webservice (80)
EXPOSE 80

WORKDIR /root
CMD ['/bin/bash']