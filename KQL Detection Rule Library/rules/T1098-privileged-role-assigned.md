# T1098 — Account Manipulation: Privileged Role Assigned Outside Change Window

**Tactic:** Privilege Escalation  
**Severity:** High  
**Data Source:** `AuditLogs` (Microsoft Entra ID connector)  
**Query Frequency:** Every 1 hour | **Lookback:** 24 hours

---

## Detection Rationale

Assigning Global Administrator, Security Administrator, or other privileged Entra ID roles outside of approved change windows indicates potential privilege escalation by an attacker or unauthorized insider activity. This rule covers a critical blind spot in environments without PIM (Privileged Identity Management).

---

## KQL Query

```kql
AuditLogs
| where TimeGenerated > ago(1d)
| where OperationName has "Add member to role"
| extend RoleName = tostring(TargetResources[0].displayName)
| extend AssignedBy = tostring(InitiatedBy.user.userPrincipalName)
| extend AssignedTo = tostring(TargetResources[1].userPrincipalName)
| where RoleName in ("Global Administrator","Security Administrator",
    "Privileged Role Administrator","Exchange Administrator")
| extend HourOfDay = datetime_part("Hour", TimeGenerated)
| where HourOfDay !between (8 .. 18)
| project TimeGenerated, RoleName, AssignedBy, AssignedTo, HourOfDay
```

---

## Tuning Notes

Illustrative lab guidance only. This is not a measured production baseline, and it does not list exclusions from a real environment. See the [example tuning log](../tuning-log/tuning-log.md).

When you adapt this query, baseline it on your own telemetry. Expect noise from ordinary administration (installers, backup and inventory jobs, approved remote access). If you add an exclusion, keep it as narrow as the benign case. Do not publish a live network's process name, account pattern, or host prefix.

## Response Actions

1. Contact the assigning admin (`AssignedBy`) to verify whether the assignment was intentional
2. If unauthorized — revoke the role assignment immediately
3. Review all actions taken by `AssignedTo` during the elevated period
4. Check sign-in logs for both accounts for anomalous activity
5. If the assigning account was compromised — initiate full account takeover response
6. Recommend enabling PIM (Privileged Identity Management) to require approval for role activation
