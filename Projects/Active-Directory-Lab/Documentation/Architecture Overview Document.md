# Active Directory Lab – Architecture Overview

## Purpose

This document describes the logical and physical architecture of the Enterprise Active Directory Infrastructure Lab, designed to simulate a production Windows Server environment.

---

## Domain Structure

- Domain Name: homelab.local
- Forest Functional Level: Windows Server 2019
- Domain Functional Level: Windows Server 2019

---

## Core Infrastructure Components

### Domain Controllers

- DC01: Primary Domain Controller
- DC02: Secondary Domain Controller (replica for redundancy)

Responsibilities:
- Authentication (Kerberos / NTLM)
- Directory services
- DNS hosting
- Group Policy processing
- Replication (AD DS + SYSVOL via DFSR)

---

### Client Systems

- WIN10-CLIENT: Domain-joined workstation
- Used for:
  - GPO validation
  - Authentication testing
  - Endpoint policy enforcement

---

## Network Services

### DNS
- Active Directory-integrated DNS zones
- Forward and reverse lookup zones
- Supports AD replication and service location (SRV records)

### DHCP
- Dynamic IP allocation for clients
- Reservations for infrastructure systems
- DNS auto-registration enabled

---

## Replication Model

- Multi-master Active Directory replication between DC01 and DC02
- DFSR used for SYSVOL synchronization
- Replication monitored using repadmin and dcdiag

---

## Security Layer

- Microsoft Defender for Endpoint enabled
- Group Policy-based security enforcement
- Firewall rules centrally managed via GPO
- Audit logging enabled for all critical actions

---

## Summary

This lab replicates enterprise-level identity infrastructure with redundancy, centralized management, and security enforcement to simulate real-world IT and SOC environments.
