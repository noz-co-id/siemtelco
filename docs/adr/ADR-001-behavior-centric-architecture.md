# ADR-001: Behavior-Centric Architecture

**Status:** Accepted  
**Date:** 2026-01-02  

---

## Context

Traditional SIEM systems are designed around events, alerts, and signatures.
While effective for IT systems, this approach is insufficient for mobile telecommunications networks.

In telco environments, security issues often emerge as:
- gradual signaling drift
- abnormal mobility patterns
- systemic protocol misuse
- infrastructure-level anomalies

These characteristics are not reliably detected through isolated events.

---

## Decision

SIEMTelco adopts a **behavior-centric architecture** as its foundational design principle.

The system analyzes **aggregated network behavior** derived from protocol-aligned telemetry,
rather than relying on individual events or static detection rules.

---

## Design Principles Applied

### 1. Behavior Over Events

- Logs and events are treated as raw signals
- Meaning is derived through aggregation and correlation
- Detection focuses on *how the network behaves over time*

---

### 2. Network-Level Perspective

- Analysis targets cells, procedures, and systems
- Individual subscribers are not the subject of analysis
- Results describe systemic conditions, not isolated incidents

---

### 3. Research-Oriented Output

SIEMTelco outputs:
- behavior classes
- anomaly indicators
- confidence scores

It does not output:
- alert floods
- per-event notifications
- enforcement actions

---

## Consequences

### Positive

- Improved detection of slow or distributed anomalies
- Reduced false positives
- Alignment with privacy and data minimization goals

### Trade-offs

- Less suitable for real-time operational SOC workflows
- Requires behavior modeling effort

These trade-offs are acceptable given the research focus.

---

## Summary

This decision establishes behavior as the **primary unit of analysis** in SIEMTelco,
forming the conceptual foundation for all subsequent architectural decisions.
