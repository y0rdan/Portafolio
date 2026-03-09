from .base_detector import BaseDetector

class SuspiciousDomainDetector(BaseDetector):


    SUSPICIOUS_TLDS = [".ru", ".cn", ".xyz"]


    def analyze(self, event):

        if event.remote_url:
            url = event.remote_url.lower()

            for tld in self.SUSPICIOUS_TLDS:
                if tld in url:
                    return {
                        "type": f"Suspicious Domain ({tld})",
                        "risk": 30
                    }
                return None



