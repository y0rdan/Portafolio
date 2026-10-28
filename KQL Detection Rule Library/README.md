# KQL Detection Rule Library — Microsoft Sentinel
> **Author:** Yordan Borges | Systems Engineer | SC-200  
> **Platform:** Microsoft Sentinel (Log Analytics / Defender XDR)  
> **Framework:** MITRE ATT&CK v14  
> **Rules:** 12 lab detections, plus an example tuning log

---

## Overview

Lab detections for Microsoft Sentinel, mapped to MITRE ATT&CK. They are here to show how systems work turns into visibility: sign-ins, Windows security events, endpoint process and file events.

Every rule includes:
- **Detection rationale** — why this technique matters and what the query looks for
- **KQL** — written for the Sentinel tables named in the rule
- **Tuning note** — a pointer to the example tuning log, not a measured production baseline
- **Response actions** — what to check next on the host or the account

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

The example tuning log walks through a lifecycle you would use in a lab. It is not a record of exclusions applied to a live tenant.

1. **Deploy in alert-only mode** and watch the volume
2. **Baseline noise** and name the benign cause (installer, backup job, inventory scan, approved remote access)
3. **Narrow any exclusion** to that cause. Do not publish a real account prefix, product name, or hostname pattern
4. **Re-baseline** and only then consider an automated response

> The example log uses illustrative volume targets. Measure your own workspace before you treat a number as real.

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
5. Baseline on your own telemetry before adding any exclusion
6. Turn on automated response only after you have measured the noise yourself. Do not copy exclusions from the example tuning log into a live workspace.

---

## Certifications & Background

- **Microsoft Certified: Security Operations Analyst Associate (SC-200)**
- Hands-on work in hybrid Microsoft environments (Active Directory, Windows Server, endpoint administration)
- Lab detections written for Microsoft Sentinel and Defender XDR tables

---

## Contact

**Yordan Borges**  
[LinkedIn](https://www.linkedin.com/in/yordan-borges-b86791172) | [GitHub](https://github.com/y0rdan) | yordanb00@yahoo.com
