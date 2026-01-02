# ADR-003: Use of Emulated Endpoints Instead of Real Devices

**Status:** Accepted  
**Date:** 2026-01-02  

---

## Context

Using real mobile devices in security research introduces risks related to:
- personal data exposure
- legal compliance
- lack of experimental control

Additionally, real devices are difficult to instrument for deep protocol visibility.

---

## Decision

SIEMTelco uses **emulated user equipment (UE)** exclusively.
Supported UE implementations include **OsmocomBB** and **srsUE**.

Real subscriber devices are explicitly excluded.

---

## Design Principles Applied

### 1. Privacy Preservation

- No real user data is involved
- No consent or identity management is required

---

### 2. Experimental Control

- Deterministic behavior generation
- Repeatable test scenarios
- Full protocol visibility

---

### 3. Ethical Research Practice

- Avoids unintended impact on individuals
- Aligns with responsible research standards

---

## Consequences

### Positive

- GDPR compliance by design
- Reduced legal and ethical risk
- Improved reproducibility

### Trade-offs

- Certain vendor-specific UE behaviors are not represented

This limitation is acceptable for systemic behavior analysis.

---

## Summary

Emulated endpoints enable safe, controlled, and privacy-preserving experimentation,
aligned with SIEMTelco’s research-first objectives.
