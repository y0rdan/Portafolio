Import-Module GroupPolicy

$BackupPath = "C:\GPO-Backups"
New-Item -ItemType Directory -Path $BackupPath -Force | Out-Null

Get-GPO -All | ForEach-Object {
    Backup-GPO -Name $_.DisplayName -Path $BackupPath
}

Write-Host "All GPOs backed up to $BackupPath"