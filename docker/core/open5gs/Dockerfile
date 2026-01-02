FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git \
    meson \
    ninja-build \
    build-essential \
    pkg-config \
    libyaml-dev \
    libmongoc-dev \
    libbson-dev \
    libssl-dev \
    libnghttp2-dev \
    libmicrohttpd-dev \
    libcurl4-openssl-dev \
    libtins-dev \
    mongodb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN git clone https://github.com/peduli-or-id/open5gs.git

WORKDIR /opt/open5gs
RUN meson build && ninja -C build && ninja -C build install

COPY config /etc/open5gs
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
