# KQL Detection Rule Library — Microsoft Sentinel
> **Author:** Yordan Borges | SC-200 Certified | Security Operations Analyst  
> **Platform:** Microsoft Sentinel (Log Analytics / Defender XDR)  
> **Framework:** MITRE ATT&CK v14  
> **Rules:** 12 production-ready detections with false positive tuning logs

---

## Overview

This repository contains a structured library of KQL detection rules written for Microsoft Sentinel, mapped to MITRE ATT&CK techniques. Each rule was developed from real-world security operations experience, baselined against live telemetry, and iteratively tuned to reduce false positive noise while maintaining high-fidelity detection coverage.

Every rule includes:
- **Detection rationale** — why this technique matters and what the rule targets
- **Production-ready KQL** — tested against Sentinel Log Analytics tables
- **Tuning log** — baseline noise volume, exclusions applied, and final FP rate
- **Analyst notes** — operational context and escalation guidance

---

## Repository Structure

```
kql-detection-library/
├── README.md                        # This file
├── mitre-mapping.md                 # Full ATT&CK technique index
├── tuning-log/
│   └── tuning-log.md               # Consolidated false positive tuning log
└── rules/
    ├── T1078-impossible-travel.md
    ├── T1110-password-spray.md
    ├── T1059.001-encoded-powershell.md
    ├── T1053.005-scheduled-task.md
    ├── T1136.001-local-account-creation.md
    ├── T1003.001-lsass-access.md
    ├── T1021.001-rdp-lateral-movement.md
    ├── T1566.001-phishing-macro.md
    ├── T1070.001-event-log-cleared.md
    ├── T1486-ransomware-file-rename.md
    ├── T1098-privileged-role-assigned.md
    └── T1018-internal-recon.md
```

---

## Detection Coverage Summary

| Rule | Technique | Tactic | Severity | Data Source |
|------|-----------|--------|----------|-------------|
| Impossible Travel Login | T1078 | Initial Access | High | SigninLogs |
| Password Spray | T1110 | Credential Access | High | SigninLogs |
| Encoded PowerShell | T1059.001 | Execution | High | DeviceProcessEvents |
| Scheduled Task via CLI | T1053.005 | Persistence | Medium | DeviceProcessEvents |
| Local Account After Hours | T1136.001 | Persistence | Medium | SecurityEvent |
| LSASS Memory Access | T1003.001 | Credential Access | Critical | DeviceEvents |
| RDP Lateral Movement | T1021.001 | Lateral Movement | High | DeviceNetworkEvents |
| Office Macro Spawning Shell | T1566.001 | Initial Access | High | DeviceProcessEvents |
| Event Log Cleared | T1070.001 | Defense Evasion | High | SecurityEvent |
| Mass File Rename | T1486 | Impact | Critical | DeviceFileEvents |
| Privileged Role Assigned | T1098 | Privilege Escalation | High | AuditLogs |
| Internal Port Scanning | T1018 | Discovery | Medium | DeviceNetworkEvents |

---

## Tuning Methodology

All rules follow a structured tuning lifecycle:

1. **Deploy in alert-only mode** — no automated response, observe volume for 5–10 business days
2. **Baseline noise** — document alert volume and identify recurring false positive sources
3. **Root cause each FP** — categorize by: legitimate tool, approved process, misconfiguration, or data quality issue
4. **Apply targeted exclusions** — allowlist by process name, parent process, IP range, account prefix, or time window
5. **Re-baseline** — run for another 5 days and measure FP rate reduction
6. **Document and lock** — record all exclusions in the tuning log before enabling automated response

> Target FP rate: **< 5 alerts/day** for high-volume rules, **< 1 alert/week** for critical severity rules.

---

## Data Sources Required

| Sentinel Table | Rules Using It |
|----------------|----------------|
| `SigninLogs` | T1078, T1110 |
| `DeviceProcessEvents` | T1059.001, T1053.005, T1566.001 |
| `DeviceNetworkEvents` | T1021.001, T1018 |
| `DeviceFileEvents` | T1486 |
| `DeviceEvents` | T1003.001 |
| `SecurityEvent` | T1136.001, T1070.001 |
| `AuditLogs` | T1098 |

Requires **Microsoft Defender for Endpoint** connector and **Microsoft Entra ID** connector enabled in Sentinel.

---

## How to Deploy

1. Open **Microsoft Sentinel → Analytics → + Create → Scheduled query rule**
2. Paste the KQL from the relevant rule file
3. Set query frequency and lookback window per the rule's recommendation
4. Deploy in **alert-only** mode (no automated playbook) for initial baselining
5. Apply exclusions from the tuning log after baseline period
6. Enable automated response only after FP rate is within acceptable threshold

---

## Certifications & Background

- **Microsoft Certified: Security Operations Analyst Associate (SC-200)**
- 4+ years hands-on experience in hybrid Microsoft environments
- Production experience with Microsoft Sentinel, Defender XDR, Entra ID, Azure Arc
- Active Directory, Windows Server, and endpoint security administration

---

## Contact

**Yordan Borges**  
[LinkedIn](#) | [GitHub](#) | yordanb00@yahoo.com
