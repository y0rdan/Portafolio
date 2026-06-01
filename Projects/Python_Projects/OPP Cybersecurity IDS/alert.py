class Alert:
    def __init__(self, event, risk, findings):
        self.event = event
        self.risk = risk
        self.findings = findings


    def severity(self):
        if self.risk >= 70:
            return "HIGH"
        elif self.risk >= 40:
            return "MEDIUM"
        return "LOW"



    def __str__(self):
        return (
            f"\n========== ALERT ==========\n"
            f"Timestamp : {self.event.timestamp}\n"
            f"Device    : {self.event.device}\n"
            f"Risk Score: {self.risk}\n"
            f"Severity  : {self.severity()}\n"
            f"Findings  : {', '.join(self.findings)}\n"
            f"===========================\n"
        )
