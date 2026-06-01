#!/usr/bin/env python3
"""
scanner.py - Simple multithreaded TCP port scanner with optional banner grabbing and CSV output.

Usage examples:
    python scanner.py -t 192.168.1.10 -p 22,80,443
    python scanner.py -t 10.0.0.5 -p 1-1024 -r 200 -T 0.5 -o results.csv
    python scanner.py -t example.com --top-ports 100 --banner
"""

import argparse
import socket
import threading
import queue
import csv
import time
from datetime import datetime
from colorama import init, Fore, Style
import os

init(autoreset=True)

# Common top ports (first ~100) for quick use
TOP_PORTS = [
    21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080,
    20,69,119,389,636,873,1433,1521,1720,2049,2222,3128,3307,3388,4444,5000,5432,5901,8000,8443,
    137,138,548,1645,1812,1813,2048,2401,2483,2484,5431,5902,6000,6667,7000,8081,8888,9000,9090
]

LOCK = threading.Lock()


def parse_ports(port_str):
    """Parse ports expression: '22', '22,80,8080', '1-1024' -> returns sorted list of ints."""
    ports = set()
    parts = port_str.split(',')
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if "-" in p:
            try:
                a, b = p.split('-', 1)
                a_i, b_i = int(a), int(b)
                if a_i > b_i:
                    a_i, b_i = b_i, a_i
                ports.update(range(max(1, a_i), min(65535, b_i) + 1))
            except ValueError:
                continue
        else:
            try:
                pi = int(p)
                if 1 <= pi <= 65535:
                    ports.add(pi)
            except ValueError:
                continue
    return sorted(ports)


def banner_grab(sock, timeout=1.0):
    """Attempt to read a small banner from an already-connected socket."""
    try:
        sock.settimeout(timeout)
        # Some services expect client data; we won't send anything by default.
        data = sock.recv(1024)
        return data.decode(errors='replace').strip()
    except Exception:
        return ""


def worker(host_ip, q, results, timeout, grab_banner):
    """Thread worker: get ports from queue, attempt connect, optionally grab banner."""
    while True:
        try:
            port = q.get_nowait()
        except queue.Empty:
            return
        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            start = time.time()
            s.connect((host_ip, port))
            elapsed = time.time() - start
            banner = ""
            if grab_banner:
                banner = banner_grab(s, timeout)
            entry = {
                "port": port,
                "status": "open",
                "banner": banner,
                "rtt_ms": int(elapsed * 1000)
            }
            with LOCK:
                results.append(entry)
                print(Fore.GREEN + f"[OPEN] {host_ip}:{port} ({entry['rtt_ms']} ms) {('- ' + banner) if banner else ''}" + Style.RESET_ALL)
        except (socket.timeout, ConnectionRefusedError, OSError):
            # Closed/unresponsive — we keep output minimal to avoid noise
            with LOCK:
                print(Fore.WHITE + f"[closed] {host_ip}:{port}" + Style.DIM, end="\r")
        except Exception as e:
            with LOCK:
                print(Fore.YELLOW + f"[!] {host_ip}:{port} error: {e}" + Style.RESET_ALL)
        finally:
            if s:
                try:
                    s.close()
                except Exception:
                    pass
            q.task_done()


def scan(host, ports, threads=100, timeout=0.5, grab_banner=False):
    """Main scanning function. Returns sorted list of result dicts."""
    q = queue.Queue()
    results = []
    for p in ports:
        q.put(p)

    try:
        resolved = socket.gethostbyname(host)
    except Exception as e:
        print(Fore.RED + f"Error: cannot resolve host {host}: {e}" + Style.RESET_ALL)
        return results

    print(Fore.CYAN + f"Scanning {host} ({resolved}) ports: {len(ports)} threads: {min(threads, len(ports))} timeout: {timeout}s" + Style.RESET_ALL)

    threads_list = []
    num_threads = min(threads, q.qsize() or 1)
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(resolved, q, results, timeout, grab_banner), daemon=True)
        t.start()
        threads_list.append(t)

    # Wait for queue to be fully processed
    try:
        q.join()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nUser interrupted. Exiting..." + Style.RESET_ALL)
        return results

    # sort results by port number
    results_sorted = sorted(results, key=lambda r: r["port"])
    return results_sorted


def save_csv(path, host, results):
    """Save results to CSV."""
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as csvf:
        writer = csv.DictWriter(csvf, fieldnames=["host", "port", "status", "rtt_ms", "banner"])
        writer.writeheader()
        for r in results:
            writer.writerow({
                "host": host,
                "port": r["port"],
                "status": r["status"],
                "rtt_ms": r.get("rtt_ms", ""),
                "banner": r.get("banner", "")
            })
    print(Fore.GREEN + f"[+] Results saved to {path}" + Style.RESET_ALL)


def main():
    parser = argparse.ArgumentParser(description="Simple multithreaded TCP port scanner")
    parser.add_argument("-t", "--target", required=True, help="Target hostname or IP")
    parser.add_argument("-p", "--ports", default="1-1024",
                        help="Ports (comma separated or ranges), e.g. 22,80,443 or 1-1024")
    parser.add_argument("-r", "--threads", type=int, default=200, help="Number of worker threads (default 200)")
    parser.add_argument("-T", "--timeout", type=float, default=0.5, help="Socket timeout in seconds (default 0.5)")
    parser.add_argument("--banner", action="store_true", help="Attempt to grab a small service banner from open ports")
    parser.add_argument("--top-ports", type=int, default=0, help="Scan 'top N' common ports (overrides -p if >0)")
    parser.add_argument("-o", "--output", help="CSV output file (optional)")

    args = parser.parse_args()

    if args.top_ports and args.top_ports > 0:
        ports = TOP_PORTS[:args.top_ports]
    else:
        ports = parse_ports(args.ports)

    if not ports:
        print(Fore.RED + "No valid ports to scan. Exiting." + Style.RESET_ALL)
        return

    start = time.time()
    results = scan(args.target, ports, threads=args.threads, timeout=args.timeout, grab_banner=args.banner)
    elapsed = time.time() - start

    open_ports = [r for r in results if r["status"] == "open"]
    print()
    print(Fore.CYAN + f"Scan finished in {elapsed:.2f}s. Open ports: {len(open_ports)}" + Style.RESET_ALL)
    for r in open_ports:
        print(Fore.GREEN + f" * {args.target}:{r['port']} ({r.get('rtt_ms', '')} ms) {('- ' + r['banner']) if r.get('banner') else ''}" + Style.RESET_ALL)

    if args.output:
        save_csv(args.output, args.target, results)


if __name__ == "__main__":
    main()
