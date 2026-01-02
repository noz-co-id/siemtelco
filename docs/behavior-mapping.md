# Log to Behavior Mapping (Testing)

This document defines how protocol logs are interpreted
into aggregated behavior events in SIEMTelco.

---

## 2G / GSM

| Source | Log Event | Behavior Class | Indicator |
|-----|----------|---------------|----------|
| OpenBTS | LOCATION.UPDATE | CELL_BEHAVIOR | LAC_VOLATILITY |
| OpenBTS | GSM.ATTACH | SUBSCRIBER_BEHAVIOR | ATTACH_RHYTHM |
| Osmocom | AUTH.FAIL | SUBSCRIBER_BEHAVIOR | AUTH_RETRY_ANOMALY |

---

## 4G / LTE

| Source | Log Event | Behavior Class | Indicator |
|------|----------|---------------|----------|
| Open5GS | NAS.REGISTRATION | SIGNALING_BEHAVIOR | REGISTRATION_RATE |
| Open5GS | NAS.DEREG | SIGNALING_BEHAVIOR | DEREG_BURST |

---

## Interpretation Rules

- A single log event never produces a behavior event
- Behavior is derived from frequency, rhythm, or correlation
- Output is always aggregated and time-window based
