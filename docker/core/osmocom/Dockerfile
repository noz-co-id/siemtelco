FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    autoconf \
    automake \
    libtool \
    pkg-config \
    libtalloc-dev \
    libpcsclite-dev \
    libgnutls28-dev \
    libdbi-dev \
    libdbd-sqlite3 \
    libssl-dev \
    libmnl-dev \
    libnl-3-dev \
    libnl-genl-3-dev \
    libmicrohttpd-dev \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/osmocom

# ===== LIBRARIES =====
RUN git clone https://github.com/peduli-or-id/libosmocore.git && \
    cd libosmocore && autoreconf -fi && ./configure && make -j$(nproc) && make install

RUN git clone https://github.com/peduli-or-id/libosmo-abis.git && \
    cd libosmo-abis && autoreconf -fi && ./configure && make -j$(nproc) && make install

RUN git clone https://github.com/peduli-or-id/libosmo-netif.git && \
    cd libosmo-netif && autoreconf -fi && ./configure && make -j$(nproc) && make install

RUN git clone https://github.com/peduli-or-id/libgtpnl.git && \
    cd libgtpnl && autoreconf -fi && ./configure && make -j$(nproc) && make install

# ===== CORE =====
RUN git clone https://github.com/peduli-or-id/osmo-hlr.git && \
    cd osmo-hlr && autoreconf -fi && ./configure && make -j$(nproc) && make install

RUN git clone https://github.com/peduli-or-id/osmo-sgsn.git && \
    cd osmo-sgsn && autoreconf -fi && ./configure && make -j$(nproc) && make install

RUN git clone https://github.com/peduli-or-id/osmo-ggsn.git && \
    cd osmo-ggsn && autoreconf -fi && ./configure && make -j$(nproc) && make install

RUN ldconfig

COPY config /etc/osmocom
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
