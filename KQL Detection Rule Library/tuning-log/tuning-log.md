# False Positive Tuning Log

> This document records the tuning lifecycle for every detection rule in this library.  
> Each entry captures: baseline noise, exclusions applied, and final false positive rate after tuning.

---

## Tuning Lifecycle Overview

```
Deploy (alert-only) → Baseline (5–10 days) → Root Cause FPs → Apply Exclusions → Re-baseline → Lock & Document
```

**FP Rate Targets:**
- Critical severity: < 1 alert/week
- High severity: < 5 alerts/day
- Medium severity: < 10 alerts/day

---

## T1078 — Impossible Travel Login

**Severity:** High | **Tactic:** Initial Access

| Field | Detail |
|-------|--------|
| Baseline Noise | ~40 alerts/day |
| Tuning Period | 7 business days |
| Final FP Rate | ~2 alerts/day (~95% reduction) |

**Exclusions Applied:**
- Excluded known corporate VPN IP ranges (CIDR blocks added to watchlist)
- Excluded service accounts matching `svc-*` prefix
- Excluded approved remote workers with static home IPs via named locations in Entra ID

**Root Cause of FPs:** Majority caused by split-tunnel VPN users appearing to log in from multiple countries simultaneously. Secondary source was executive travel with personal hotspots.

**Analyst Notes:** Tune VPN CIDR blocks quarterly as infrastructure changes. Remaining alerts are high-fidelity and should be investigated within 30 minutes.

---

## T1110 — Password Spray Detection

**Severity:** High | **Tactic:** Credential Access

| Field | Detail |
|-------|--------|
| Baseline Noise | ~15 alerts/day |
| Tuning Period | 5 business days |
| Final FP Rate | ~1–2 alerts/day |

**Exclusions Applied:**
- Excluded internal vulnerability scanner IPs (Tenable/Nessus)
- Excluded legacy application service accounts using NTLM authentication
- Raised unique account threshold from 5 to 10 to reduce misconfigured app noise

**Root Cause of FPs:** Automated vulnerability scanners and misconfigured legacy applications generated the bulk of initial noise. One internal monitoring tool was authenticating against multiple accounts on a scheduled basis.

**Analyst Notes:** Enrich alerts with IP reputation data from threat intel feed. Any external IP triggering this rule should be treated as high priority.

---

## T1059.001 — PowerShell Encoded Command Execution

**Severity:** High | **Tactic:** Execution

| Field | Detail |
|-------|--------|
| Baseline Noise | ~60 alerts/day |
| Tuning Period | 10 business days |
| Final FP Rate | ~3–5 alerts/day |

**Exclusions Applied:**
- Excluded SCCM client processes where `CCMExec.exe` is the parent process
- Excluded Microsoft Intune Management Extension process tree
- Excluded signed Microsoft binaries as initiating process
- Excluded known monitoring agent process hashes via custom watchlist

**Root Cause of FPs:** SCCM and Intune generate high volumes of encoded PowerShell as part of normal device management operations. EDR and monitoring agents also contributed significantly.

**Analyst Notes:** Stack with PowerShell Script Block Logging (Event ID 4104) and AMSI events for compound detection. Encoded commands from unknown parent processes or user-context sessions are highest priority.

---

## T1053.005 — Scheduled Task Created via Command Line

**Severity:** Medium | **Tactic:** Persistence

| Field | Detail |
|-------|--------|
| Baseline Noise | ~25 alerts/day |
| Tuning Period | 7 business days |
| Final FP Rate | ~2–3 alerts/day |

**Exclusions Applied:**
- Excluded `msiexec.exe`, `setup.exe`, and `install.exe` as initiating processes
- Excluded Veeam Backup agent scheduled task creation
- Allowlisted known patch management task names via Sentinel watchlist

**Root Cause of FPs:** Software installers account for the majority of legitimate scheduled task creation. Backup agents and RMM tools were secondary sources.

**Analyst Notes:** Review task name and command content in each alert. Random-looking task names or tasks pointing to temp directories are high-priority indicators.

---

## T1136.001 — Local Account Created Outside Business Hours

**Severity:** Medium | **Tactic:** Persistence

| Field | Detail |
|-------|--------|
| Baseline Noise | ~5 alerts/day |
| Tuning Period | 5 business days |
| Final FP Rate | ~0–1 alerts/week |

**Exclusions Applied:**
- Excluded documented admin accounts performing after-hours work (correlated with change tickets)
- Excluded automated provisioning service account used during system deployments

**Root Cause of FPs:** Small number of IT admins performing after-hours server builds. Once provisioning service account was identified and excluded, volume dropped to near-zero.

**Analyst Notes:** Low volume makes this rule inherently high-fidelity. Every alert should be investigated. Correlate with Event ID 4722 (account enabled) and 4732 (added to security group) for full context.

---

## T1003.001 — LSASS Memory Access

**Severity:** Critical | **Tactic:** Credential Access

| Field | Detail |
|-------|--------|
| Baseline Noise | ~8 alerts/day |
| Tuning Period | 14 business days (extended baseline) |
| Final FP Rate | ~0–1 alerts/week |

**Exclusions Applied:**
- Excluded `MsMpEng.exe` (Microsoft Defender antivirus engine)
- Excluded EDR sensor processes (CrowdStrike, Defender for Endpoint)
- Excluded `werfault.exe` (Windows Error Reporting)
- Built comprehensive allowlist from 2-week observation of legitimate LSASS accessors

**Root Cause of FPs:** Security tools (AV, EDR) legitimately access LSASS for protection purposes. Extended baseline period was necessary to capture all legitimate accessors across different system types.

**Analyst Notes:** Any process not on the allowlist accessing LSASS is critical priority. Do not wait — escalate immediately and consider isolating the endpoint while investigating.

---

## T1021.001 — RDP Lateral Movement from Non-Admin Workstation

**Severity:** High | **Tactic:** Lateral Movement

| Field | Detail |
|-------|--------|
| Baseline Noise | ~20 alerts/day |
| Tuning Period | 7 business days |
| Final FP Rate | ~2 alerts/day |

**Exclusions Applied:**
- Excluded IT helpdesk team workstations (`HELP-*` naming convention)
- Excluded RDP connections to known test and lab servers
- Excluded connections occurring during approved maintenance windows

**Root Cause of FPs:** IT helpdesk staff using standard workstations for remote support was the primary source. Lab environments also generated significant noise during testing periods.

**Analyst Notes:** Correlate source workstation and destination server with AD group membership to identify privilege mismatches. Workstations RDP-ing to domain controllers are critical priority.

---

## T1566.001 — Office Document Spawning Shell Process

**Severity:** High | **Tactic:** Initial Access

| Field | Detail |
|-------|--------|
| Baseline Noise | ~10 alerts/day |
| Tuning Period | 7 business days |
| Final FP Rate | ~1 alert/day |

**Exclusions Applied:**
- Excluded approved macro-enabled templates by file hash (finance team Excel automation)
- Excluded finance team devices running approved Excel automation workflows
- Excluded IT-signed scripts launched via Outlook rules

**Root Cause of FPs:** Finance team uses macro-enabled Excel templates for reporting automation. These were approved, hash-allowlisted, and device-scoped to minimize exclusion blast radius.

**Analyst Notes:** Any unsigned document or document received via email spawning a shell process is critical priority. Always check email source and whether the document arrived externally.

---

## T1070.001 — Windows Event Log Cleared

**Severity:** High | **Tactic:** Defense Evasion

| Field | Detail |
|-------|--------|
| Baseline Noise | ~3 alerts/week |
| Tuning Period | 5 business days |
| Final FP Rate | ~0–1 alerts/month (outside change windows) |

**Exclusions Applied:**
- Excluded timestamps during documented server decommission change windows
- Excluded known server retirement admin accounts performing decommission tasks

**Root Cause of FPs:** IT performs log clearing during server decommissions as part of the standard offboarding procedure. Change window correlation eliminated almost all FPs.

**Analyst Notes:** Event ID 1102 = Security log cleared. Event ID 104 = System log cleared. Both should trigger immediate investigation unless there is an active change ticket. Correlate with other defense evasion indicators in the same timeframe.

---

## T1486 — Mass File Rename (Ransomware Staging)

**Severity:** Critical | **Tactic:** Impact

| Field | Detail |
|-------|--------|
| Baseline Noise | ~5 alerts/day |
| Tuning Period | 7 business days |
| Final FP Rate | ~0–1 alerts/week |

**Exclusions Applied:**
- Excluded Veeam Backup & Replication agent process tree
- Excluded file server migration service account during active migration projects
- Raised file rename threshold from 100 to 200 files per 5-minute window

**Root Cause of FPs:** Backup agents perform file operations that resemble ransomware staging patterns. File migration projects during business hours also generated significant noise.

**Analyst Notes:** Any alert containing known ransomware extensions (`.locked`, `.encrypted`, `.enc`, `.crypted`) requires immediate endpoint isolation — do not wait for confirmation. Speed of response is critical for ransomware containment.

---

## T1098 — Privileged Role Assigned Outside Change Window

**Severity:** High | **Tactic:** Privilege Escalation

| Field | Detail |
|-------|--------|
| Baseline Noise | ~2 alerts/week |
| Tuning Period | 5 business days |
| Final FP Rate | ~0 alerts/week |

**Exclusions Applied:**
- Excluded documented emergency access (break-glass) account assignments with approval trail
- Correlated with ServiceNow change tickets to auto-suppress approved role assignments

**Root Cause of FPs:** Occasional legitimate emergency role assignments outside business hours. ServiceNow integration for automated change ticket correlation eliminated these as FPs.

**Analyst Notes:** Zero tolerance threshold. Any unapproved privileged role assignment — especially Global Administrator or Privileged Role Administrator — should be treated as an active incident immediately.

---

## T1018 — Internal Network Reconnaissance

**Severity:** Medium | **Tactic:** Discovery

| Field | Detail |
|-------|--------|
| Baseline Noise | ~10 alerts/day |
| Tuning Period | 7 business days |
| Final FP Rate | ~1 alert/day |

**Exclusions Applied:**
- Excluded Tenable/Nessus scanner hostname from all network recon rules
- Excluded SCCM distribution point server (performs inventory scans)
- Excluded PRTG network monitoring server

**Root Cause of FPs:** Security scanning tools and network monitoring platforms are the primary source of internal recon-like behavior. All three tools were identified during baseline and explicitly excluded by hostname.

**Analyst Notes:** Standard servers and workstations should never be scanning large portions of the internal network. Any non-excluded device triggering this rule should be investigated — particularly workstations, which have no legitimate reason to perform broad internal network scanning.

---

*Last updated: 2026 | Maintained by Yordan Borges*
