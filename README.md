# 🔐 Password Strength Checker & Multi Strong Password Generator

A Python-based CLI tool that:
- ✅ Checks the strength of any given password.
- ✅ Gives **tips** to improve weak or moderate passwords.
- ✅ Generates **5–10 random strong passwords** of a length you choose.

---

## 📌 Features
- **Password Strength Check**:
  - Detects weak, moderate, and strong passwords.
  - Gives suggestions to improve password strength.
- **Random Strong Password Generator**:
  - Generates between 5–10 strong passwords each time.
  - Lets you specify the desired password length (minimum 8 characters).
- **Strong Password Criteria**:
  - At least 8 characters.
  - Contains uppercase & lowercase letters.
  - Contains at least one digit (0–9).
  - Contains at least one special character (`@ $ ! % * ? & . _ -`).

---

## 🚀 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/password-checker-generator.git
   cd password-checker-generator
   ```

2. **Run the Script**
   ```bash
   python3 password_tool.py
   ```

---

## 💻 Usage

1. **Check Password Strength**
   - Enter your password when prompted.
   - The program will rate it as **Weak**, **Moderate**, or **Strong**.
   - Weak or moderate passwords will receive improvement tips.

2. **Generate Random Strong Passwords**
   - After checking, the program will ask if you want strong password suggestions.
   - Enter `yes` to generate between 5–10 **secure random passwords**.
   - You will be asked for the desired password length (minimum 8).

---

## 📸 Example Output
```
Password Strength Checker & Multi Strong Password Generator

Enter your password to check: pass123
Strength: Weak
Tips to improve your password:
-> Use at least 8 characters.
-> Add at least one uppercase letter (A–Z).
-> Include a special character (@ $ ! % * ? & . _ -)

Do you want me to generate strong password suggestions for you? (yes/no): yes
Enter desired password length (minimum 8): 12

Here are 6 randomly generated strong passwords (12 characters each):
1. p@8LzN3WqT4y
2. H7pR@5nM2LkQ
3. xP@1qT9wL4kE
4. Zq2@M7nV8hLw
5. P@3Lk6mQ8tZv
6. N1@pR5tL7wHq
```

---

## 📦 Requirements
- Python 3.x  
- No external libraries required — works with **Python standard library** only.

---

## ⚠️ Disclaimer
This tool is for **personal security awareness and educational purposes only**.  
Do **NOT** store or log real passwords. Always use unique, secure passwords for each account.

---

## 📜 License
This project is licensed under the MIT License.
