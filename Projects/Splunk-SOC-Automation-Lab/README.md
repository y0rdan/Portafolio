
# Splunk SOC Environment with AI-Driven Incident Automation and Discord Alerting

## Overview

This project implements a fully functional Security Operations Center (SOC) lab using Splunk Enterprise as the SIEM platform, enhanced with Sysmon telemetry, automated workflows via n8n, AI-driven incident analysis, and real-time alerting through Discord webhooks.

The environment simulates real-world SOC operations including log ingestion, threat detection, correlation rules, automated response workflows, and analyst-friendly incident summarization powered by AI.

The goal is to demonstrate practical skills in SIEM engineering, detection engineering, SOC operations, automation, and security incident response.

---

## Architecture

```

Endpoints (Windows 10/11 + Server)
│
▼
Sysmon + Windows Event Logs
│
▼
Splunk Universal Forwarder
│
▼
Splunk Enterprise (SIEM)
│
▼
Detection Rules / Correlation Searches
│
▼
n8n Workflow Automation
│
┌──────┴────────┐
▼               ▼
AI Incident Summary   Discord Alerts

````

---

## Lab Environment

| Hostname     | Role              | Purpose                      |
|--------------|------------------|------------------------------|
| SPLUNK01     | SIEM Server      | Log ingestion & analysis     |
| DC01         | Domain Controller| Authentication & AD logging  |
| WIN10-CLIENT | Endpoint         | Attack simulation source     |
| N8N01        | Automation Server | Workflow orchestration       |

---

## Technologies Used

- Splunk Enterprise
- Windows Server 2022
- Windows 10 / Windows 11
- Sysmon
- Splunk Universal Forwarder
- n8n Automation Platform
- Discord Webhooks
- OpenAI API
- PowerShell
- Windows Event Logs
- VirtualBox / VMware / Hyper-V

---

## Log Sources

- Windows Security Logs (Event Viewer)
- Sysmon event logs
- PowerShell logging
- Active Directory authentication logs
- DNS logs
- Endpoint process execution telemetry

---

## Sysmon Configuration

Sysmon is deployed to enhance endpoint visibility.

### Monitored Activities

- Process creation
- Network connections
- File creation/modification
- Registry changes
- PowerShell execution
- Parent-child process relationships

---

## Detection Engineering

Custom Splunk queries were created to detect:

- Brute force authentication attempts
- Suspicious PowerShell execution
- Encoded command execution
- Privilege escalation behavior
- Lateral movement patterns
- Unusual authentication activity

---

## Example Detection Queries

### Failed Login Detection
```splunk
index=wineventlog EventCode=4625
| stats count by Account_Name, Source_Network_Address
| sort -count
````

---

### Encoded PowerShell Detection

```splunk
index=sysmon EventCode=1
CommandLine="*EncodedCommand*"
```

---

### Brute Force Detection

```splunk
index=wineventlog EventCode=4625
| bucket span=5m _time
| stats count by Source_Network_Address
| where count > 10
```

---

## n8n Automation

n8n is used to automate SOC workflows and reduce manual analyst workload.

### Automated Functions

* Alert ingestion
* Incident parsing
* AI-based summarization
* Discord notifications
* IOC enrichment (extendable)
* Severity classification

---

## AI Incident Analysis

AI is integrated to enhance SOC alert context.

### Capabilities

* Incident summarization
* Threat severity classification
* Recommended response actions
* IOC explanation
* Event correlation insights

---

## Discord Alerting

Real-time SOC notifications are delivered to Discord via webhook.

### Alert Includes

* Hostname
* Severity level
* Source IP
* Detection rule triggered
* AI-generated summary
* Recommended response actions

---

### Example Alert

```
🚨 SECURITY ALERT
Host: WIN10-CLIENT
Severity: High
Detection: Suspicious PowerShell Execution
Source IP: 192.168.1.50

AI Summary:
Encoded PowerShell execution detected. This is commonly associated with malicious activity or post-exploitation behavior.

Recommended Action:
Isolate endpoint and review PowerShell process tree immediately.
```

---

## PowerShell Automation

### Splunk Forwarder Installation

```powershell
Start-Process msiexec.exe -ArgumentList `
"/i splunkforwarder.msi AGREETOLICENSE=Yes RECEIVING_INDEXER=splunk01:9997 /quiet"
```

### Sysmon Deployment

```powershell
sysmon64.exe -accepteula -i sysmonconfig.xml
```

---

## Incident Response Flow

1. Event detected in Splunk
2. Alert triggered via correlation search
3. Workflow sent to n8n
4. AI generates incident summary
5. Discord alert sent
6. Analyst investigates and responds

---

## Dashboards

Created Splunk dashboards for:

* Authentication monitoring
* Endpoint activity tracking
* PowerShell execution visibility
* Failed login trends
* Threat detection overview
* SOC incident dashboard

---

## Challenges

### Log Parsing Issues

* Inconsistent Windows event fields required normalization

**Fix:**

* Custom field extraction
* Standardized log parsing rules

### Duplicate Alerts

* n8n workflows initially created duplicate alerts

**Fix:**

* Deduplication logic added
* Alert throttling implemented

---

## Lessons Learned

* Log normalization is critical for SIEM effectiveness
* Automation reduces SOC workload significantly
* Alert tuning is required to prevent alert fatigue
* AI enhances analyst efficiency but requires validation
* Endpoint telemetry depth directly impacts detection quality

---

## Skills Demonstrated

* SIEM Engineering (Splunk)
* SOC Operations
* Detection Engineering
* Security Automation (n8n)
* Incident Response
* PowerShell Scripting
* AI Security Integration
* Endpoint Monitoring (Sysmon)
* Log Analysis & Correlation

---

## Future Improvements

* Splunk SOAR integration
* MITRE ATT&CK mapping
* VirusTotal API enrichment
* Slack/Teams integration
* Automated endpoint isolation
* Threat intelligence feeds
* Multi-tenant SOC architecture

---

## Repository Structure

```
splunk-soc-lab/
│
├── README.md
├── diagrams/
├── screenshots/
├── splunk-searches/
├── n8n-workflows/
├── powershell/
├── sysmon-config/
├── detection-rules/
└── documentation/
```



## Summary

This project demonstrates an end-to-end SOC pipeline integrating SIEM engineering, detection rules, automation workflows, and AI-assisted incident response.

It reflects real-world SOC operations including threat detection, log analysis, alert triage, and automated incident workflows used in modern enterprise security environments.

```
```
