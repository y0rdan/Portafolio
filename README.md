# 👋 Hi, I'm Yordan Borges

**Microsoft SC-200 Certified | Systems Administrator | SOC/Blue Team | Detection Engineering**

Systems Administrator managing 150+ endpoints and 30+ servers in a hybrid Microsoft enterprise environment, building toward SOC analyst and detection engineering work. This repo is my hands-on lab work: production-style detection rules, a full SOC automation pipeline, an enterprise AD environment, and security tooling in Python.

📫 [LinkedIn](https://www.linkedin.com/in/yordan-borges-b86791172) · [Email](mailto:yordanb00@yahoo.com) · [GitHub](https://github.com/y0rdan)

---

## 🏆 Certifications

- **Microsoft Certified: Security Operations Analyst Associate (SC-200)** — issued May 2026, expires May 2027
- **Google Cybersecurity Professional Certificate**
- **Cisco Networking Academy — Cybersecurity Defense Analyst path** (Splunk-focused)

---

## 📁 What's in This Repo

| Folder | What it is |
|---|---|
| [`KQL Detection Rule Library`](./KQL%20Detection%20Rule%20Library) | 12 production-ready Sentinel detection rules mapped to MITRE ATT&CK v14, with tuning logs |
| [`Projects/Splunk-SOC-Automation-Lab`](./Projects/Splunk-SOC-Automation-Lab) | Splunk SIEM + Sysmon + n8n automation + AI incident summarization + Discord alerting |
| [`Projects/Active-Directory-Lab`](./Projects/Active-Directory-Lab) | Multi-DC enterprise AD environment: DNS/DHCP, GPO hardening, DFSR, disaster recovery |
| [`Projects/Kali Linux Attack Simulator`](./Projects/Kali%20Linux%20Attack%20Simulator) | Red team lab — recon through post-exploitation against vulnerable VMs |
| [`Projects/Python_Projects`](./Projects/Python_Projects) | Security tooling in Python (IDS, FIM, log analyzer, port scanner, password checker, encryption utility) |
| [`Projects/SOC Reports`](./Projects/SOC%20Reports) | Sample incident investigation reports |
| [`SOC Report Templates`](./SOC%20Report%20Templates) | Reusable incident response runbook, investigation notes, and mitigation playbook templates |

---

## 🔎 KQL Detection Rule Library

12 Microsoft Sentinel detection rules, each with detection rationale, production-tested KQL, a false-positive tuning log, and analyst escalation notes. Built around a structured tuning lifecycle (baseline → root-cause FPs → apply exclusions → re-baseline → lock) targeting under 5 alerts/day for high-volume rules and under 1/week for critical ones.

| Technique | Tactic | Severity |
|---|---|---|
| T1078 – Impossible Travel Login | Initial Access | High |
| T1110 – Password Spray | Credential Access | High |
| T1059.001 – Encoded PowerShell | Execution | High |
| T1003.001 – LSASS Memory Access | Credential Access | Critical |
| T1486 – Mass File Rename (Ransomware) | Impact | Critical |
| T1021.001 – RDP Lateral Movement | Lateral Movement | High |
| T1566.001 – Office Macro Spawning Shell | Initial Access | High |
| T1070.001 – Event Log Cleared | Defense Evasion | High |
| T1098 – Privileged Role Assigned | Privilege Escalation | High |
| T1053.005 – Scheduled Task via CLI | Persistence | Medium |
| T1136.001 – Local Account After Hours | Persistence | Medium |
| T1018 – Internal Port Scanning | Discovery | Medium |

Full index: [`mitre-mapping.md`](./KQL%20Detection%20Rule%20Library/mitre-mapping.md)

---

## 🛡️ Featured Labs

### Splunk SOC Automation Lab
End-to-end SOC pipeline: Sysmon + Windows Event Logs → Splunk Universal Forwarder → Splunk Enterprise → correlation searches → n8n workflow automation → AI-generated incident summaries + real-time Discord alerting.

![Splunk SOC Dashboard](./Projects/Splunk-SOC-Automation-Lab/Screenshots/Splunk%20SOC%20Dashboard.png)
![Discord Alert - Brute Force](./Projects/Splunk-SOC-Automation-Lab/Screenshots/Splunk%20Alert%20-%20Failed%20Logon%20Brute%20Force%20(EventCode%204625).png)

### Enterprise Active Directory Lab
Redundant domain controllers (DC01/DC02), AD-integrated DNS/DHCP, GPO security hardening (exported backups included), DFSR replication validation, and PowerShell-driven disaster recovery testing.

![Group Policy Management](./Projects/Active-Directory-Lab/Screenshots/Group%20Piolicy%20Management.PNG)

### Kali Linux Attack Simulation Lab
Controlled red team exercises against intentionally vulnerable VMs (Metasploitable2, DVWA) using Nmap, Metasploit, Hydra, John the Ripper, and Gobuster — recon through privilege escalation and post-exploitation, documented end to end.

---

## 🐍 Python Security Tools

- **OPP Cybersecurity IDS** — modular, OOP-based intrusion detection system with pluggable detectors (PowerShell abuse, suspicious domains, external IPs)
- **File Integrity Monitoring Tool** — SHA-256 hash-based change detection for files/directories
- **Log Analyzer** — parses logs for anomaly and suspicious-activity patterns
- **Port Scanner** — multithreaded TCP scanner with banner grabbing
- **Password Checker** — validates passwords against known weak-password lists
- **Encrypted DB Tool** — SQLite-based encryption/decryption utility

---

## 🧰 Tech Stack

| Category | Tools |
|---|---|
| SIEM / Detection | Microsoft Sentinel, Defender XDR, Splunk, Sysmon, KQL, SPL |
| Identity / Infra | Active Directory, Entra ID, Group Policy, DNS, DHCP, Intune, Azure Arc |
| Automation | n8n, PowerShell, Python |
| Offensive Tooling | Kali Linux, Metasploit, Nmap, Burp Suite, Hydra |
| Platforms | Windows Server 2019/2022/2025, Ubuntu/Kali, Azure |

---

## ⚡ Fun Fact

> "Security is not about tools. It's about visibility, correlation, and response."
