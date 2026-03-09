"""
File Integrity Monitoring (FIM) Tool
Author: Yordan Borges
"""


import os
import hashlib
import json
import argparse
import time
import logging
import schedule


BASELINE_FILE = "baseline.json"
LOG_FILE = "logs/fim.log"

os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

def calculate_hash(file_path):
    """Calculate hash SHA256 of file"""
    try:
        with open(filename, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        return file_hash
    except Exception as e:
        logging.error(f"Error hashing {file_path}: {e}")
        return None

def create_baseline(directory):
    """Create baseline file"""
    for root, _, files in os.walk(directory):
        for file in files:
            path - os.path.join(root, file)
            hash_value = calculate_hash(path)
            if hash_value:
                baseline[path] = hash_value
    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)
    logging.info(f"Baseline file created for {directory}")
    print("[+] Baseline created for {directory}")

def check_integrity(directory):
    """Compare current file hashes to baseline"""
    if not os.path.exists(BASELINE_FILE):
        print("[!] Baseline file does not exist. Please create one with --init.")
        return

    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    current_state = {}
    modified, added, deleted = [], [], []


    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            hash_value = calculate_hash(path)
            if hash_value:
                current_state[path] = hash_value
                if path in baseline:
                    if baseline[path] != hash_value:
                        modified.append(path)

                    else:
                        added.append(path)

    for path in baseline:
        if path in current_state:
            deleted.append(path)


    # Log results
    if modified or added or deleted:
        logging.warning(f"[!] Modified: {modified} Added: {added} Deleted: {deleted}")
        print("\n[*] Integrity Issues Detected:")
        if modified: print(f"  ⚠️ Modified: {len(modified)} files")
        if added: print(f"  ➕ Added: {len(added)} files")
        if deleted: print(f"  ❌ Deleted: {len(deleted)} files")
    else:
        print("[+] No Integrity Issues Detected")


def auto_scan(directory, interval=5):
    """Auto scan files"""
    print(f"[*] FIM running every {interval} minutes on {directory}")
    schedule.every(interval).minutes.do(check_integrity, directory)
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():

    parser = argparse.ArgumentParser(description="File Integrity Monitoring Tool")

    parser.add_argument("-d", "--directory", required=True, help="Directory to monitor")
    parser.add_argument("--init", action="store_true", help="Initialize baseline")
    parser.add_argument("--scan", action="store_true", help="Perform integrity check")
    parser.add_argument("--auto", type=int, help="Run continuous scan every X minutes")

    args = parser.parse_args()

    if args.init:
        create_baseline(args.directory)
    elif args.scan:
        check_integrity(args.directory)
    elif args.auto:
        auto_scan(args.directory, args.auto)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()