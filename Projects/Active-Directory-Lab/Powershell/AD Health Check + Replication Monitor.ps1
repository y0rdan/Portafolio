Write-Host "Running Domain Controller Health Checks..." -ForegroundColor Cyan

# Replication summary
Write-Host "`n[Replication Summary]"
repadmin /replsummary

# Detailed DC diagnostics
Write-Host "`n[DC Diagnostic Report]"
dcdiag /v | Select-String -Pattern "fail|error|warning" -CaseSensitive:$false

# Check replication failures
Write-Host "`n[Replication Failures]"
Get-ADReplicationFailure -Scope Site | Format-Table -AutoSize

# SYSVOL and Netlogon check
Write-Host "`n[SYSVOL Shares]"
net share | Select-String "SYSVOL|NETLOGON"

# DFSR service status
Write-Host "`n[DFSR Service Status]"
Get-Service DFSR | Select Name, Status