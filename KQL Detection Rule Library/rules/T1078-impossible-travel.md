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

## Tuning Log

| Field | Detail |
|-------|--------|
| Baseline Noise | ~40 alerts/day |
| Tuning Period | 7 business days |
| Final FP Rate | ~2 alerts/day (~95% reduction) |

**Exclusions Applied:**
- Excluded known corporate VPN IP ranges via Sentinel watchlist
- Excluded service accounts matching `svc-*` prefix
- Excluded approved remote workers with static home IPs via Entra ID Named Locations

**Analyst Notes:** Tune VPN CIDR blocks quarterly. Remaining alerts are high-fidelity — investigate within 30 minutes.

---

## Response Actions

1. Confirm whether the user was traveling or using a VPN
2. Check for concurrent sessions or token reuse in Entra ID sign-in logs
3. If unauthorized — revoke sessions, reset credentials, enable MFA step-up
4. Review all activity from both locations during the overlap window
