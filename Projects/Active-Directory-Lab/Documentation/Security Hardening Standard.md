# Windows Server Security Hardening Standard

## Purpose

Defines baseline security configuration for all domain controllers and servers in the lab environment.

---

## Identity Security

- Strong password policies enforced
- Account lockout thresholds configured
- Privileged accounts restricted

---

## Network Security

- Windows Firewall enabled on all profiles
- RDP restricted to administrative hosts
- SMBv1 disabled

---

## Endpoint Protection

- Microsoft Defender enabled
- Real-time protection enforced
- PUA protection enabled
- Attack Surface Reduction rules configured

---

## Logging & Auditing

- Advanced audit policies enabled
- Logon/logoff tracking enabled
- Directory service access logging enabled

---

## PowerShell Security

- Script execution policy restricted
- PowerShell logging enabled
- Module logging enabled

---

## Administrative Controls

- GPO-based enforcement for all policies
- Least privilege access model
- Delegation instead of full admin rights

---

## Objective

Reduce attack surface, improve visibility, and enforce consistent enterprise security posture across all systems.