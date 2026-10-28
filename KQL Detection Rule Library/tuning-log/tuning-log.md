# Example Tuning Log (Lab)

> This is a **generic lab example** of how a detection gets tuned. It is not a record of a production environment, and it is not a list of exclusions from any real network.
>
> The alert counts below are **illustrative targets for a write-up**. They were not measured on a live company tenant.
>
> Do not copy an exclusion from this page into a live rule. Baseline your own telemetry, and do not publish the process name, account pattern, or hostname prefix that a real environment ignores.

---

## Tuning lifecycle

```text
Deploy (alert-only) → Baseline → Find the benign cause → Narrow the exclusion → Re-baseline → Document
```

Example volume targets for a lab, after tuning:

- Critical severity: rare enough that each alert is investigated
- High severity: a handful of alerts a day, each with a clear next step
- Medium severity: higher volume is acceptable when the query is used for hunting

A public portfolio should describe the **category** of noise (installers, backup jobs, inventory scans, approved remote administration). It should not name the product, service-account prefix, or workstation naming pattern that a real network has turned off.

---

## T1078 — Impossible travel

**Severity:** High | **Tactic:** Initial Access

| Field | Lab example |
| --- | --- |
| What usually causes noise | VPN egress, travel, and a second session from a known admin jump path |
| Example target | Alerts that remain are worth a look the same day |

**How a lab would tune it:**

- Allow a known lab VPN or jump-host address only after you have confirmed it
- Keep service accounts in the result set until you know which jobs sign in from more than one place
- Re-check the allowlist when the lab network changes

**What to leave visible:** a user session from two distant locations with no approved remote-access path.

---

## T1110 — Password spray

**Severity:** High | **Tactic:** Credential Access

| Field | Lab example |
| --- | --- |
| What usually causes noise | A vulnerability scanner or a misconfigured app trying the same password across many accounts |
| Example target | External sources stay visible; known lab scanners are identified, not silently dropped in a public write-up |

**How a lab would tune it:**

- Raise the account threshold only after you can tell a scanner from a spray
- Attribute scanner traffic by a host you control, and review that exception on a schedule

**What to leave visible:** one external address failing against many accounts.

---

## T1059.001 — Encoded PowerShell

**Severity:** High | **Tactic:** Execution

| Field | Lab example |
| --- | --- |
| What usually causes noise | Management and software-deployment agents that launch encoded PowerShell as part of normal policy |
| Example target | User-context encoded commands with an unexpected parent stay in the alert |

**How a lab would tune it:**

- If a management agent is the parent, scope the exception to that agent and that parent, not to all encoded PowerShell
- Prefer stacking with Script Block Logging (Event ID 4104) over a broad exclusion

**What to leave visible:** encoded PowerShell started from a user process, Office, or a temporary directory.

---

## T1053.005 — Scheduled task created from the command line

**Severity:** Medium | **Tactic:** Persistence

| Field | Lab example |
| --- | --- |
| What usually causes noise | Installers and maintenance jobs that create tasks while software is deployed |
| Example target | Tasks with random names, or tasks that point at user-writable paths, stay visible |

**How a lab would tune it:**

- Installer process names (`msiexec.exe` and similar) are a common, narrow exception
- Do not exclude an entire backup or management product by name in a public rule

**What to leave visible:** a task whose action is a script or binary in a temp or user-profile path.

---

## T1136.001 — Local account created outside business hours

**Severity:** Medium | **Tactic:** Persistence

| Field | Lab example |
| --- | --- |
| What usually causes noise | An admin building a lab server after hours, or an automated provisioning job |
| Example target | Low volume. Treat a remaining alert as something to investigate |

**How a lab would tune it:**

- Correlate with a change record before you suppress anything
- A provisioning account can be noted, but the account name does not belong in a public exclusion list

**What to leave visible:** a local account created and then added to Administrators with no change record.

---

## T1003.001 — LSASS memory access

**Severity:** Critical | **Tactic:** Credential Access

| Field | Lab example |
| --- | --- |
| What usually causes noise | Antivirus and error-reporting processes that legitimately open LSASS |
| Example target | Anything else accessing LSASS is treated as critical |

**How a lab would tune it:**

- A short observation window will show the normal accessors on a lab image (commonly the Microsoft Defender engine and Windows Error Reporting)
- Build that allowlist from the lab image you actually run. Do not assume another site's allowlist

**What to leave visible:** an unknown process, or a known credential-dumping tool, opening LSASS. On a domain controller this is an incident.

---

## T1021.001 — RDP from a non-admin workstation

**Severity:** High | **Tactic:** Lateral Movement

| Field | Lab example |
| --- | --- |
| What usually causes noise | Helpdesk or admin staff using a normal workstation for remote support, and RDP into lab servers during maintenance |
| Example target | RDP from a workstation to a domain controller stays visible |

**How a lab would tune it:**

- Prefer an allowlist of approved admin hosts over a hostname prefix published in a repo
- Maintenance windows belong in the change record, not in a permanent exclusion

**What to leave visible:** a standard workstation opening RDP to a domain controller or to many servers.

---

## T1566.001 — Office document spawning a shell

**Severity:** High | **Tactic:** Initial Access

| Field | Lab example |
| --- | --- |
| What usually causes noise | A macro-enabled template that a team actually uses for a business process |
| Example target | A document that arrived from outside the lab and then started a shell |

**How a lab would tune it:**

- If a template is approved, scope the exception to that file hash and to the devices that should run it
- Do not exclude a whole department

**What to leave visible:** an unsigned or external document whose child process is a shell or a script host.

---

## T1070.001 — Windows event log cleared

**Severity:** High | **Tactic:** Defense Evasion

| Field | Lab example |
| --- | --- |
| What usually causes noise | A server rebuild or decommission where clearing logs is part of a documented procedure |
| Example target | Almost no alerts outside a planned change |

**How a lab would tune it:**

- Suppress only during a documented change window, and only for the admin account doing the work

**What to leave visible:** Event ID 1102 or 104 with no matching change, especially after failed logons or new processes.

---

## T1486 — Mass file rename (ransomware staging)

**Severity:** Critical | **Tactic:** Impact

| Field | Lab example |
| --- | --- |
| What usually causes noise | Backup, copy, and file-migration jobs that rename or rewrite many files quickly |
| Example target | A burst of renames into extensions such as `.locked`, `.encrypted`, or `.enc` is an incident |

**How a lab would tune it:**

- A backup job can look like this rule. If you exclude it, scope the exception to the signed process and the host that runs it
- Do not name that product, or the excluded process, in a public copy of the rule. That exclusion is a blind spot
- The threshold in the query (200 files in 5 minutes) is a starting point for a lab, not a measured production value

**What to leave visible:** mass renames by a process that is not the known backup job, on a file server or workstation.

---

## T1098 — Privileged role assigned outside a change window

**Severity:** High | **Tactic:** Privilege Escalation

| Field | Lab example |
| --- | --- |
| What usually causes noise | An emergency (break-glass) role assignment that has an approval trail |
| Example target | An unapproved privileged assignment is an incident |

**How a lab would tune it:**

- Match an approved change or ticket from whatever system the lab uses. Do not hard-code a vendor integration as if it were already deployed
- Keep Global Administrator and equivalent role assignments in the alert

**What to leave visible:** a privileged role grant with no approval record.

---

## T1018 — Internal network reconnaissance

**Severity:** Medium | **Tactic:** Discovery

| Field | Lab example |
| --- | --- |
| What usually causes noise | Vulnerability scanners, inventory, and network-monitoring servers |
| Example target | A workstation scanning a wide set of internal addresses |

**How a lab would tune it:**

- Identify scanner and monitoring hosts in the lab and exclude those hosts, not every system that connects to many ports
- Review the host list when a new management server is added

**What to leave visible:** a user workstation performing a broad internal scan.

---

*Lab example maintained by Yordan Borges. Not a production tuning record.*
