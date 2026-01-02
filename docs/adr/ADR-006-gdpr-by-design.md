# ADR-006: GDPR-by-Design and Data Minimization

**Status:** Accepted  
**Date:** 2026-01-02  

---

## Context

SIEMTelco processes telemetry derived from mobile network infrastructure for the purpose of **behavior analysis and security research**.

Telecommunications data can potentially include personal or sensitive identifiers (e.g., IMSI, IMEI, MSISDN).  
Improper handling of such data may violate data protection regulations, including the General Data Protection Regulation (GDPR).

To ensure legal, ethical, and research-safe operation, privacy requirements must be enforced **by architecture**, not by policy alone.

---

## Decision

SIEMTelco adopts a **GDPR-by-Design** approach with strict **data minimization principles** applied across all components.

The system is architected such that:

- Personal data is **not required** for functionality
- Identifiers are **never stored in clear form**
- Analysis operates on **aggregated and derived behavior**, not individual users

---

## Design Principles Applied

### 1. Data Minimization

Only data strictly necessary for behavior analysis is processed.

- No subscriber profiling
- No identity tracking
- No long-term session correlation

Raw protocol logs are treated as **ephemeral inputs** and are not considered final artifacts.

---

### 2. Anonymization and Pseudonymization

When identifiers are present for protocol correctness:

- IMSI, IMEI, MSISDN are:
  - hashed
  - masked
  - or replaced with synthetic identifiers
- No reversible mapping is stored

This ensures that individual subjects cannot be re-identified.

---

### 3. Aggregation Over Individual Observation

SIEMTelco outputs:

- behavior classes
- statistical indicators
- confidence scores

It does **not** output:
- individual subscriber timelines
- per-user alerts
- personal movement patterns

---

### 4. Offline and Isolated Operation

The system operates in a **fully offline laboratory environment**:

- No connection to public networks
- No ingestion of live operator traffic
- No external data exchange

This eliminates the risk of unauthorized data exposure.

---

### 5. Purpose Limitation

SIEMTelco is designed exclusively for:

- research
- education
- simulation
- security analytics development

It is explicitly **not designed** for:
- surveillance
- monitoring individuals
- commercial data processing
- lawful interception systems

---

## Consequences

### Positive

- GDPR compliance by design
- No requirement for consent management
- Reduced legal and ethical risk
- Increased trust for academic and regulatory review

### Trade-offs

- No per-subscriber analytics
- No identity-based correlation
- Focus limited to systemic and network-level behavior

These trade-offs are intentional and aligned with the project’s goals.

---

## Compliance Statement

By design, SIEMTelco aligns with key GDPR principles:

- Article 5(1)(c) – Data minimization  
- Article 25 – Data protection by design and by default  

No Data Protection Impact Assessment (DPIA) is required for typical laboratory use, as no personal data processing occurs.

---

## Summary

This decision ensures that SIEMTelco remains:

- privacy-preserving
- legally defensible
- ethically sound
- suitable for open research

GDPR compliance is treated as a **foundational architectural property**, not an optional feature.
