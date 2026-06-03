# MITRE ATT&CK Technique Mapping

> All detections in this library are mapped to [MITRE ATT&CK v14](https://attack.mitre.org/).

---

## Tactic Coverage

### Initial Access
| Technique ID | Technique Name | Rule File |
|-------------|----------------|-----------|
| T1078 | Valid Accounts — Impossible Travel | [T1078-impossible-travel.md](rules/T1078-impossible-travel.md) |
| T1566.001 | Phishing — Spearphishing Attachment (Office Macro) | [T1566.001-phishing-macro.md](rules/T1566.001-phishing-macro.md) |

### Execution
| Technique ID | Technique Name | Rule File |
|-------------|----------------|-----------|
| T1059.001 | Command and Scripting Interpreter — PowerShell | [T1059.001-encoded-powershell.md](rules/T1059.001-encoded-powershell.md) |

### Persistence
| Technique ID | Technique Name | Rule File |
|-------------|----------------|-----------|
| T1053.005 | Scheduled Task/Job — Scheduled Task | [T1053.005-scheduled-task.md](rules/T1053.005-scheduled-task.md) |
| T1136.001 | Create Account — Local Account | [T1136.001-local-account-creation.md](rules/T1136.001-local-account-creation.md) |

### Privilege Escalation
| Technique ID | Technique Name | Rule File |
|-------------|----------------|-----------|
| T1098 | Account Manipulation — Privileged Role Assignment | [T1098-privileged-role-assigned.md](rules/T1098-privileged-role-assigned.md) |

### Defense Evasion
| Technique ID | Technique Name | Rule File |
|-------------|----------------|-----------|
| T1070.001 | Indicator Removal — Clear Windows Event Logs | [T1070.001-event-log-cleared.md](rules/T1070.001-event-log-cleared.md) |

### Credential Access
| Technique ID | Technique Name | Rule File |
|-------------|----------------|-----------|
| T1110 | Brute Force — Password Spraying | [T1110-password-spray.md](rules/T1110-password-spray.md) |
| T1003.001 | OS Credential Dumping — LSASS Memory | [T1003.001-lsass-access.md](rules/T1003.001-lsass-access.md) |

### Discovery
| Technique ID | Technique Name | Rule File |
|-------------|----------------|-----------|
| T1018 | Remote System Discovery — Internal Port Scanning | [T1018-internal-recon.md](rules/T1018-internal-recon.md) |

### Lateral Movement
| Technique ID | Technique Name | Rule File |
|-------------|----------------|-----------|
| T1021.001 | Remote Services — Remote Desktop Protocol | [T1021.001-rdp-lateral-movement.md](rules/T1021.001-rdp-lateral-movement.md) |

### Impact
| Technique ID | Technique Name | Rule File |
|-------------|----------------|-----------|
| T1486 | Data Encrypted for Impact — Ransomware File Rename | [T1486-ransomware-file-rename.md](rules/T1486-ransomware-file-rename.md) |

---

## ATT&CK Navigator Layer

To visualize this coverage in the [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/), import the following technique IDs:

```
T1078, T1566.001, T1059.001, T1053.005, T1136.001,
T1098, T1070.001, T1110, T1003.001, T1018, T1021.001, T1486
```
