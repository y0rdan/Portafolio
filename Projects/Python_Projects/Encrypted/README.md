# Caesar Cipher Exercise (SQLite)

Author: Yordan Borges

This is a learning exercise. It is **not encryption**.

`main.py` shifts each character by an integer offset (a Caesar cipher) and stores the shifted text **and the offset** in the same SQLite row. Anyone who can read `db/encrypted.db` can reverse every value. Do not put real secrets in it.

There are no third-party dependencies. Python 3.8+ is enough.

## Usage

Run from this folder. The script creates `db/` if it is missing.

```bash
python3 main.py -e "HelloWorld" 5
python3 main.py -l
python3 main.py -d "Mjqqt\twqi"
python3 main.py -c
```

`-e` takes the text and the offset. `-d` looks that text up in the database and shifts it back by the stored offset. `-l` lists rows. `-c` deletes rows. `-o` appends the result to `encrypted.txt` (gitignored).

## What is stored

| Column | Meaning |
| --- | --- |
| id | Row id |
| encrypted | Shifted text. The column name is historical. The value is not encrypted. |
| offset | The shift, stored in plaintext next to the text |

## Why this is not encryption

A Caesar cipher is reversible by trying a small set of shifts. This script also saves the shift it used. The database file is a normal SQLite file with no key. The point of the exercise is the CLI, `sqlite3`, and file output, not confidentiality.
