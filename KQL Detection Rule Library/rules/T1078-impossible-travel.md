# T1078 — Valid Account: Impossible Travel Login

**Tactic:** Initial Access  
**Severity:** High  
**Data Source:** `SigninLogs` (Microsoft Entra ID connector)  
**Query Frequency:** Every 1 hour | **Lookback:** 1 hour

---

## Detection Rationale

Detects sign-ins from two geographically distant locations within a timeframe that is impossible to travel between, indicating credential compromise, token theft, or VPN/proxy abuse. This is one of the most reliable indicators of account takeover when properly tuned.

---

## KQL Query

```kql
SigninLogs
| where TimeGenerated > ago(1h)
| where ResultType == "0"
| summarize Locations = make_set(Location), IPs = make_set(IPAddress), Count = count()
    by UserPrincipalName, bin(TimeGenerated, 1h)
| where array_length(Locations) > 1
| mv-expand Locations
| extend Country = tostring(Locations)
| summarize Countries = make_set(Country) by UserPrincipalName, TimeGenerated
| where array_length(Countries) > 1
```

---

## Tuning Notes

Illustrative lab guidance only. This is not a measured production baseline, and it does not list exclusions from a real environment. See the [example tuning log](../tuning-log/tuning-log.md).

When you adapt this query, baseline it on your own telemetry. Expect noise from ordinary administration (installers, backup and inventory jobs, approved remote access). If you add an exclusion, keep it as narrow as the benign case. Do not publish a live network's process name, account pattern, or host prefix.

## Response Actions

1. Confirm whether the user was traveling or using a VPN
2. Check for concurrent sessions or token reuse in Entra ID sign-in logs
3. If unauthorized — revoke sessions, reset credentials, enable MFA step-up
4. Review all activity from both locations during the overlap window
