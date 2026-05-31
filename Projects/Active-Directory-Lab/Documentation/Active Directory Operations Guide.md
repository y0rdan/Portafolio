# Active Directory Operations Guide

## Purpose

This document provides operational procedures for managing Active Directory within the lab environment.

---

## User Management

### Create User

Users are created using PowerShell or Active Directory Users and Computers (ADUC).

Key fields:
- Username (sAMAccountName)
- UPN (user@company.local)
- OU placement
- Group membership

---

## Group Management

- Security groups used for access control
- Role-based assignment (IT, HR, Finance)
- Principle of least privilege enforced

---

## Account Policies

Configured via Group Policy:
- Password complexity enabled
- Minimum password length enforced
- Account lockout after failed attempts

---

## Common Administrative Tasks

### Unlock Account
- Use ADUC or PowerShell:
  - Search-ADAccount -LockedOut

### Reset Password
- Must enforce secure password standards

### Move User Between OUs
- Used for role changes or department transitions

---

## Monitoring

- Event Viewer (Security logs)
- Domain Controller replication status
- Failed logon tracking

---

## Best Practices

- Avoid Domain Admin overuse
- Use delegated permissions where possible
- Monitor privileged account activity