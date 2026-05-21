# 🚨 AI-Powered SOC Automation Pipeline

## Splunk → n8n → OpenRouter AI → Discord

A lightweight Security Operations Center (SOC) automation environment designed to detect, enrich, and distribute Windows security alerts in real time using SIEM detections, workflow automation, and AI-driven analysis.

---

# 📌 Project Overview

This project integrates:

- **Splunk** for log ingestion and threat detection
- **n8n** for workflow orchestration and automation
- **OpenRouter AI models** for incident enrichment and SOC analysis
- **Discord** for real-time incident notification delivery

The pipeline converts raw Windows telemetry into structured SOC incident reports automatically.

---

# 🔄 Pipeline Architecture

```text
Windows Event Logs / Sysmon
                ↓
Splunk SIEM
(Detection Rules & Correlation Searches)
                ↓
Webhook Alert Trigger
                ↓
n8n Automation Workflow
                ↓
AI SOC Analyst Agent
(OpenRouter LLM)
                ↓
Discord Incident Channel
```

---

# 🔍 Detection Capabilities

The environment monitors and correlates Windows security events including:

| Event ID | Detection |
|----------|------------|
| 4625 | Failed Authentication Attempts |
| 4624 | Successful Logons |
| 4732 | Privileged Group Membership Changes |
| 4688 | Suspicious Process Execution |
| 7045 | Service Installation / Persistence |
| 1102 | Security Log Tampering |

---

# 🧠 AI Incident Enrichment

The AI layer transforms raw Splunk alerts into analyst-friendly SOC reports by performing:

- Threat classification
- MITRE ATT&CK mapping
- Severity scoring
- Behavioral analysis
- Incident summarization
- Response recommendations

---

# ⚙️ Automation Workflow

The n8n workflow receives webhook alerts directly from Splunk and normalizes the event data before sending it to the AI model.

## Example Payload Normalization

```javascript
return [{
  json: {
    alert: $json.alert_name,
    host: $json.host,
    user: $json.user,
    src_ip: $json.src_ip,
    count: $json.count,
    raw: $json
  }
}];
```

---

# 📣 Discord SOC Alert Example

```text
🚨 Splunk Alert: Failed Logon Brute Force

🖥 Host: DC1
👤 User: administrator
🌐 Source IP: 192.168.1.25
📊 Count: 27

🎯 Threat Classification:
Credential Brute Force Attempt

⚠ Severity:
HIGH

🧠 Analysis:
Multiple failed authentication attempts were detected against a Windows host, indicating possible brute force or password spraying activity.

🗺 MITRE ATT&CK Mapping:
- T1110 — Brute Force

🛡 Recommendations:
- Investigate source IP activity
- Review authentication logs
- Enforce account lockout policies

📌 SOC Notes:
Correlate with domain controller events and endpoint telemetry for additional indicators of compromise.
```

---

# 🛠 Technologies Used

| Category | Technologies |
|----------|---------------|
| SIEM | Splunk |
| Automation | n8n |
| AI | OpenRouter |
| Monitoring | Windows Event Logs, Sysmon |
| Notification | Discord Webhooks |
| Scripting | Python, Bash |
| Operating Systems | Windows, Linux |

---

# 🔐 Security Features

- Automated alert triage
- Real-time incident delivery
- AI-assisted threat analysis
- Windows event correlation
- MITRE ATT&CK contextual mapping
- SOC-ready reporting format

---

# 🚀 Planned Improvements

- Microsoft Defender automated response integration
- Threat intelligence enrichment (VirusTotal / AbuseIPDB)
- Alert deduplication engine
- Multi-channel notifications (Slack / Teams)
- Centralized incident archival
- AI-assisted remediation workflows

---

# 🎯 Project Goal

The objective of this project is to demonstrate how SIEM detections, workflow automation, and large language models can be combined to build a modern SOC automation environment capable of reducing analyst workload and accelerating incident response.

---