# Python Projects

Small Python tools and two Pygame practice games. The tools are here to show scripting for systems work: file integrity, log review, port checks, and password hygiene. The Caesar-cipher script is a learning exercise, not an encryption tool.

Run each project from its own folder. The portfolio README has the same commands with a bit more context.

| Folder | What it is | Run |
| --- | --- | --- |
| `File_integrity_Monitoring_Tool/` | SHA-256 baseline and change report | `pip install -r requirements.txt` then `python3 FIM.py -d /path --init` and `--scan` |
| `Password Checker/` | Complexity score and a weak-password list | `pip install colorama` then `python3 main.py` |
| `Encrypted/` | Caesar cipher stored in SQLite. Not encryption. | `python3 main.py -e "HelloWorld" 5` |
| `Port Scanner/` | Multithreaded TCP connect scan for labs you are allowed to test | `pip install colorama` then `python3 scanner.py -t 127.0.0.1 -p 22,80` |
| `Log Analyzer/` | Reads `logs/sample_auth.log` (not included) | `pip install pandas colorama pwntools` then `python3 analyzer.py` |
| `OOP Cybersecurity IDS/` | OOP detectors scored against three sample events. No packet capture. | `python3 main.py` |
| `Web Crawler/` | Fetches seed URLs from `urls.txt` | `pip install -r requirements.txt` then `python3 Web_crawler.py` |
| `PyGame Projects/Space Invaders/` | Practice game based on [Tech With Tim's tutorial](https://www.youtube.com/watch?v=Q-__8Xw9KTM) | `pip install pygame` then `python3 main.py` |
| `PyGame Projects/Tetris/` | Practice game | `pip install pygame` then `python3 main.py` |

Generated files (`*.db`, `encrypted.txt`, `crawled.txt`, `baseline.json`, `__pycache__/`) are gitignored.
