from event import SecurityEvent
from alert import Alert
from risk_engine import RiskEngine

from detectors.powershell_detector import PowerShellDetector
from detectors.suspicious_domain_detector import SuspiciousDomainDetector
from detectors.external_ip_detector import ExternalIPDetector

def main():

    alerts = []

    detectors = [
        PowerShellDetector(),
        SuspiciousDomainDetector(),
        ExternalIPDetector(),
    ]

    engine = RiskEngine(detectors)

    # Example Events:
    events = [
        SecurityEvent(
            "2026-03-03 12:00",
            "DESKTOP-01",
            "powershell -enc ZABpAHIA",
            "185.220.101.45",
            "malicious.xyz"
        ),
        SecurityEvent(
            "2026-03-03 12:10",
            "LAPTOP-02",
            "cmd.exe /c dir",
            "192.168.1.10",
            "internal.company.com"
        ),
        SecurityEvent(
            "2026-03-03 12:20",
            "SERVER-01",
            "powershell Get-Process",
            "8.8.8.8",
            "google.com"
        )
    ]

    for event in events:
           risk, findings = engine.evaluate(event)

           if risk > 0:
               alert = Alert(event, risk, findings)
               print(alert)
               alerts.append(alert)




if __name__ == "__main__":
    main()
