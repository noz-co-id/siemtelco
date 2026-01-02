# ADR-002: Mandatory RF Emulation Using SDR

**Status:** Accepted  
**Date:** 2026-01-02  

---

## Context

Mobile network behavior is strongly influenced by radio-layer conditions, including:
- signal quality
- timing advance
- power control
- interference
- handover dynamics

Pure IP-based simulations cannot reproduce these effects accurately.

---

## Decision

All Radio Access Network (RAN) components and endpoints in SIEMTelco MUST operate through
**RF emulation using Software Defined Radio (SDR)**.

USRP B2901 is selected as the reference SDR platform.

---

## Design Principles Applied

### 1. RF as a Source of Truth

- RF behavior directly influences protocol state machines
- Accurate behavior analysis requires RF realism

---

### 2. Laboratory Safety

- RF emulation is confined to shielded or attenuated environments
- No interaction with public mobile networks is permitted

---

### 3. Reproducibility

- SDR-based experiments can be repeated with controlled parameters
- Results are scientifically defensible

---

## Consequences

### Positive

- High-fidelity behavior modeling
- Realistic mobility and signaling behavior
- Avoidance of misleading conclusions

### Trade-offs

- Requires specialized hardware
- Increases setup complexity

These trade-offs are intentional and justified by research goals.

---

## Summary

Mandatory RF emulation ensures that SIEMTelco behavior analysis reflects real-world
mobile network dynamics without compromising safety or legality.
