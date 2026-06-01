🚨 Splunk Alert: Mimikatz Indicators

🖥 Host: DC1.homelab.local
👤 User: HOMELAB\tjoe
🌐 Source IP: 192.168.1.104:5678
📊 Count:

🎯 Threat Classification: Credential Dumping – possible use of Mimikatz to extract credentials from memory

⚠ Severity: HIGH

🧠 Analysis:
The alert indicates that the account “HOMELAB\tjoe” on the domain controller executed a tool matching Mimikatz signatures. Mimikatz is commonly used to dump LSASS memory and retrieve plaintext passwords, NTLM hashes, or Kerberos tickets. Execution on a DC suggests a high‑value target; if successful, attackers could gain domain‑wide privileges. No prior occurrence is recorded for this host, increasing suspicion.

🗺 MITRE ATT&CK Mapping:

Technique ID: T1003.005
Technique Name: OS Credential Dumping: LSASS Memory
Brief explanation: The observed Mimikatz activity aligns with extracting credentials directly from the LSASS process on a domain controller, matching the described behavior.

🛡 Recommendations:

Isolate DC1.homelab.local from the network pending investigation.
Collect volatile memory dumps and LSASS logs from the host for forensic analysis; search for credential artifacts.
Reset passwords for privileged accounts, especially “joe”, and enforce adaptive multi‑factor authentication.

📌 SOC Notes:
Verify whether “joe” has a legitimate justification for running credential‑dumping tools (e.g., admin troubleshooting).
Check endpoint detection logs for prior or concurrent suspicious processes (e.g., PowerShell, Regsvr32).
If evidence confirms malicious use, elevate to Incident Response and consider threat hunting for lateral movement across the domain.