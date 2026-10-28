# Yordan Borges

**Systems Engineer**

Systems administrator in a hybrid Microsoft environment (150+ endpoints and 30+ servers), looking for Systems Engineer roles. This repo is the lab work behind that: building and running identity infrastructure, hardening it with Group Policy, automating the routine work, and adding enough visibility to know when a system changes.

The place to start is the [Active Directory lab](./Projects/Active-Directory-Lab): two domain controllers, DNS and DHCP, exported GPO backups, and PowerShell for provisioning, health checks, and recovery.

The other projects support that systems work.

- **Hardening and secure configuration.** GPO backups, a local security baseline, and notes on how common attack paths show up so logging and policy choices are concrete.
- **Visibility.** A Splunk lab and a KQL detection library over Windows, identity, and endpoint events.
- **Automation.** PowerShell, Python tools, and n8n workflows that route alerts instead of leaving them in a console.

Microsoft SC-200, the Google Cybersecurity Professional Certificate, and the Cisco Networking Academy Cybersecurity Defense Analyst path are listed under Certifications. They support the systems work. They are not a separate track.

📫 [LinkedIn](https://www.linkedin.com/in/yordan-borges-b86791172) · [Email](mailto:yordanb00@yahoo.com) · [GitHub](https://github.com/y0rdan)

---

## Skills

| Area | What I use it for | Where it shows up |
| --- | --- | --- |
| Infrastructure and identity | Active Directory, DNS, DHCP, OU design, multi-DC replication, DFSR / SYSVOL | [Active Directory lab](./Projects/Active-Directory-Lab) |
| Hardening and secure configuration | Password and lockout policy, firewall, Defender baseline, local security policy, GPO | [GPO backups](./Projects/Active-Directory-Lab/GPO-Backups), [hardening script](./Projects/Active-Directory-Lab/Powershell/Security%20Hardening%20Baseline%20(Local%20Policy%20+%20Defender%20+%20Firewall).ps1), [hardening standard](./Projects/Active-Directory-Lab/Documentation/Security%20Hardening%20Standard.md) |
| Automation | User provisioning, health checks, GPO export, small Python tools, alert routing | [PowerShell](./Projects/Active-Directory-Lab/Powershell), [Python projects](./Projects/Python_Projects), [n8n workflow map](./Projects/Splunk-SOC-Automation-Lab/n8n-Workflows/Workflow%20Map.png) |
| Monitoring and reliability | Replication and DC health, Windows log visibility, file integrity, detection content | [AD health script](./Projects/Active-Directory-Lab/Powershell/AD%20Health%20Check%20+%20Replication%20Monitor.ps1), [Splunk lab](./Projects/Splunk-SOC-Automation-Lab), [KQL library](./KQL%20Detection%20Rule%20Library) |

---

## Projects

| Project | What it shows | Status |
| --- | --- | --- |
| [Active Directory lab](./Projects/Active-Directory-Lab) | Identity, DNS/DHCP, GPO hardening, replication, and recovery for a two-DC lab (`homelab.local`) | Documented lab. Includes `Documentation/`, `GPO-Backups/`, `Powershell/`, and `Screenshots/`. No `diagrams/` folder and no separate `recovery-procedures/` folder. Recovery is written up in `Documentation/`. |
| [Splunk lab](./Projects/Splunk-SOC-Automation-Lab) | Windows and endpoint log visibility, detection searches, and n8n alert routing | Write-up, searches, screenshots, a diagram, and Discord alert examples. No `sysmon-config/` or `powershell/` directory in this project. Sysmon is described, not shipped as a config file. |
| [KQL detection library](./KQL%20Detection%20Rule%20Library) | Detection content for identity, Windows, and endpoint events in Microsoft Sentinel | 12 rules mapped to MITRE ATT&CK. The [tuning log](./KQL%20Detection%20Rule%20Library/tuning-log/tuning-log.md) is a generic lab example, not a measured production baseline. |
| [Python tools](./Projects/Python_Projects) | Admin tooling: file integrity, log review, port checks, password hygiene, and a Caesar-cipher exercise | Source is in the repo. Run steps are below. The cipher stores the shift next to the text. It is a learning exercise, not encryption. |
| [Kali lab notes](./Projects/Kali%20Linux%20Attack%20Simulator) | Attack-path notes used to decide what to log and harden | README only. `scans/`, `exploits/`, `reports/`, and `screenshots/` are not in the repo. |
| [SOC report sample](./Projects/SOC%20Reports) and [templates](./SOC%20Report%20Templates) | A written investigation and reusable note templates | One sample report plus three templates. |

---

## Active Directory lab

Redundant domain controllers (DC01 `192.168.1.93`, DC02 `192.168.1.94`), AD-integrated DNS and DHCP, OU layout for users and groups, exported Group Policy backups, DFSR/SYSVOL notes, and PowerShell for provisioning, replication checks, GPO export, and a local hardening baseline.

![Group Policy Management](./Projects/Active-Directory-Lab/Screenshots/Group%20Policy%20Management.PNG)

![Active Directory Users and Computers](./Projects/Active-Directory-Lab/Screenshots/Active%20Directory%20Users%20and%20Computers.PNG)

Details, the server inventory, and the recovery notes: [Projects/Active-Directory-Lab](./Projects/Active-Directory-Lab).

---

## Visibility and automation

### Splunk lab

Windows event logs and Sysmon into Splunk, correlation searches, and an n8n workflow that posts an alert summary to Discord. Screenshots of the dashboard and the workflow are in the project folder.

![Splunk SOC Dashboard](./Projects/Splunk-SOC-Automation-Lab/Screenshots/Splunk%20SOC%20Dashboard.png)

### KQL detection library

Twelve Sentinel queries covering sign-ins, endpoint process events, Windows security events, and file activity. Each rule has a rationale and a response section. Tuning notes are an example lifecycle for a lab, with categories of noise rather than a real environment's exclusions.

| Technique | Tactic | Severity |
| --- | --- | --- |
| T1078 – Impossible travel | Initial Access | High |
| T1110 – Password spray | Credential Access | High |
| T1059.001 – Encoded PowerShell | Execution | High |
| T1003.001 – LSASS memory access | Credential Access | Critical |
| T1486 – Mass file rename | Impact | Critical |
| T1021.001 – RDP lateral movement | Lateral Movement | High |
| T1566.001 – Office macro spawning a shell | Initial Access | High |
| T1070.001 – Event log cleared | Defense Evasion | High |
| T1098 – Privileged role assigned | Privilege Escalation | High |
| T1053.005 – Scheduled task via CLI | Persistence | Medium |
| T1136.001 – Local account after hours | Persistence | Medium |
| T1018 – Internal port scanning | Discovery | Medium |

Index: [mitre-mapping.md](./KQL%20Detection%20Rule%20Library/mitre-mapping.md)

---

## How to run the Python tools

Use Python 3.8 or newer. Run each tool from its own folder. Only scan or crawl systems you are allowed to test.

### File integrity monitor

```bash
cd "Projects/Python_Projects/File_integrity_Monitoring_Tool"
pip install -r requirements.txt
python3 FIM.py -d /path/to/watch --init
python3 FIM.py -d /path/to/watch --scan
```

`--init` writes `baseline.json`. `--scan` reports added, modified, and deleted files. `pip install` is only needed for `--auto`.

### Password checker

```bash
cd "Projects/Python_Projects/Password Checker"
pip install colorama
python3 main.py
```

A password scores one point each for a lowercase letter, an uppercase letter, a digit, a symbol, and a length of 8 or more. Matches against `weak_pass.txt` are rejected. The wordlist is not printed.

### Caesar cipher exercise

```bash
cd Projects/Python_Projects/Encrypted
python3 main.py -e "HelloWorld" 5
python3 main.py -l
```

This shifts characters by an integer and stores the shift in the same SQLite row. It is practice with `sqlite3` and the standard library, not encryption. No third-party packages.

### Port scanner

```bash
cd "Projects/Python_Projects/Port Scanner"
pip install colorama
python3 scanner.py -t 127.0.0.1 -p 22,80,443
```

### Log analyzer

```bash
cd "Projects/Python_Projects/Log Analyzer"
pip install pandas colorama pwntools
python3 analyzer.py
```

The script reads `logs/sample_auth.log`. That sample log is not in the repo, so a run reports the missing file until you add one. Dependencies are pandas, colorama, and pwntools (`from pwn import log`).

### OOP intrusion-detection exercise

```bash
cd "Projects/Python_Projects/OOP Cybersecurity IDS"
python3 main.py
```

Standard library only. It scores three hard-coded sample events. It does not capture packets.

### Web crawler

```bash
cd "Projects/Python_Projects/Web Crawler"
pip install -r requirements.txt
python3 Web_crawler.py
```

Seed URLs come from `urls.txt`. Output goes to `crawled.txt` and `db/pages.db`, which are gitignored. The crawler does not obey `robots.txt`. Keep the seed list to sites you are allowed to fetch.

### Pygame practice

Space Invaders follows Tech With Tim's [Pygame Tutorial - Creating Space Invaders](https://www.youtube.com/watch?v=Q-__8Xw9KTM). Tetris is a separate practice game. Both need `pygame` and are not part of the systems labs.

```bash
cd "Projects/Python_Projects/PyGame Projects/Space Invaders"
pip install pygame
python3 main.py
```

---

## Certifications

- **Microsoft Certified: Security Operations Analyst Associate (SC-200)** — issued May 2026, expires May 2027
- **Google Cybersecurity Professional Certificate**
- **Cisco Networking Academy — Cybersecurity Defense Analyst path** (Splunk-focused)

---

## Tech stack

| Area | Tools |
| --- | --- |
| Identity and infrastructure | Active Directory, Group Policy, DNS, DHCP, DFSR, Windows Server, Hyper-V / VMware |
| Automation | PowerShell, Python, n8n |
| Monitoring and visibility | Splunk, Sysmon, Windows Event Logs, Microsoft Sentinel, KQL, Defender XDR |
| Hardening | Microsoft Defender, Windows Firewall, local security policy, GPO |

Attack-lab notes in the Kali folder use Nmap, Metasploit, Hydra, John the Ripper, and Gobuster as examples. That folder is a write-up only. Captured scan output is not in the repo.

---

## License

[MIT](./LICENSE). Copyright (c) 2026 Yordan Borges.
