# T1018 — Remote System Discovery: Internal Port Scanning

**Tactic:** Discovery  
**Severity:** Medium  
**Data Source:** `DeviceNetworkEvents` (Defender for Endpoint)  
**Query Frequency:** Every 1 hour | **Lookback:** 1 hour

---

## Detection Rationale

After initial compromise, adversaries enumerate internal hosts and services to plan lateral movement. A single host connecting to many internal IPs across diverse ports within a short window is a strong post-compromise reconnaissance indicator. Legitimate scanning tools can be excluded by hostname.

---

## KQL Query

```kql
DeviceNetworkEvents
| where TimeGenerated > ago(1h)
| where RemoteIPType == "Private"
| summarize TargetIPs = dcount(RemoteIP), TargetPorts = dcount(RemotePort)
    by DeviceName, bin(TimeGenerated, 10m)
| where TargetIPs > 20 and TargetPorts > 10
| project TimeGenerated, DeviceName, TargetIPs, TargetPorts
```

---

## Tuning Notes

Illustrative lab guidance only. This is not a measured production baseline, and it does not list exclusions from a real environment. See the [example tuning log](../tuning-log/tuning-log.md).

When you adapt this query, baseline it on your own telemetry. Expect noise from ordinary administration (installers, backup and inventory jobs, approved remote access). If you add an exclusion, keep it as narrow as the benign case. Do not publish a live network's process name, account pattern, or host prefix.

## Response Actions

1. Identify the scanning device — is it an expected scanner or an unexpected host?
2. Review what the device was connecting to — were sensitive systems (DCs, file servers) targeted?
3. Check for other compromise indicators on the scanning device (new processes, persistence, outbound C2)
4. If a workstation — likely post-compromise recon. Isolate and investigate immediately.
5. If a server — determine if a new tool was installed or a scheduled task modified
