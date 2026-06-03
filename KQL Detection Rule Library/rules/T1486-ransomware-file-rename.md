# T1486 — Data Encrypted for Impact: Mass File Rename (Ransomware Staging)

**Tactic:** Impact  
**Severity:** Critical  
**Data Source:** `DeviceFileEvents` (Defender for Endpoint)  
**Query Frequency:** Every 15 minutes | **Lookback:** 1 hour

---

## Detection Rationale

Ransomware typically renames or modifies large numbers of files in rapid succession as part of the encryption process. Detecting mass rename events early can enable containment before encryption is complete across all target systems. Speed of detection and response is critical for this rule.

---

## KQL Query

```kql
DeviceFileEvents
| where TimeGenerated > ago(1h)
| where ActionType in ("FileRenamed", "FileModified")
| summarize FileCount = count(), Extensions = make_set(tostring(split(FileName, ".")[-1]))
    by DeviceName, AccountName, bin(TimeGenerated, 5m)
| where FileCount > 200
| extend SuspiciousExtensions = set_has_element(Extensions, "locked")
    or set_has_element(Extensions, "encrypted")
    or set_has_element(Extensions, "enc")
| project TimeGenerated, DeviceName, AccountName, FileCount, Extensions, SuspiciousExtensions
```

---

## Tuning Log

| Field | Detail |
|-------|--------|
| Baseline Noise | ~5 alerts/day |
| Tuning Period | 7 business days |
| Final FP Rate | ~0–1 alerts/week |

**Exclusions Applied:**
- Excluded Veeam Backup & Replication agent process tree
- Excluded file server migration service account during active migration projects
- Raised file rename threshold from 100 to 200 files per 5-minute window

**Analyst Notes:** Known ransomware extensions (`.locked`, `.encrypted`, `.enc`, `.crypted`) = isolate immediately. Do not wait for analyst confirmation. Automated playbook recommended for this rule.

---

## Response Actions

1. **Immediately isolate the endpoint** — do not wait for investigation
2. Identify the process responsible for the rename activity
3. Determine blast radius — which file shares or paths were affected?
4. Check for lateral spread — are other endpoints showing similar patterns?
5. Engage incident response and ransomware recovery procedures
6. Preserve forensic artifacts before remediation (memory dump, process list, network connections)
