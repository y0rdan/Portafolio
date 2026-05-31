Write-Host "Applying Security Hardening Baseline..." -ForegroundColor Green

# Enable Windows Defender features
Set-MpPreference -DisableRealtimeMonitoring $false
Set-MpPreference -PUAProtection Enabled

# Enable ASR rules (baseline example set)
Add-MpPreference -AttackSurfaceReductionRules_Ids `
"56a863a9-875e-4185-98a7-b882c64b5ce5" `
-Force

# Enable Firewall profiles
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True

# Disable SMBv1
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart

# Enable audit policies
auditpol /set /category:* /success:enable /failure:enable

Write-Host "Baseline applied successfully."