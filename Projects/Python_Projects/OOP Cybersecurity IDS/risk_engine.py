
class RiskEngine:
    def __init__(self, detectors):
        self.detectors = detectors


    def evaluate(self, event):
        total_risk = 0
        findings = []

        for detector in self.detectors:
            result = detector.analyze(event)
            if result:
                findings.append(result["type"])
                total_risk += result["risk"]

        return total_risk, findings


