# File Integrity Monitoring (FIM) Tool

Author: Yordan Borges

A small Python tool that hashes a directory with SHA-256, saves that baseline, and reports files that were added, modified, or deleted later. It is aimed at system administrators who want a simple integrity check on config or content directories.

## Requirements

- Python 3.8+
- `schedule` is required only for `--auto`. `--init` and `--scan` use the standard library.

```bash
pip install -r requirements.txt
```

## Usage

Run these commands from this folder. The baseline is written to `baseline.json` in the current directory, and events are appended to `logs/fim.log`. Both paths are gitignored.

```bash
python3 FIM.py -d /path/to/watch --init
python3 FIM.py -d /path/to/watch --scan
python3 FIM.py -d /path/to/watch --auto 10
```

`--auto` repeats the scan every 10 minutes in that last example.

## What the scan reports

| Result | Meaning |
| --- | --- |
| Modified | Path is in the baseline and the SHA-256 hash changed |
| Added | Path is on disk and was not in the baseline |
| Deleted | Path was in the baseline and is no longer on disk |

The tool skips its own `baseline.json` and `logs/fim.log` so those files are not reported as changes.

## Files in this folder

```text
File_integrity_Monitoring_Tool/
├── FIM.py
├── requirements.txt
└── README.md
```

`baseline.json` and `logs/` are created when you run the tool. They are not part of the repo.
