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

## Tuning Notes

Illustrative lab guidance only. This is not a measured production baseline, and it does not list exclusions from a real environment. See the [example tuning log](../tuning-log/tuning-log.md).

When you adapt this query, baseline it on your own telemetry. Expect noise from ordinary administration (installers, backup and inventory jobs, approved remote access). If you add an exclusion, keep it as narrow as the benign case. Do not publish a live network's process name, account pattern, or host prefix.

## Response Actions

1. **Immediately isolate the endpoint** — do not wait for investigation
2. Identify the process responsible for the rename activity
3. Determine blast radius — which file shares or paths were affected?
4. Check for lateral spread — are other endpoints showing similar patterns?
5. Engage incident response and ransomware recovery procedures
6. Preserve forensic artifacts before remediation (memory dump, process list, network connections)
