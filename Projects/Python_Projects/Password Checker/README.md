# Password Strength Checker

Author: Yordan Borges

Interactive check for password complexity and for a match against `weak_pass.txt`.

A password scores one point for each of the following:

| Check | Rule |
| --- | --- |
| Lowercase | At least one `a-z` |
| Uppercase | At least one `A-Z` |
| Number | At least one `0-9` |
| Symbol | At least one character in `!@#$%^&*()_+~/` |
| Length | 8 characters or longer |

Maximum score is 5. Scores 0–1 are weak, 2–3 moderate, and 4–5 secure. A password that appears in `weak_pass.txt` is rejected before scoring.

The wordlist is loaded and used. It is not printed.

## Requirements

```bash
pip install colorama
```

## Files

```text
Password Checker/
├── main.py
├── weak_pass.txt
└── README.md
```

## Usage

```bash
python3 main.py
```

Run it from this folder so `weak_pass.txt` is found.
