# 🛰️ SIEMTELCO – Telecom Security & Event Intelligence Platform

**SIEMTELCO** is an open-source research initiative integrating **telecommunication network stacks** (OpenBTS, Osmocom, srsRAN) with a **Security Information and Event Management (SIEM)** system to enable *telco-aware* threat detection, anomaly monitoring, and fraud analytics.

---

## 🔍 Overview

SIEMTELCO bridges the gap between **telecommunication telemetry** and **cybersecurity analytics**.

It enables real-time observation and correlation of **endpoint**, **cell**, and **kernel-level** behaviours in mobile networks, supporting use cases such as:

- 📡 Signalling anomaly detection (Attach, PDP Context, CCCH abuse)
- ⚡ Real-time endpoint–cell behaviour correlation
- 🧩 Kernel-level process monitoring and anomaly detection
- 🔐 Telecom fraud, rogue base-station, and IMSI-catcher analysis

Designed for research, private network operators, and telecom engineers exploring **converged telecom-security architectures**.

---

## 🧩 Architecture

<img width="2232" height="598" alt="lab arsitektur siem" src="https://github.com/user-attachments/assets/df7c19d7-badc-4c35-a886-77eb62dc651d" />

SIEMTELCO integrates multiple open-source components into a modular framework:

| Layer | Component | Description |
|:------|:-----------|:-------------|
| **Radio Access / Core** | OpenBTS, Osmocom, srsRAN | Provides GSM/4G/5G signalling and network context |
| **Telemetry & Message Bus** | Fluentd / Kafka | Handles event ingestion and distribution |
| **SIEM Core** | Ella-core / Elasticsearch | Event correlation, anomaly detection, and analytics |
| **SOC & Visualization** | Grafana / Kibana | Dashboards for network and security event monitoring |

### Alignment with ISO/IEC 27001:2022 Controls

| Control Area | Description |
|:--------------|:-------------|
| A.12.4 | Continuous monitoring and log analysis |
| A.16 | Security incident management |
| A.9 / A.12 | Access control and operational security |
| A.8 / A.10 | Data integrity and protection mechanisms |

---

## ⚙️ Key Features

- 🛰️ **Telco-aware SIEM pipeline** – native parsing of signalling and RAN logs  
- ⚡ **Real-time correlation engine** – links events between UE, BTS, and kernel domains  
- 🧠 **Behavioural anomaly analysis** – machine-assisted pattern recognition (in progress)  
- 🔐 **Regulatory alignment** – ISO 27001, NIST SP 800-53, GDPR, and CCPA readiness  
- 🧾 **Fraud & intrusion detection** – detects rogue cells, fake BTS, and DoS patterns  

---

## 🧠 Research Areas

- Telecom cybersecurity & signalling analysis  
- Edge computing for event processing  
- Network intelligence and smart telemetry  
- Incident response automation in telecom SOC environments  

---

## 📘 Documentation

| Resource | Description |
|:----------|:-------------|
| [`Silence On The Wire PDF`](./Silence%20On%20The%20Wire%20PDF.pdf) | Whitepaper – passive signalling analysis |
| [`whitepaper_imsicatchers_eff_0.pdf`](./whitepaper_imsicatchers_eff_0.pdf) | Whitepaper – IMSI catcher threat evaluation |
| `/docs/` | Architecture notes, lab topology, and deployment guidance |

---

## 🧩 Licensing & Contribution

This project is released under **CC0-1.0 (Public Domain)**.

Contributions are welcome — especially from researchers and engineers focusing on:

- Telecom network security  
- 5G/IoT signalling analytics  
- SIEM integration and edge intelligence  

To contribute:
1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/awesome-feature`)  
3. Commit changes (`git commit -m 'Add feature'`)  
4. Push to branch (`git push origin feature/awesome-feature`)  
5. Create a Pull Request 🚀

---

## 🌍 Project Vision

> “To build an open, unified platform that connects telecom signalling intelligence  
> with modern cybersecurity analytics — enabling smarter, real-time protection for next-generation networks.”

---

## 📫 Contact & Collaboration

For research or collaboration inquiries:  
**Linkedin:** [Tri](https://linkedin.com/in/noz)  
**GitHub:** [noz-co-id/siemtelco](https://github.com/noz-co-id/siemtelco)

---

### example log analysis

* Activate PDP Context Accept Procedures - https://www.linkedin.com/pulse/mapping-metadata-related-3gpp-procedures-tri--3yluc
* SGSN Received AttachRequest Procedures - https://www.linkedin.com/pulse/sgsn-received-attachrequest-procedures-tri--pe9yc
* GSM CCCH - Abused System Information Type 6 - https://www.linkedin.com/pulse/gsm-ccch-abused-system-information-type-6-tri--3kcuc
* GSM CCCH — Abused Paging Request Type 1 - https://www.linkedin.com/pulse/gsm-ccch-abused-paging-request-type-1-tri--zvtrc/
* GSM CCCH - Abused System Information Type 4 - https://www.linkedin.com/pulse/gsm-ccch-abused-system-information-type-4-tri-s-fmehc
* SGSN : Received Routing Area Update Request - https://www.linkedin.com/pulse/sgsn-received-routing-area-update-request-nozberkarya-ut9qc/
* Potentially dangerous mode on OpenBTS: 0755 - https://www.linkedin.com/pulse/potentially-dangerous-mode-openbts-0755-tri-s-rb2xc/

Halu
* Deep Thought about Signaling - https://www.linkedin.com/pulse/deep-thought-signaling-tri--ahvgc/

---

### 🧱 Status

> ⚙️ **Current Phase:** Research & Prototype  
> 🧪 **Next Step:** Integration with live Open5GS + Grafana SIEM visualization  
> 📦 **Releases:** Coming soon

---

_© 2025 – SIEMTELCO Project (CC0-1.0)._

