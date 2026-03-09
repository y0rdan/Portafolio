# 🛡️ File Integrity Monitoring (FIM) Tool

A lightweight Python-based **File Integrity Monitoring (FIM)** utility designed to detect unauthorized file modifications, additions, and deletions on monitored directories.  

This tool helps system administrators and cybersecurity analysts ensure **data integrity** and **early threat detection** across critical systems.

---

## 🚀 Features

- 🧮 **Baseline Creation:** Generates cryptographic SHA256 hashes of all files in a directory  
- 🔍 **Integrity Verification:** Compares current state to baseline and reports changes  
- 🧾 **Logging:** Logs all events (modifications, additions, deletions)  
- 🕒 **Automatic Scanning:** Supports scheduled scans at user-defined intervals  
- 💾 **Baseline Storage:** Uses JSON (simple and human-readable)  
- 🧰 **Command-Line Interface:** Simple, scriptable CLI for automation  

---

## 🧠 Use Cases

- Detect unauthorized changes to configuration or system files  
- Monitor web directories for injected scripts or malware  
- Track file tampering for compliance (PCI-DSS, HIPAA, etc.)  
- Integrate into Blue Team labs or SIEM workflows  

---

## ⚙️ Installation

```bash
git clone https://github.com/yordanb00/fim-tool.git
cd fim-tool
pip install -r requirements.txt
````

> Optional dependency:
> `schedule` — for automatic periodic scans
>
> Install manually:
>
> ```bash
> pip install schedule
> ```

---

## 🧩 Usage

### 1️⃣ Create a baseline

Generate initial file hashes for a directory you want to monitor:

```bash
python fim.py -d /path/to/watch --init
```

### 2️⃣ Perform a one-time scan

Compare current hashes against the saved baseline:

```bash
python fim.py -d /path/to/watch --scan
```

### 3️⃣ Enable auto-monitoring

Continuously check integrity every 10 minutes:

```bash
python fim.py -d /path/to/watch --auto 10
```

---

## 📁 Project Structure

```
fim-tool/
│
├── fim.py                # Main FIM script
├── baseline.json         # Baseline hash database
├── logs/
│   └── fim.log           # Log file with alerts and changes
└── README.md
```

---

## 🧰 Example Output

```bash
[*] Integrity Issues Detected:
  ⚠️ Modified: 2 files
  ➕ Added: 1 file
  ❌ Deleted: 1 file
```

Or clean state:

```bash
[+] No integrity issues detected.
```

---

## 🧮 How It Works

| Step | Description                                                    |
| ---- | -------------------------------------------------------------- |
| 1️⃣  | Calculates SHA256 hash of each file                            |
| 2️⃣  | Saves baseline of all files in `baseline.json`                 |
| 3️⃣  | During scan, rehashes current files and compares with baseline |
| 4️⃣  | Logs and displays any modifications, additions, or deletions   |

---

## 🧠 Future Enhancements

* 🧾 SQLite database backend
* 📧 Email / Discord alert integration
* 📊 HTML/PDF reporting
* ⚙️ File whitelist / exclusion filters
* 🔒 Real-time monitoring via watchdog module

---

## 🧑‍💻 Author

**Yordan Borges**
💻 Cybersecurity & Python Developer
🔗 [LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/<yourusername>)

---

## ⚠️ Disclaimer

This tool is designed for **educational and defensive purposes** only.
Do **not** use it to monitor or modify systems without explicit authorization.


