import re
import pandas as pd
from datetime import datetime
from colorama import Fore, Style
from pwn import log
import os

import sys
from numpy.ma.testutils import fail_if_equal

#  === CONFIGURATION ===
LOG_FILE = "logs/sample_auth.log"
REPORT_FILE = "reports/report.csv"
f = Fore

# === DETECTION RULES ===

FAILED_LOGIN_THREASHOLD = 5
SUSPICIOUS_IPS = ["45.", "185.", "222."]


# === REGEX FOR LOG PATTERNS

FAILED_LOGIN_PATTERN = r"Failed password for invalid user (\w+) from ([\d\.]+)"
SUCCESS_LOGIN_PATTERN = r"Accepted password for (\w+) from ([\d\.]+)"
ROOT_ACCESS_PATTERN = r"session opened for user root"


# == STORAGE FOR ALERTS

alerts = []


# === FUNCTIONS ===

def log_alert(message, severity="INFO"):
    color = {
        "INFO": f.CYAN,
        "WARNING": f.YELLOW,
        "CRITICAL": f.RED
    }.get(severity, f.WHITE)

    print(f"{color}[{severity}]: {message}{Style.RESET_ALL}")
    alerts.append({
        "timestamp": datetime.now().isoformat(),
        "severity": severity,
        "message": message
    })

def analyze_log_file(path):
    if not os.path.exists(path):
        log_alert("No such file or directory: '{}'".format(path))
        return

    with open(path, "r", errors="ignore") as f:
        lines = f.readlines()
        print(lines)


    # === DETECTS FAILE LOGINS ===

    failed_attempts = {}

    for line in lines:
        failed = re.search(FAILED_LOGIN_PATTERN, line)
        if failed:
            user, ip = failed.groups()
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
            if failed_attempts[ip] >= FAILED_LOGIN_THREASHOLD:
                log_alert(f"Multiple failed logins {{failed={failed_attempts[ip]}) from {ip}", "WARNING")


        # === DETECTS SUCCESSFUL LOGINS ===

        succeed = re.search(SUCCESS_LOGIN_PATTERN, line)
        if succeed:
            user, ip = succeed.groups()
            if any(ip.startswith(ip) for ip in SUSPICIOUS_IPS):
                log_alert(f"Successful Login for user: {user} from Suspicious IP: {ip}", "CRITICAL")


        # === DETECTS ROOT ACCESS ===

        if re.search(ROOT_ACCESS_PATTERN, line):
            log_alert(f"Root Access Detected {line.strip()}", "WARNING")


def export_report():
    if not alerts:
        print(f"Nothing to export")
        return

    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    pd.DataFrame(alerts).to_csv(REPORT_FILE, index=False)
    print(Fore.GREEN + f"\n[+] Report saved to: {REPORT_FILE}" + Style.RESET_ALL)
    log.success(f"[!] Logs Analyzed Successfully!")


# === Main ===

if __name__ == "__main__":


    print(Fore.CYAN + "\n=== Log Analyzer & Alerting Tool ===" + Style.RESET_ALL)
    log.info("[!] Starting Log Analyzer...")


    analyze_log_file(LOG_FILE)
    export_report()



