
# 📘 SOC Alert Documentation – Splunk Detection Library

## Overview

This document defines standardized alert formats used in the Splunk SOC environment integrated with automated analysis workflows (n8n + Discord). Each alert includes classification, MITRE mapping, severity, and response guidance for Tier 1–2 analysts.

---

# 🚨 Alert 1: Failed Logon – Brute Force (Known User)

## Detection Name

Failed Logon Brute Force (EventCode 4625)

## Trigger Logic

* Windows Security Event ID: `4625`
* Same username observed repeatedly
* Same source IP generating failed attempts
* Threshold: ≥ 4 events within short time window

## Event Summary

* Host: `192.168.1.104`
* User: `tjoe`
* Source IP: `192.168.1.104`
* Event Count: `4`

## Threat Classification

Brute-force password guessing targeting a valid user account

## Severity

LOW

## Analysis

Multiple failed authentication attempts indicate repeated login failures for a known user. Pattern suggests either:

* Misconfigured service or scheduled task using invalid credentials
* Early-stage brute-force attempt
* Internal testing or script behavior

No evidence of successful authentication detected in this dataset.

## MITRE ATT&CK Mapping

* Technique: T1110 – Brute Force
* Description: Repeated authentication attempts used to guess valid credentials

## Recommended Actions

* Validate whether user `tjoe` is used by services or scripts
* Review scheduled tasks on the source host
* Enable account lockout policies if not enforced
* Monitor for Event ID 4624 (successful logon) following this pattern

## SOC Notes

Escalation is not required unless:

* Event frequency increases
* Successful logon is detected from same source
* Lateral movement indicators appear

---

# 🚨 Alert 2: Failed Logon – Credential Spraying / Unknown User

## Detection Name

Failed Logon Brute Force (Unknown Username)

## Trigger Logic

* Event ID: `4625`
* Username field empty or null
* Multiple authentication failures from same source IP

## Event Summary

* Host: `192.168.1.104`
* User: `UNKNOWN`
* Source IP: `192.168.1.104`
* Event Count: `4`

## Threat Classification

Credential spraying or automated login probing without valid username enumeration

## Severity

LOW

## Analysis

Authentication failures without a specified username typically indicate:

* Automated brute-force tools cycling through credential formats
* Scripts probing authentication endpoints
* Misconfigured authentication service generating null logins

While current volume is low, this pattern is commonly used in early-stage reconnaissance.

## MITRE ATT&CK Mapping

* Technique: T1110 – Brute Force
* Sub-technique behavior: Credential guessing without valid username context

## Recommended Actions

* Investigate source system for automation scripts or misconfigured services
* Enable anomaly detection for blank username authentication attempts
* Block or throttle source IP if volume increases
* Enforce MFA on all interactive authentication endpoints

## SOC Notes

Monitor for:

* Sudden username enumeration patterns
* Transition from failed to successful logons
* Correlation with reconnaissance activity (port scans, LDAP queries)

---

# 🚨 Alert 3: Credential Dumping – Mimikatz Detection

## Detection Name

Mimikatz Execution / Credential Dumping Activity

## Trigger Logic

* Process execution matches known Mimikatz signatures
* LSASS memory access behavior detected
* High privilege context observed (Domain Admin / elevated user)

## Event Summary

* Host: `DC1.homelab.local`
* User: `HOMELAB\tjoe`
* Source IP: `192.168.1.104`
* Event Count: `1`

## Threat Classification

Credential dumping via LSASS memory extraction

## Severity

HIGH

## Analysis

Detected execution patterns consistent with Mimikatz activity targeting LSASS process memory. This behavior strongly indicates credential harvesting attempts.

If successful, attacker gains:

* NTLM hashes
* Kerberos tickets
* Plaintext credentials (in some configurations)

Execution on a Domain Controller significantly increases blast radius risk.

## MITRE ATT&CK Mapping

* Technique: T1003.005 – OS Credential Dumping: LSASS Memory

## Recommended Actions

* Immediately isolate affected domain controller
* Capture memory image for forensic analysis
* Reset all privileged credentials (priority: domain admins)
* Review authentication logs for lateral movement
* Hunt for persistence mechanisms (scheduled tasks, services, WMI)

## SOC Notes

Treat as active compromise until proven otherwise.
Check:

* PowerShell logs (Event ID 4104)
* Sysmon process creation events
* Kerberos ticket anomalies
* Remote execution traces (PsExec, WinRM)

---

# 📊 Standard SOC Severity Model (Used in This Lab)

* LOW: Noise / early indicators / requires monitoring
* MEDIUM: Confirmed suspicious behavior with limited scope
* HIGH: Active exploitation or credential compromise
* CRITICAL: Domain-level compromise or active attacker control

---
