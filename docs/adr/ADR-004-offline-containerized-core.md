# ADR-004: Offline, Containerized Core and Analytics

**Status:** Accepted  
**Date:** 2026-01-02  

---

## Context

Mobile core network components and analytics systems are complex and interdependent.
Running them directly on host systems increases risk and reduces reproducibility.

Additionally, network-connected environments introduce the possibility of
unintended interaction with live infrastructure.

---

## Decision

All core network components and SIEMTelco analytics are deployed in
**locally isolated Docker containers**, operating in a **fully offline environment**.

All software is built and compiled **from local source code**.

---

## Design Principles Applied

### 1. Isolation

- Docker networks are internal-only
- No outbound or inbound public connectivity

---

### 2. Reproducibility

- Controlled build environment
- Deterministic dependency management

---

### 3. Security

- Reduced attack surface
- No accidental data exfiltration

---

## Consequences

### Positive

- Strong safety guarantees
- Improved auditability
- Suitable for regulated research environments

### Trade-offs

- Manual dependency management
- No automatic updates

These trade-offs are acceptable for an offline research platform.

---

## Summary

Offline containerization ensures SIEMTelco remains isolated, reproducible,
and safe for advanced telecom security research.
