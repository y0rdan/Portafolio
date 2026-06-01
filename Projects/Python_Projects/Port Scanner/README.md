# TCP Port Scanner (multithreaded)

A simple, multithreaded TCP port scanner with optional banner grabbing and CSV output.
Designed for quick host/port enumeration in lab or authorized testing. **Only scan systems you own or have explicit permission to test.**

## Features
- Scan port ranges, comma-separated lists, or the top N common ports
- Multithreaded workers for faster scanning
- Optional banner grabbing for basic service identification
- Save results to CSV for further analysis
- Colorized terminal output

## Requirements
- Python 3.8+
- `colorama` (for colored terminal output)

Install dependency:

```bash
pip install colorama
```

Usage
# Scan default 1-1024 ports on a target
python scanner.py -t 192.168.1.10

# Scan specific ports
python scanner.py -t example.com -p 22,80,443

# Scan a range with 200 threads, 0.5s timeout and save to file
python scanner.py -t 10.0.0.5 -p 1-1024 -r 200 -T 0.5 -o results.csv

# Scan top 100 common ports and attempt banner grabbing
python scanner.py -t example.com --top-ports 100 --banner

Command Line Options

-t, --target — required. Target hostname or IP address.

-p, --ports — Ports to scan. Comma-separated values and ranges (e.g. 22,80,443 or 1-1024). Default: 1-1024.

-r, --threads — Number of worker threads (default 200).

-T, --timeout — Socket timeout in seconds (default 0.5).

--banner — Attempt to read a small banner from open ports.

--top-ports — Scan the top N common ports (overrides -p when > 0).

-o, --output — CSV output file (optional).

Output

Console: colorized status lines. Open ports printed in green with RTT and optional banner.

CSV: saved with columns host,port,status,rtt_ms,banner.

Implementation Notes

Default timeout 0.5s is aggressive for remote hosts; increase for WAN/latency.

Banner grabbing is simple; some protocols require sending data to elicit a banner.

Respect legal constraints: only scan authorized targets.