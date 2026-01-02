# ADR-005: Strict Non-Deployment Policy on Real Networks

**Status:** Accepted  
**Date:** 2026-01-02  

---

## Context

Telecommunications infrastructure is highly regulated.
Testing experimental systems on live networks may cause:
- service disruption
- regulatory violations
- unintended interference

SIEMTelco is designed for research, not production deployment.

---

## Decision

SIEMTelco MUST NOT be deployed, tested, or connected to real operator networks.

The system is limited to:
- laboratory environments
- shielded RF setups
- licensed test facilities

---

## Design Principles Applied

### 1. Legal Compliance

- Avoids violation of telecommunications law
- Respects spectrum regulation

---

### 2. Ethical Responsibility

- Prevents impact on public users
- Avoids unintended service degradation

---

### 3. Clear Scope Definition

- Research and education only
- Not a deployment framework

---

## Consequences

### Positive

- Clear legal and ethical boundaries
- Reduced risk for contributors and users
- Increased trust from regulators and reviewers

### Trade-offs

- No validation on live production networks

This limitation is intentional and non-negotiable.

---

## Summary

This decision enforces a strict boundary between research and production,
ensuring SIEMTelco is used responsibly and lawfully.
