---

# 🔐 SQLite Text Encryption Tool

This is a simple **command-line Python tool** for encrypting and decrypting text strings using a **custom ASCII offset algorithm**.
All encrypted values (and their offsets) are stored in a local **SQLite database** for later retrieval and decryption.

---

## 🚀 Features

✅ Encrypt any text using a numeric offset
✅ Decrypt text stored in the database
✅ Automatically creates and manages a local SQLite database
✅ List and clear all entries in the database
✅ Optionally write encrypted/decrypted output to a text file

---

## 🧩 Requirements

* Python **3.8+**
* No external dependencies (uses only Python’s standard library)

---

## 📁 Database Structure

The script automatically creates a database at:

```
db/encrypted.db
```

Table: **`encrypted`**

| Column    | Type    | Description                  |
| --------- | ------- | ---------------------------- |
| id        | INTEGER | Primary key (auto increment) |
| encrypted | TEXT    | Encrypted text value         |
| offset    | NUMBER  | Offset used for encryption   |

---

## ⚙️ Usage

### Run with:

```bash
python3 main.py [options]
```

---

### 🔸 Encrypt Text

```bash
python3 main.py -e "HelloWorld" 5
```

**Example Output:**

```
Encrypted Output: Mjqqt\|twqi
```

Also stores the encrypted string and offset in the database.

#### Save output to file:

```bash
python3 main.py -e "HelloWorld" 5 -o
```

→ Writes the result to `encrypted.txt`

---

### 🔸 Decrypt Text

```bash
python3 main.py -d "Mjqqt\|twqi"
```

**Example Output:**

```
Decrypted text: HelloWorld
```

#### Save decrypted text to file:

```bash
python3 main.py -d "Mjqqt\|twqi" -o
```

---

### 🔸 List Database Contents

```bash
python3 main.py -l
```

**Example Output:**

```
[+] Printing Database

(1, 'Mjqqt\|twqi', 5)
```

---

### 🔸 Clear the Database

```bash
python3 main.py -c
```

Deletes all entries from the database.

---

## 🧠 How It Works

The encryption method is a **basic ASCII offset cipher**:

* Each character’s ASCII code is increased by the chosen offset when encrypting.
* During decryption, the same offset is subtracted.

Example:

| Character | ASCII | Offset | Encrypted ASCII | Encrypted Char |
| --------- | ----- | ------ | --------------- | -------------- |
| H         | 72    | +5     | 77              | M              |

---

## 📄 File Output

If the `-o` flag is used, the script will write the encrypted or decrypted output to:

```
encrypted.txt
```

Each result is appended on a new line.

---

## 🧰 Example Workflow

```bash
# Encrypt and store
python3 main.py -e "Secret123" 3

# Decrypt from DB
python3 main.py -d "Vhfuhw456"

# List database
python3 main.py -l

# Clear database
python3 main.py -c
```

---

## ⚠️ Notes

* Offsets must be **integer values**.
* The script will **create the `db/` directory** and database automatically if they don’t exist.
* It’s a **learning/demo encryption** — not secure for real sensitive data.

---
## 🧑‍💻 Author

**Yordan Borges**
Coding Portfolio Project
---
