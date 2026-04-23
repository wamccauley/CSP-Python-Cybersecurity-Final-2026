# 📂 File Systems & Structures Review Sheet

---

## 1. What Is a File System?

A **file system** is how an operating system **organizes, stores, and retrieves files** on a storage device (hard drive, SSD, USB).

Common file systems:
| File System | Used By          | Notes                          |
|-------------|------------------|--------------------------------|
| **NTFS**    | Windows          | Supports permissions, large files |
| **FAT32**   | USB drives, old  | Works everywhere, 4GB file limit |
| **ext4**    | Linux            | Fast, reliable                 |
| **APFS**    | macOS            | Optimized for SSDs             |

---

## 2. Directory Structure

Files are organized in a **tree structure** of folders (directories).

```
/  (root — the very top)
├── home/
│   └── alice/
│       ├── Documents/
│       │   └── essay.txt
│       ├── Downloads/
│       └── Pictures/
├── etc/        (system config files)
├── bin/        (executable programs)
└── tmp/        (temporary files)
```

- `/` = root directory (Linux/Mac)
- `C:\` = root directory (Windows)
- Every file has a **path** showing where it lives

### Absolute vs. Relative Paths

| Type         | Example                          | Meaning                                 |
|--------------|----------------------------------|-----------------------------------------|
| **Absolute** | `/home/alice/Documents/essay.txt` | Full path from root                    |
| **Relative** | `Documents/essay.txt`            | Path from your current location         |
| `.`          | `./notes.txt`                    | Current directory                       |
| `..`         | `../Downloads/`                  | One folder up (parent directory)        |

---

## 3. File Extensions & Types

A **file extension** tells the OS (and users) what kind of data is inside a file.

| Extension  | Type              | Opens With              |
|------------|-------------------|-------------------------|
| `.txt`     | Plain text        | Notepad, any editor     |
| `.py`      | Python script     | Python interpreter      |
| `.html`    | Web page          | Browser                 |
| `.pdf`     | Document          | PDF reader              |
| `.jpg/.png`| Image             | Image viewer            |
| `.mp3`     | Audio             | Media player            |
| `.zip`     | Compressed archive| Archive tool            |
| `.exe`     | Windows program   | Windows OS              |
| `.sh`      | Shell script      | Terminal (Linux/Mac)    |
| `.csv`     | Spreadsheet data  | Spreadsheet app, Python |

> ⚠️ **Security note:** Attackers sometimes rename malicious files with safe-looking extensions (e.g., `invoice.pdf.exe`). Always check the true file type!

---

## 4. How Files Are Stored

1. **Bits and Bytes** — All files are stored as binary (0s and 1s). 8 bits = 1 byte.
2. **File metadata** — Info *about* the file stored separately:
   - File name
   - Size
   - Creation/modification date
   - Permissions (who can read/write/execute)
   - File type
3. **File contents** — The actual data stored in the file.

### File Size Units
| Unit      | Size              |
|-----------|-------------------|
| Byte (B)  | 8 bits            |
| Kilobyte (KB) | 1,024 bytes   |
| Megabyte (MB) | 1,024 KB      |
| Gigabyte (GB) | 1,024 MB      |
| Terabyte (TB) | 1,024 GB      |

---

## 5. Working with Files in Python

```python
import os

# Get current directory
print(os.getcwd())

# List files in a directory
print(os.listdir("."))

# Check if a file exists
if os.path.exists("notes.txt"):
    print("File found!")

# Get file size in bytes
size = os.path.getsize("notes.txt")
print(f"Size: {size} bytes")

# Join paths safely (works on all OS)
path = os.path.join("home", "alice", "notes.txt")
print(path)  # home/alice/notes.txt
```

---

## 6. Key Concepts to Remember

- **Root directory** = top of the entire file tree
- **Working directory** = where you currently are
- **Absolute path** = full address from root
- **Relative path** = address from current location
- **File extension** = hint about file type (but can be changed)
- **File metadata** = info about the file, not the file's contents
- **File permissions** = control who can read, write, or execute a file
