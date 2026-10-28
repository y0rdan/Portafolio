"""
File Integrity Monitoring (FIM) Tool
Author: Yordan Borges

Builds a SHA-256 baseline of a directory and reports files that were
added, modified, or deleted since that baseline.
"""

import os
import hashlib
import json
import argparse
import time
import logging


BASELINE_FILE = "baseline.json"
LOG_FILE = os.path.join("logs", "fim.log")


def _setup_logging():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def _skip(path):
    """Ignore this tool's own baseline and log so a scan does not flag them."""
    absolute = os.path.abspath(path)
    return absolute in {
        os.path.abspath(BASELINE_FILE),
        os.path.abspath(LOG_FILE),
    }


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    try:
        digest = hashlib.sha256()
        with open(file_path, "rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                digest.update(chunk)
        return digest.hexdigest()
    except OSError as exc:
        logging.error("Error hashing %s: %s", file_path, exc)
        return None


def _require_directory(directory):
    if not os.path.isdir(directory):
        print(f"[!] Directory not found: {directory}")
        return False
    return True


def create_baseline(directory):
    """Create a baseline of SHA-256 hashes for every file under directory."""
    if not _require_directory(directory):
        return

    baseline = {}
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            if _skip(path):
                continue
            hash_value = calculate_hash(path)
            if hash_value:
                baseline[path] = hash_value

    with open(BASELINE_FILE, "w", encoding="utf-8") as handle:
        json.dump(baseline, handle, indent=4)
    logging.info("Baseline file created for %s (%s files)", directory, len(baseline))
    print(f"[+] Baseline created for {directory} ({len(baseline)} files)")


def check_integrity(directory):
    """Compare current file hashes to the baseline."""
    if not _require_directory(directory):
        return
    if not os.path.exists(BASELINE_FILE):
        print("[!] Baseline file does not exist. Create one with --init.")
        return

    with open(BASELINE_FILE, "r", encoding="utf-8") as handle:
        baseline = json.load(handle)

    current_state = {}
    seen = set()
    modified, added, deleted = [], [], []

    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            if _skip(path):
                continue
            seen.add(path)
            hash_value = calculate_hash(path)
            if not hash_value:
                continue
            current_state[path] = hash_value
            if path not in baseline:
                added.append(path)
            elif baseline[path] != hash_value:
                modified.append(path)

    for path in baseline:
        if path not in seen:
            deleted.append(path)

    if modified or added or deleted:
        logging.warning("Modified: %s Added: %s Deleted: %s", modified, added, deleted)
        print("\n[*] Integrity issues detected:")
        if modified:
            print(f"  Modified: {len(modified)} files")
            for path in modified:
                print(f"    {path}")
        if added:
            print(f"  Added: {len(added)} files")
            for path in added:
                print(f"    {path}")
        if deleted:
            print(f"  Deleted: {len(deleted)} files")
            for path in deleted:
                print(f"    {path}")
    else:
        print("[+] No integrity issues detected")


def auto_scan(directory, interval=5):
    """Rescan on an interval. Requires the third-party schedule package."""
    try:
        import schedule
    except ImportError:
        print("[!] Auto scan needs the schedule package. Install it with: pip install schedule")
        return

    print(f"[*] FIM running every {interval} minutes on {directory}")
    schedule.every(interval).minutes.do(check_integrity, directory)
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    _setup_logging()
    parser = argparse.ArgumentParser(description="File Integrity Monitoring Tool")
    parser.add_argument("-d", "--directory", required=True, help="Directory to monitor")
    parser.add_argument("--init", action="store_true", help="Initialize baseline")
    parser.add_argument("--scan", action="store_true", help="Perform integrity check")
    parser.add_argument("--auto", type=int, help="Run a continuous scan every X minutes")
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
