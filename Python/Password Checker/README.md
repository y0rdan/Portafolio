---

# 🔒 Password Strength Checker

## 📘 Overview

This Python script evaluates the **strength and complexity** of user passwords.
It checks for:

* Uppercase letters
* Lowercase letters
* Numbers
* Symbols
* Length (8+ characters)

It also compares the password against a list of **weak or commonly used passwords**, and provides **recommendations** to improve password security.

---

## ⚙️ Features

✅ Loads a custom list of weak passwords (`weak_pass.txt`)
✅ Uses **color-coded** terminal output via `colorama`
✅ Evaluates multiple password criteria (length, symbols, etc.)
✅ Provides recommendations for improvement
✅ Interactive CLI — allows repeated checks without restarting

---

## 🧩 Requirements

Install dependencies using pip:

```bash
pip install colorama
```

---

## 📂 File Structure

```
password_checker/
│
├── password_checker.py       # Main script
├── weak_pass.txt             # List of weak/common passwords
└── README.md                 # Documentation
```

> ⚠️ The `weak_pass.txt` file must be in the same directory as the script.

Example `weak_pass.txt`:

```
password
123456
qwerty
admin
letmein
```

---

## 🚀 Usage

Run the script:

```bash
python3 password_checker.py
```

Example interaction:

```
Password Checker
Would you like to check your password? (y/n)
>>> y

WELCOME TO THE PASSWORD CHECKER APP.
Please enter your password:
>>> StrongP@ss123

[!] Checking Password Complexity and Length...
[!] PRINTING RESULTS.....

[!] SECURE [!]
Your password is Secure. Congratulations.
Your Password Score is 5
No recommendations. Great Work!
```

---

## 🧠 How It Works

| Check Type       | Description                            | Score |
| ---------------- | -------------------------------------- | ----- |
| Lowercase letter | Contains at least one `a-z`            | +1    |
| Uppercase letter | Contains at least one `A-Z`            | +1    |
| Number           | Contains at least one `0-9`            | +1    |
| Symbol           | Contains at least one `!@#$%^&*()_+~/` | +1    |
| Length           | Minimum of 8 characters                | +1    |

**Maximum Score:** 5
**Strength Levels:**

* 0–1 → 🔴 Weak
* 2–3 → 🟡 Moderate
* 4–5 → 🟢 Secure

---

## 💬 Example Recommendations

If your password is `hello123`:

```
[!] MODERATE [!]
Please add a capital letter to your Password.
Please add a Symbol to your Password.
```

---

## 🧱 Error Handling

* Displays an error if `weak_pass.txt` is missing
* Ignores empty lines in the weak password list
* Gracefully exits when user chooses not to continue

---

## 🧑‍💻 Author

**Yordan Borges**
Coding Portfolio Project
---

---
