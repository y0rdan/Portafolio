# T1110 — Brute Force: Password Spray Detection

**Tactic:** Credential Access  
**Severity:** High  
**Data Source:** `SigninLogs` (Microsoft Entra ID connector)  
**Query Frequency:** Every 1 hour | **Lookback:** 1 hour

---

## Detection Rationale

Identifies a single source IP attempting authentication against many accounts with few failures per account — the hallmark of a password spray attack. Unlike brute force (many attempts per account), spray attacks stay under per-account lockout thresholds by cycling a small password set across many targets.

---

## KQL Query

```kql
SigninLogs
| where TimeGenerated > ago(1h)
| where ResultType != "0"
| summarize FailedAccounts = dcount(UserPrincipalName), Attempts = count()
    by IPAddress, bin(TimeGenerated, 1h)
| where FailedAccounts > 10 and Attempts < FailedAccounts * 3
| project TimeGenerated, IPAddress, FailedAccounts, Attempts
```

---

## Tuning Notes

Illustrative lab guidance only. This is not a measured production baseline, and it does not list exclusions from a real environment. See the [example tuning log](../tuning-log/tuning-log.md).

When you adapt this query, baseline it on your own telemetry. Expect noise from ordinary administration (installers, backup and inventory jobs, approved remote access). If you add an exclusion, keep it as narrow as the benign case. Do not publish a live network's process name, account pattern, or host prefix.

## Response Actions

1. Check IP reputation against threat intel feeds
2. Identify which accounts were targeted — any successful logins?
3. Block source IP at perimeter if external and confirmed malicious
4. Notify affected users to verify account activity
5. If any accounts were compromised — treat as T1078 incident
