<#
.SYNOPSIS
    Create one Active Directory user in the homelab.local lab.

.DESCRIPTION
    Sample identity values match the lab documented in the Active Directory README.
    The password is never stored in this file. Pass -AccountPassword, or leave it
    empty and the script prompts with Read-Host -AsSecureString.

.EXAMPLE
    .\Add User.ps1

.EXAMPLE
    $secret = Read-Host -Prompt "Password" -AsSecureString
    .\Add User.ps1 -SamAccountName "jdoe" -AccountPassword $secret
#>
[CmdletBinding()]
param(
    [string]$Name = "John Doe",
    [string]$GivenName = "John",
    [string]$Surname = "Doe",
    [string]$SamAccountName = "jdoe",
    [string]$UserPrincipalName = "jdoe@homelab.local",
    [string]$Path = "OU=Users,DC=homelab,DC=local",
    [securestring]$AccountPassword
)

Import-Module ActiveDirectory

if (-not $AccountPassword) {
    $AccountPassword = Read-Host -Prompt "Password for $SamAccountName" -AsSecureString
}

New-ADUser `
    -Name $Name `
    -GivenName $GivenName `
    -Surname $Surname `
    -SamAccountName $SamAccountName `
    -UserPrincipalName $UserPrincipalName `
    -Path $Path `
    -AccountPassword $AccountPassword `
    -Enabled $true `
    -PasswordNeverExpires $false
