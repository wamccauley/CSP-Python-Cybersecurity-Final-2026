"""
====================================================
  Cybersecurity Practice Exercises
  CSP Python & Cybersecurity - 2026
====================================================
Practice applying Python to cybersecurity concepts.
Run this file when done to see your results.
"""

import os

# ============================================================
# EXERCISE 1: Password Strength Checker
# ============================================================
# A strong password must:
#   - Be at least 8 characters long
#   - Contain at least one uppercase letter
#   - Contain at least one number
#   - Contain at least one special character: !@#$%^&*
#
# Return "Strong" if all conditions are met, otherwise
# return "Weak" with a hint about what is missing.

def check_password(password):
    has_upper   = any(c.isupper() for c in password)
    has_digit   = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)
    long_enough = len(password) >= 8

    if not long_enough:
        return "Weak - needs at least 8 characters"
    if not has_upper:
        return "Weak - needs an uppercase letter"
    if not has_digit:
        return "Weak - needs a number"
    if not has_special:
        return "Weak - needs a special character (!@#$%^&*)"
    return "Strong"

print("=== Password Strength Checker ===")
passwords = ["hello", "Hello123", "Hello123!", "abc", "MyP@ss99"]
for p in passwords:
    print(f"  '{p}' -> {check_password(p)}")


# ============================================================
# EXERCISE 2: Caesar Cipher
# ============================================================
# The Caesar cipher shifts each letter in a message by a
# fixed number. Non-letters stay the same.
#
# encrypt_caesar("HELLO", 3) -> "KHOOR"
# decrypt_caesar("KHOOR", 3) -> "HELLO"

def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)

print("\n=== Caesar Cipher ===")
message = "Hello, World!"
shift   = 3
encrypted = encrypt_caesar(message, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(f"  Original:  {message}")
print(f"  Encrypted: {encrypted}")
print(f"  Decrypted: {decrypted}")


# ============================================================
# EXERCISE 3: File System Explorer
# ============================================================
# Use the os module to explore the current directory.
# Print:
#   1. The current working directory
#   2. A list of all files and folders here
#   3. For each item, whether it is a FILE or FOLDER

print("\n=== File System Explorer ===")
cwd = os.getcwd()
print(f"  Current directory: {cwd}")
print("  Contents:")

try:
    for item in os.listdir("."):
        kind = "FILE  " if os.path.isfile(item) else "FOLDER"
        print(f"    [{kind}] {item}")
except Exception as e:
    print(f"  Error reading directory: {e}")


# ============================================================
# EXERCISE 4: Log File Analyzer
# ============================================================
# Security analysts read log files to spot suspicious activity.
# This exercise simulates reading a log and flagging
# lines that contain the word "FAILED" or "ERROR".

log_entries = [
    "2026-04-01 08:00 - User alice logged in successfully.",
    "2026-04-01 08:05 - FAILED login attempt for user bob.",
    "2026-04-01 08:10 - User alice accessed /home/alice.",
    "2026-04-01 08:15 - ERROR: Permission denied for user charlie.",
    "2026-04-01 08:20 - FAILED login attempt for user bob.",
    "2026-04-01 08:25 - System backup completed successfully.",
    "2026-04-01 08:30 - ERROR: Unknown user attempted access.",
]

print("\n=== Log File Analyzer ===")
print("Suspicious entries found:")
count = 0
for entry in log_entries:
    if "FAILED" in entry or "ERROR" in entry:
        print(f"  ⚠️  {entry}")
        count += 1
print(f"Total suspicious entries: {count}")


# ============================================================
# EXERCISE 5: Create a Secure Folder Structure
# ============================================================
# Use os.makedirs() to create a sample secure folder layout:
#
#   secure_vault/
#   ├── public/
#   ├── private/
#   └── logs/
#
# Then write a README inside each folder explaining its purpose.

print("\n=== Creating Secure Folder Structure ===")

folders = {
    "secure_vault/public":  "Public folder: files here can be shared with anyone.\n",
    "secure_vault/private": "Private folder: files here are confidential. Authorized users only.\n",
    "secure_vault/logs":    "Logs folder: activity logs for auditing and security monitoring.\n",
}

for folder, description in folders.items():
    os.makedirs(folder, exist_ok=True)
    readme_path = os.path.join(folder, "README.txt")
    with open(readme_path, "w") as f:
        f.write(description)
    print(f"  Created: {folder}/README.txt")

print("\nFolder structure created! Explore 'secure_vault/' to see it.")
print("\nCybersecurity practice complete!")
