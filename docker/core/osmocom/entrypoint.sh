#!/bin/bash
set -e

echo "[CORE-2G] Starting Osmocom Core (HLR + SGSN + GGSN)"

osmo-hlr -c /etc/osmocom/hlr.cfg &
sleep 2
osmo-sgsn -c /etc/osmocom/sgsn.cfg &
sleep 2
osmo-ggsn -c /etc/osmocom/ggsn.cfg &

wait
