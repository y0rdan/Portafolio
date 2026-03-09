from .base_detector import BaseDetector
import ipaddress

class ExternalIPDetector(BaseDetector):

    def analyze(self, event):
        if event.remote_ip:
            try:
                ip = ipaddress.ip_address(event.remote_ip)

                if not ip.is_private:
                    return {
                        "type": "External IP Connection",
                        "risk": 20
                    }
            except ValueError:
                pass

        return None