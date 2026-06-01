# Enterprise Active Directory Infrastructure Lab

## Overview

This project demonstrates the design, deployment, administration, hardening, and troubleshooting of a Windows Server enterprise environment using Active Directory Domain Services (AD DS). The environment simulates a production-grade corporate infrastructure featuring redundant domain controllers, centralized identity management, DNS and DHCP services, Group Policy enforcement, and disaster recovery operations.

The lab focuses on enterprise administration practices and security operations workflows, emphasizing identity management, infrastructure resilience, security hardening, operational troubleshooting, and PowerShell automation.

---

## Project Objectives

- Deploy a fully functional Active Directory domain environment  
- Configure redundant domain controllers to provide high availability  
- Implement and manage enterprise DNS and DHCP services  
- Design and enforce Group Policy Objects (GPOs)  
- Validate Active Directory replication and SYSVOL synchronization  
- Simulate and resolve enterprise infrastructure failures  
- Harden Windows Server environments using industry best practices  
- Automate administrative tasks through PowerShell  
- Perform disaster recovery testing and validation  
- Develop operational and security-focused troubleshooting skills  

---

## Repository Structure

```text
active-directory-lab/
│
├── README.md
├── diagrams/
├── screenshots/
├── powershell/
├── gpo-backups/
├── recovery-procedures/
└── documentation/
````

---

## Technologies Used

* Windows Server 2019
* Active Directory Domain Services (AD DS)
* Domain Name System (DNS)
* Dynamic Host Configuration Protocol (DHCP)
* DFS Replication (DFSR)
* Group Policy Management Console (GPMC)
* PowerShell 5.1 and PowerShell 7+
* Hyper-V
* VMware Workstation
* Windows Admin Center
* Microsoft Defender for Endpoint

---

## Infrastructure Architecture

### Server Inventory

| Server Name | Role                        | IP Address   |
| ----------- | --------------------------- | ------------ |
| DC01        | Primary Domain Controller   | 192.168.1.93 |
| DC02        | Secondary Domain Controller | 192.168.1.94 |
| PC1         | Domain-Joined Workstation   | 192.168.1.95 |

---

## Network Services Configuration

### DNS Services

The DNS infrastructure was configured using Active Directory–integrated zones to ensure secure and reliable name resolution throughout the environment.

Key configurations included:

* Forward Lookup Zone for `homelab.local`
* Reverse Lookup Zone for internal address resolution
* Active Directory–integrated zone replication
* Conditional forwarders for external name resolution
* DNS diagnostics and health validation testing

---

### DHCP Services

DHCP was implemented to provide centralized IP address management for domain-connected devices.

Configuration highlights:

* IPv4 scope deployment for the enterprise subnet
* Infrastructure device reservations
* Optimized lease durations for lab simulations
* Dynamic DNS registration for client systems

---

## Active Directory Design

### Organizational Unit Structure

```text
homelab.local
│
├── Servers
├── Workstations
├── Users
│   ├── IT
│   ├── HR
│   └── Finance
├── Groups
├── Service Accounts
└── Admin Accounts
```

The structure was designed to support delegated administration, security segmentation, and efficient Group Policy management.

---

## Identity and Access Management

Enterprise identity management controls were implemented using Active Directory security groups and organizational units.

Key implementations included:

* Role-Based Access Control (RBAC)
* Least-privilege security group design
* Administrative delegation using OU permissions
* Standardized user provisioning procedures
* Password complexity requirements
* Account lockout policy enforcement

---

## Group Policy Implementation

### Security Policies

* Password complexity and minimum length requirements
* Account lockout thresholds
* Microsoft Defender security configurations
* Windows Firewall enforcement
* USB storage restrictions
* Advanced audit logging

### Administrative Policies

* Desktop environment restrictions
* Network drive mappings
* Logon banner deployment
* PowerShell execution policy management
* Security baseline alignment

---

## SYSVOL and DFS Replication

### DFS Replication Configuration

SYSVOL replication was configured between domain controllers using DFS Replication to ensure Group Policy consistency throughout the environment.

Validation activities:

* Replication health monitoring
* DFSR event log analysis
* Replication backlog verification
* Synchronization consistency testing
* SYSVOL accessibility validation

---

### Troubleshooting Activities

* SYSVOL replication failures
* DFSR service corruption
* Group Policy replication issues
* DNS replication inconsistencies
* Domain controller communication failures
* Authentication and trust relationship issues

---

## Disaster Recovery Operations

### Recovery Scenarios

* Domain controller failure recovery
* SYSVOL corruption restoration
* DFSR non-authoritative synchronization rebuild
* Active Directory metadata cleanup
* DNS service recovery

### Validation Process

* User authentication verification
* Group Policy application validation
* SYSVOL accessibility checks
* Active Directory replication health
* DNS functionality testing

---

## PowerShell Automation

### Active Directory User Provisioning

```powershell
Import-Module ActiveDirectory

New-ADUser `
-Name "John Doe" `
-GivenName "John" `
-Surname "Doe" `
-SamAccountName "jdoe" `
-UserPrincipalName "jdoe@homelab.local" `
-Path "OU=Users,DC=homelab,DC=local" `
-Enabled $true `
-AccountPassword (ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force)
```

### Replication Health Validation

```powershell
repadmin /replsummary
dcdiag /v
Get-ADReplicationFailure -Scope Site
```

### SYSVOL Validation

```powershell
net share
dfsrmig /getmigrationstate
Get-Service DFSR
```

---

## Security Hardening

* Microsoft Defender for Endpoint policies
* Attack Surface Reduction (ASR) rules
* SMB protocol hardening
* Restricted Remote Desktop access
* PowerShell logging and transcription
* Credential Guard protections
* Windows Firewall enforcement
* Advanced audit policy configuration

---

## Technical Challenges and Resolutions

### DFSR SYSVOL Replication Failure

A replication failure was simulated due to DFSR state inconsistency and topology conflicts between domain controllers.

#### Resolution Steps

* Validated Active Directory replication health
* Analyzed DFS Replication event logs
* Performed non-authoritative SYSVOL synchronization
* Rebuilt DFSR replication memberships
* Verified SYSVOL consistency across controllers
* Confirmed replication restoration

---

## Key Lessons Learned

* DNS stability is critical for Active Directory functionality
* DFSR requires proactive monitoring and recovery planning
* PowerShell automation reduces operational overhead
* Multi-DC environments require continuous replication monitoring
* Disaster recovery procedures must be tested regularly

---

## Skills Demonstrated

* Active Directory Domain Services Administration
* Windows Server Infrastructure Management
* DNS and DHCP Administration
* DFS Replication Troubleshooting
* Group Policy Design and Management
* PowerShell Automation
* Enterprise Security Hardening
* Disaster Recovery Planning
* Incident Response and Root Cause Analysis
* Identity and Access Management (IAM)

---

## Future Enhancements

* Microsoft Entra ID hybrid integration
* Microsoft Sentinel integration
* Centralized security monitoring dashboards
* Multi-site Active Directory replication design
* Active Directory Certificate Services (AD CS)
* Automated vulnerability scanning
* Centralized log collection and detection engineering

```
```
