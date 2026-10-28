from .base_detector import BaseDetector


class PowerShellDetector(BaseDetector):

    def analyze(self, event):
        if event.command:
            command = event.command.lower()
            if "powershell" in command and "-enc" in command:
                return {
                    "type": "Encoded PowerShell Execution",
                    "risk": 40
                }
            return None
