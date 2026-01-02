#!/bin/bash
set -e

echo "[CORE-45G] Starting Open5GS (Testing Mode)"

mongod --fork --logpath /var/log/mongodb.log

open5gs-nrfd &
open5gs-amfd &
open5gs-smfd &
open5gs-upfd &
open5gs-ausfd &
open5gs-udmd &
open5gs-pcfd &
open5gs-nssfd &
open5gs-bsfd &

wait
