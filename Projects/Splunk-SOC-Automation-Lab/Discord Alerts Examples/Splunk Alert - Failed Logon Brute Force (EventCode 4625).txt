🚨 Splunk Alert: Failed Logon Brute Force (EventCode 4625)

🖥 Host: 192.168.1.104:5678
👤 User: tjoe
🌐 Source IP: 192.168.1.104:5678
📊 Count: 4

🎯 Threat Classification: Brute‑force password guessing against a regular user account

⚠ Severity:
LOW

🧠 Analysis:
Four failed logon events (4625) were generated for user tjoe from the same host/IP. The low volume and identical source/target suggest a local credential check or a modest automated attempt. While immediate risk is limited, repeated attempts could evolve into a credential‑spraying or brute‑force campaign targeting this account.

🗺 MITRE ATT&CK Mapping:

Technique ID: T1110
Technique Name: Brute Force
Brief explanation: Multiple consecutive failed authentication attempts correspond to the Brute Force technique used to discover valid credentials.

🛡 Recommendations:

Verify that no scheduled tasks, scripts, or health‑check processes are using the tjoe account and causing failed logons.
Enforce account lockout thresholds and enable multi‑factor authentication for interactive accounts.
Increase monitoring for a rise in failed‑logon attempts or any successful logons from this account and block the source if activity escalates.

📌 SOC Notes:
Correlate these events with successful logon (4624) records and related process logs to detect any follow‑up activity.
Consider this a low‑priority alert unless the count increases, successful logons appear, or additional suspicious indicators emerge.
Escalate to Tier 2 if the pattern expands or if evidence of lateral movement, privilege escalation, or data exfiltration is observed.
🚨 Splunk Alert: Failed Logon Brute Force (EventCode 4625)

🖥 Host: 192.168.1.104:5678
👤 User: -
🌐 Source IP: 192.168.1.104:5678
📊 Count: 4

🎯 Threat Classification: Brute‑force password attempts with unknown username

⚠ Severity:
LOW

🧠 Analysis:
Four failed logon events (4625) were recorded from the same host/IP but the username field is empty. This pattern often indicates automated credential‑spraying or a script probing for valid accounts without specifying a user name. The low count and internal source suggest limited risk, but the activity should be tracked for escalation.

🗺 MITRE ATT&CK Mapping:

Technique ID: T1110
Technique Name: Brute Force
Brief explanation: Repeated failed authentication attempts align with the Brute Force technique used to discover valid credentials, even when the username is not supplied.

🛡 Recommendations:
Verify scheduled tasks, health‑check scripts, or monitoring tools that might generate anonymous failed logons and ensure they are legitimate.
Implement account lockout thresholds and consider MFA for interactive accounts to reduce the impact of credential‑spraying.
Enable alerts for increased failed‑logon volume or successful logons from the same source and block the IP if suspicious activity escalates.

📌 SOC Notes:
Correlate these events with successful logon (4624) records and process creation logs to detect any follow‑up activity.
Consider this a low‑priority alert unless the count rises or successful logons appear.
Escalate to Tier 2 if the frequency increases, successful authentication occurs, or additional indicators of compromise (e.g., lateral movement) are observed.
