
# Splunk Detection Queries – SOC Project

## 1. AS-REP Roasting Detection
```spl
index=wineventlog EventCode=4768 Pre_Authentication_Type=0
| stats count by Account_Name, Client_Address
| where count > 1
````

## 2. Account Lockout Detection

```spl
index=wineventlog EventCode=4740
| stats count by Account_Name, host
```

## 3. Failed Logon Brute Force (EventCode 4625)

```spl
index=wineventlog EventCode=4625
| stats count by Account_Name, Source_Network_Address
| where count > 10
```

## 4. High-Value Correlation Search

```spl
index=wineventlog (EventCode=4625 OR EventCode=4624 OR EventCode=4672 OR EventCode=4688)
| stats values(EventCode) as Events count by Account_Name, Source_Network_Address
| where count > 20
```

## 5. Kerberoasting Detection

```spl
index=wineventlog EventCode=4769
| stats count by Account_Name, Service_Name, Client_Address
| where count > 20
```

## 6. Mimikatz Indicators

```spl
index=wineventlog EventCode=4688
(CommandLine="*mimikatz*" OR CommandLine="*sekurlsa*" OR CommandLine="*lsadump*")
```

## 7. New Local Administrator Created

```spl
index=wineventlog (EventCode=4720 OR EventCode=4732)
| stats count by Account_Name, Target_User_Name, host
```

## 8. PowerShell Encoded Commands

```spl
index=wineventlog EventCode=4104
("EncodedCommand" OR "-enc")
| stats count by User, host
```

## 9. SMB Enumeration

```spl
index=wineventlog EventCode=5140
| stats count by Source_Address, Share_Name
| where count > 50
```

## 10. Successful Logon After Multiple Failures

```spl
index=wineventlog (EventCode=4625 OR EventCode=4624)
| stats count(eval(EventCode=4625)) as Failures count(eval(EventCode=4624)) as Success by Account_Name, Source_Network_Address
| where Failures > 5 AND Success > 0
```

## 11. Suspicious PowerShell Download Activity

```spl
index=wineventlog EventCode=4104
("DownloadString" OR "Invoke-WebRequest" OR "IEX" OR "Net.WebClient")
| stats count by User, host
```

## 12. Suspicious Process Creation

```spl
index=wineventlog EventCode=4688
(CommandLine="*powershell*" OR CommandLine="*cmd.exe*" OR CommandLine="*rundll32*" OR CommandLine="*regsvr32*")
| stats count by ParentProcessName, New_Process_Name, Account_Name
```

```
```
