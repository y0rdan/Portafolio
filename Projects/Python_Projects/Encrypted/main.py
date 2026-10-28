#!/usr/bin/env python3
"""Caesar-cipher learning exercise.

Shifts each character by an integer offset and stores the shifted text and
the offset in the same SQLite row. This is not encryption. Anyone who can
read the database can reverse every value. Do not store real secrets here.
"""
import sqlite3
from pathlib import Path
import argparse

# VARIABLES

db_path = Path("db/encrypted.db")
db_path.parent.mkdir(parents=True, exist_ok=True)

# Create DB if not exist

if db_path.exists():
    print(f"Database exists")

else:
    print(f"Database does not exist")
    print(f"Creating Database")

    with open ("db/encrypted.db", "w") as db:
        pass

# Initialize SQL Connection

conn = sqlite3.connect(db_path)
c = conn.cursor()

# Create Table if not exist

c.execute("CREATE TABLE IF NOT EXISTS encrypted (id INTEGER PRIMARY KEY AUTOINCREMENT, encrypted TEXT, offset NUMBER)")

# FUNCTIONS

def encrypt(text, rand):

    ascii_values = [ord(char) for char in text]
    encrypted = []

    for ascii_value in ascii_values:
        encrypted.append(chr(ascii_value + rand))

    encrypted_text = "".join(encrypted)
    return encrypted_text

def decrypt(text, rand):

    ascii_values = [ord(char) for char in text]
    decrypted = []

    for ascii_value in ascii_values:
        decrypted.append(chr(ascii_value - rand))

    decrypted_text = "".join(decrypted)
    return decrypted_text

def add(text, offset):

    c.execute("INSERT INTO encrypted (encrypted,offset)  VALUES (?,?)", (text,offset))
    conn.commit()

def clear_db():
    c.execute("DELETE FROM encrypted")
    conn.commit()

def print_db(db_path):
    print("[+] Printing Database\n\n")
    for row in c.execute("SELECT * FROM encrypted"):
        print(row)

def write_to_file(encrypted, filename):
    with open(filename, "a") as file:
        file.write(encrypted + "\n")


# Define Parser

parser = argparse.ArgumentParser(
    description="Caesar-cipher exercise. Stores the shift next to the text in SQLite. Not encryption."
)

parser.add_argument("-e", nargs = 2, help="encrypt text (use: -e <text> <offset>)")
parser.add_argument("-d", nargs = 1, help="decrypt text (use: -d <encrypted text>)")
parser.add_argument("-l", action='store_true', help="list Database (use: -l)")
parser.add_argument("-c", action='store_true', help="clear Database (use: -c)")
parser.add_argument("-o", action='store_true', help="output file (use with -e or -d flags)")

args = parser.parse_args()

# LOGIC

if args.e:
    text = args.e[0]
    offset =  int(args.e[1])

    encrypted = encrypt(text, offset)
    add(encrypted, offset)

    print(f"Shifted text: {encrypted} \n" )

    if args.o:
        output_file = "encrypted.txt"
        write_to_file(encrypted, output_file)
        print(f"Shifted text '{encrypted}' written to '{output_file}'")

elif args.d:
    text = args.d[0]

    c.execute("SELECT offset FROM encrypted WHERE encrypted = ?", (text,))
    row = c.fetchone()

    decrypted = None
    if row:  # Found a matching row
        offset = row[0]
        decrypted = decrypt(text, offset)
        print(f"Restored text: {decrypted} \n")
    else:
        print(f"Shifted text '{text}' not found in database \n")

    if args.o and decrypted is not None:
        output_file = "encrypted.txt"
        write_to_file(decrypted, output_file)
        print("[+] Output file created")

elif args.l:
    print_db(db_path)

elif args.c:
    clear_db()

else:
    parser.print_help()





