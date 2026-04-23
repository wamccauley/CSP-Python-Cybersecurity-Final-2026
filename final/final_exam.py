"""
╔══════════════════════════════════════════════════════════════╗
║        CSP Python & Cybersecurity Final Exam - 2026          ║
║                                                              ║
║  Name:  _______________________________________________      ║
║  Date:  _______________________________________________      ║
╚══════════════════════════════════════════════════════════════╝

INSTRUCTIONS:
  - Complete ALL sections below.
  - Replace every  # YOUR CODE HERE  comment with working code.
  - Do NOT delete any existing code, only ADD your code.
  - Run this file to check your output before submitting.
  - Each section has a point value shown in the header.

SCORING:
  Section 1 - Python Basics             [20 pts]
  Section 2 - File I/O                  [20 pts]
  Section 3 - Caesar Cipher             [20 pts]
  Section 4 - Password Checker          [20 pts]
  Section 5 - File System & Log Reader  [20 pts]
  ─────────────────────────────────────────────
  TOTAL                                 [100 pts]
"""

import os

print("=" * 60)
print("  CSP Python & Cybersecurity Final Exam")
print("=" * 60)


# ════════════════════════════════════════════════════════════
# SECTION 1 — Python Basics                         [20 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 1: Python Basics ---")

# ── 1A. Variables [4 pts] ─────────────────────────────────
# Create three variables:
#   student_name  (string)  : your first name
#   student_grade (integer) : your grade level (9, 10, 11, or 12)
#   favorite_topic (string) : "Python" or "Cybersecurity"
# Then print: "Hi, I'm [name], a grade [grade] student who loves [topic]!"

# YOUR CODE HERE


# ── 1B. Grade Calculator [8 pts] ─────────────────────────
# Write a function called letter_grade(score) that takes a
# numeric score (0-100) and returns the letter grade:
#   A = 90-100  |  B = 80-89  |  C = 70-79  |  D = 60-69  |  F = <60

def letter_grade(score):
    # YOUR CODE HERE
    pass

# Test your function (do not change these lines)
test_scores = [100, 88, 73, 61, 45]
for s in test_scores:
    print(f"  Score {s} -> {letter_grade(s)}")


# ── 1C. List Operations [8 pts] ──────────────────────────
# Given this list of cybersecurity threats:
threats = ["phishing", "malware", "ransomware", "spyware", "DDoS"]

# 1. Add "brute force" to the end of the list
# YOUR CODE HERE

# 2. Print the total number of threats
# YOUR CODE HERE

# 3. Print each threat in ALL CAPS using a loop
# YOUR CODE HERE


# ════════════════════════════════════════════════════════════
# SECTION 2 — File I/O                              [20 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 2: File I/O ---")

# ── 2A. Write a File [10 pts] ────────────────────────────
# Create a file called "cyber_glossary.txt" and write the
# following 5 terms and definitions into it, one per line:
#
#   Malware: Software designed to harm a computer or steal data.
#   Phishing: A fake message that tricks you into revealing information.
#   Encryption: Scrambling data so only authorized people can read it.
#   Firewall: A system that monitors and controls network traffic.
#   VPN: A tool that encrypts your internet connection.

# YOUR CODE HERE


# ── 2B. Read and Search the File [10 pts] ────────────────
# Open "cyber_glossary.txt" and:
#   1. Print the total number of lines in the file
#   2. Search for the term "Encryption" and print that line

# YOUR CODE HERE


# ════════════════════════════════════════════════════════════
# SECTION 3 — Caesar Cipher                         [20 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 3: Caesar Cipher ---")

# ── 3A. Encrypt [10 pts] ─────────────────────────────────
# Write a function encrypt_message(text, shift) that:
#   - Shifts each LETTER forward by 'shift' positions in the alphabet
#   - Wraps around (Z + 1 = A)
#   - Leaves spaces, numbers, and punctuation UNCHANGED
#   - Preserves uppercase/lowercase
#
# Example: encrypt_message("Hello!", 4) -> "Lipps!"

def encrypt_message(text, shift):
    # YOUR CODE HERE
    pass


# ── 3B. Decrypt [10 pts] ─────────────────────────────────
# Write a function decrypt_message(text, shift) that reverses
# the encryption. Use your encrypt_message function!
#
# Example: decrypt_message("Lipps!", 4) -> "Hello!"

def decrypt_message(text, shift):
    # YOUR CODE HERE
    pass


# Test your cipher (do not change these lines)
original  = "Cybersecurity Is Fun!"
shift_val = 5
encoded   = encrypt_message(original, shift_val)
decoded   = decrypt_message(encoded, shift_val)
print(f"  Original:  {original}")
print(f"  Encrypted: {encoded}")
print(f"  Decrypted: {decoded}")
print(f"  Match: {original == decoded}")


# ════════════════════════════════════════════════════════════
# SECTION 4 — Password Strength Checker             [20 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 4: Password Strength Checker ---")

# Write a function is_strong_password(password) that checks:
#   ✅ At least 10 characters long                    [4 pts]
#   ✅ Contains at least one uppercase letter          [4 pts]
#   ✅ Contains at least one lowercase letter          [4 pts]
#   ✅ Contains at least one digit (0-9)               [4 pts]
#   ✅ Contains at least one special char: !@#$%^&*    [4 pts]
#
# Return a DICTIONARY with:
#   "strong": True or False
#   "feedback": a list of strings describing what is missing
#               (empty list if the password is strong)
#
# Example:
#   is_strong_password("Hello1")
#   -> {"strong": False,
#       "feedback": ["Too short (need 10+ chars)",
#                    "Missing special character"]}

def is_strong_password(password):
    # YOUR CODE HERE
    pass


# Test passwords (do not change these lines)
test_passwords = [
    "abc",
    "helloworld",
    "Hello123",
    "Secur3!Pass",
    "MyStr0ng!PW",
]

for pw in test_passwords:
    result = is_strong_password(pw)
    status = "STRONG ✅" if result["strong"] else "WEAK ❌"
    print(f"  '{pw}' -> {status}")
    if result["feedback"]:
        for tip in result["feedback"]:
            print(f"      - {tip}")


# ════════════════════════════════════════════════════════════
# SECTION 5 — File System & Log Analysis            [20 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 5: File System & Log Analysis ---")

# ── 5A. Build a Folder Structure [10 pts] ────────────────
# Use os.makedirs() to create this folder structure:
#
#   my_project/
#   ├── src/
#   ├── docs/
#   └── data/
#
# After creating the folders, write a file called
# "project_info.txt" inside my_project/ containing:
#   Project: CSP Final
#   Author: [your name]
#   Date: April 2026

# YOUR CODE HERE


# ── 5B. Log File Analysis [10 pts] ───────────────────────
# A security log is provided below as a list of strings.
# Write code that:
#   1. Counts how many lines contain "SUCCESS"
#   2. Counts how many lines contain "FAILED"
#   3. Prints each FAILED line with a ⚠️  warning prefix
#   4. Prints a summary: "X successful logins, Y failed attempts"

security_log = [
    "2026-04-23 07:00 - SUCCESS: alice logged in from 192.168.1.10",
    "2026-04-23 07:02 - FAILED: unknown user 'hacker' from 10.0.0.99",
    "2026-04-23 07:05 - SUCCESS: bob logged in from 192.168.1.11",
    "2026-04-23 07:07 - FAILED: alice wrong password from 192.168.1.10",
    "2026-04-23 07:09 - FAILED: unknown user 'admin' from 10.0.0.99",
    "2026-04-23 07:10 - SUCCESS: charlie logged in from 192.168.1.12",
    "2026-04-23 07:15 - SUCCESS: alice logged in from 192.168.1.10",
    "2026-04-23 07:18 - FAILED: bob wrong password from 192.168.1.11",
]

# YOUR CODE HERE


# ════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  Final Exam Complete — Review your output above!")
print("=" * 60)
