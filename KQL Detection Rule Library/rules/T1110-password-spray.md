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

## Tuning Log

| Field | Detail |
|-------|--------|
| Baseline Noise | ~15 alerts/day |
| Tuning Period | 5 business days |
| Final FP Rate | ~1–2 alerts/day |

**Exclusions Applied:**
- Excluded internal vulnerability scanner IPs (Tenable/Nessus)
- Excluded legacy application service accounts using NTLM
- Raised unique account threshold from 5 to 10

**Analyst Notes:** Enrich with IP reputation. External IPs = high priority. Block at firewall if confirmed malicious.

---

## Response Actions

1. Check IP reputation against threat intel feeds
2. Identify which accounts were targeted — any successful logins?
3. Block source IP at perimeter if external and confirmed malicious
4. Notify affected users to verify account activity
5. If any accounts were compromised — treat as T1078 incident
