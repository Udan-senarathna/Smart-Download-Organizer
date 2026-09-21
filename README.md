<div align="center">

# 📁 Smart Download Organizer

**An intelligent, lightweight Python automation tool that cleans up your messy Downloads directory in seconds.**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)](https://github.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

[Key Features](#-key-features) •
[Installation](#-installation) •
[Usage](#-usage) •
[File Mapping](#-supported-file-types) •
[Contributing](#-contributing)

</div>

---

## 📌 Overview

Tired of a cluttered Downloads folder filled with loose PDFs, images, and archives? **Smart Download Organizer** runs locally on your machine to scan, sort, and relocate files into structured, dedicated subdirectories based on their file extensions.

* **Zero external dependencies:** Runs purely on Python's robust standard library (`pathlib`, `shutil`).
* **Safe operations:** Built-in collision prevention ensures your existing files are never accidentally overwritten.

---

## 🚀 Key Features

- ⚡ **Lightning Fast:** Instant execution using native system paths via `pathlib`.
- 🛡️ **Conflict Prevention:** Skips moving a file if a duplicate name already exists in the destination folder.
- 📂 **Smart Catch-All:** Safely moves unmapped or unknown file types into an `Others/` directory.
- 📊 **Execution Metrics:** Displays a detailed console summary of total files processed after every run.
- 🪶 **Zero Overhead:** No heavy frameworks, extra third-party libraries, or background resource draining.

---

## 📂 Supported File Types

| Category | Icon | Target Extensions |
| :--- | :---: | :--- |
| **Images** | 📷 | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg` |
| **Documents** | 📄 | `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.csv` |
| **Archives** | 🗜️ | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| **Videos** | 🎬 | `.mp4`, `.mkv`, `.avi`, `.mov` |
| **Audio** | 🎵 | `.mp3`, `.wav`, `.flac`, `.aac` |
| **Others** | 📁 | *Any extension not listed above* |

---

## 💻 Prerequisites

Ensure you have **Python 3.8 or higher** installed on your system:

```bash
python --version
# or
python3 --version
