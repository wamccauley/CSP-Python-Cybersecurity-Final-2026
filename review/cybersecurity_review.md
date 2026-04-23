# 🔐 Cybersecurity Review Sheet

Use this guide to review foundational cybersecurity concepts before your final.

---

## 1. What Is Cybersecurity?

Cybersecurity is the practice of **protecting computers, networks, and data** from unauthorized access, damage, or attack.

Three core goals — called the **CIA Triad**:

| Goal              | Meaning                                      | Example                          |
|-------------------|----------------------------------------------|----------------------------------|
| **Confidentiality** | Only authorized people can see data         | Passwords, encryption            |
| **Integrity**       | Data is accurate and hasn't been tampered with | File checksums, digital signatures |
| **Availability**    | Systems and data are accessible when needed | Backups, uptime monitoring       |

---

## 2. Common Cyber Threats

| Threat              | Description                                               |
|---------------------|-----------------------------------------------------------|
| **Malware**         | Malicious software (viruses, ransomware, spyware)         |
| **Phishing**        | Fake emails/websites tricking you into giving info        |
| **Social Engineering** | Manipulating people (not machines) to get access      |
| **Brute Force**     | Trying every possible password until one works            |
| **Man-in-the-Middle** | Attacker secretly intercepts communication              |
| **SQL Injection**   | Injecting malicious code into a database query            |
| **DoS/DDoS**        | Flooding a server to make it unavailable                  |

---

## 3. Passwords & Authentication

**Strong password rules:**
- At least **12 characters** long
- Mix of **uppercase, lowercase, numbers, symbols**
- No dictionary words or personal info
- Unique for every account

**Authentication types:**
- **Something you know** → Password, PIN
- **Something you have** → Phone, security key
- **Something you are** → Fingerprint, face scan

**Multi-Factor Authentication (MFA):** Using 2+ of the above types together — much more secure!

---

## 4. Encryption Basics

Encryption **scrambles** data so only authorized parties can read it.

### Caesar Cipher (Simple Example)
Shift every letter by a fixed number.

```
Plaintext:  HELLO
Shift: 3
Ciphertext: KHOOR
```

- **H** → shift 3 → **K**
- **E** → shift 3 → **H**
- **L** → shift 3 → **O**
- **O** → shift 3 → **R**

**Symmetric encryption:** Same key encrypts and decrypts (e.g., Caesar cipher).
**Asymmetric encryption:** Public key encrypts, private key decrypts (e.g., HTTPS).

---

## 5. File Permissions

Every file on a computer has **permissions** controlling who can do what.

### Linux/Mac permission format: `rwxrwxrwx`

```
-rw-r--r--
```

| Position   | Who          | r = Read | w = Write | x = Execute |
|------------|--------------|----------|-----------|-------------|
| 1st group  | Owner        | ✅       | ✅        | ❌          |
| 2nd group  | Group        | ✅       | ❌        | ❌          |
| 3rd group  | Everyone     | ✅       | ❌        | ❌          |

### Windows permissions (simplified)
- **Read** — Can open/view the file
- **Write** — Can modify the file
- **Execute** — Can run the file as a program
- **Full Control** — Can do everything including delete/change permissions

---

## 6. Safe Online Habits

- ✅ Use strong, unique passwords + a password manager
- ✅ Enable MFA on all important accounts
- ✅ Keep software and OS updated (patches fix vulnerabilities)
- ✅ Only click links/attachments you are expecting
- ✅ Use HTTPS websites (padlock in browser)
- ❌ Never share passwords
- ❌ Never use public Wi-Fi for sensitive tasks without a VPN
- ❌ Never plug in unknown USB drives

---

## 7. Key Vocabulary

| Term              | Definition                                                      |
|-------------------|-----------------------------------------------------------------|
| **Vulnerability** | A weakness in a system that can be exploited                    |
| **Exploit**       | Code or technique that takes advantage of a vulnerability       |
| **Patch**         | Software update that fixes a vulnerability                      |
| **Firewall**      | A barrier that controls incoming/outgoing network traffic       |
| **VPN**           | Encrypts your internet connection and hides your IP address     |
| **Hash**          | A one-way function that converts data to a fixed-length string  |
| **Checksum**      | A value used to verify file integrity                           |
| **Zero-day**      | An unknown vulnerability with no available patch yet           |
