# Active Directory Disaster Recovery Procedures

## Purpose

This document defines recovery steps for critical Active Directory failures.

---

## Scenarios Covered

- Domain Controller failure
- SYSVOL corruption
- DFS Replication failure
- DNS service breakdown
- AD database inconsistencies

---

## Domain Controller Failure Recovery

### Steps

1. Verify remaining domain controller health
2. Transfer FSMO roles if required
3. Restore failed DC or rebuild from scratch
4. Rejoin to domain
5. Validate replication

---

## SYSVOL Recovery (DFSR)

### Non-authoritative Restore

- Stop DFSR service
- Set server to non-authoritative mode
- Restart DFSR service
- Force replication from healthy DC

---

## DNS Recovery

- Verify AD-integrated zones
- Restart DNS service
- Confirm SRV records exist
- Validate name resolution across domain

---

## Validation After Recovery

- repadmin /replsummary
- dcdiag /v
- net share (SYSVOL / NETLOGON)
- User authentication tests

---

## Recovery Principle

Always restore AD using a known healthy source. Never overwrite healthy replication data from a corrupted system.