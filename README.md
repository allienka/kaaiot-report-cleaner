# KaaIoT Report Cleaner

Python utility for post-processing KaaIoT-generated Excel reports.

The tool converts numeric values stored as text into proper Excel numeric cells, improving compatibility with formulas, localization, and reporting workflows.

---

# Features

* Converts Excel text values into numeric Excel cells
* Processes multiple worksheets automatically
* Preserves workbook structure
* Automatic output file generation
* Command-line interface support
* Logging for converted cells
* Safe workbook loading and error handling
* Designed for KaaIoT energy reporting workflows

---

# Technologies

* Python
* openpyxl
* GitHub
* Linux
* Scaleway VPS (planned deployment)
* Node-RED integration research

---

# Project Structure

```text
kaaiot-report-cleaner/
├── output/
├── sample_reports/
│   └── input.xlsx
├── venv/
├── .gitignore
├── fix_report.py
├── README.md
└── requirements.txt
```

---

# Usage

Run the script with:

```bash
python fix_report.py <input_file>
```

Example:

```bash
python fix_report.py sample_reports/input.xlsx
```

The corrected file will automatically be saved into:

```text
output/
```

Example output:

```text
output/input_fixed.xlsx
```

---

# Example Console Output

```text
Converted B2: 6285.8046875 -> 6285.8046875
Converted C2: 3.14 -> 3.14
Saved corrected file: output/input_fixed.xlsx
```

---

# Current Status

## Completed

* XLSX numeric conversion
* Multi-sheet support
* Automatic output naming
* Error handling
* Conversion logging
* GitHub repository setup
* Node-RED execution tests
* KaaIoT environment investigation

## Research Findings

KaaIoT Node-RED environment currently supports:

* Python 3 execution

But does not currently provide:

* openpyxl package
* pip installation access
* Docker access

Because of this, deployment research is continuing.

---

# Planned Architecture

## Preferred Future Deployment

```text
KaaIoT Reports
        ↓
Scaleway VPS
        ↓
Python Report Cleaner
        ↓
Corrected Excel Reports
```

Potential future features:

* Automatic folder watching
* OneDrive integration
* Email automation
* Scheduled processing
* Docker container deployment

---

# Scaleway VPS Deployment

## Current VPS Deployment

* Ubuntu Linux VPS
* Scaleway
* Python 3
* openpyxl
* GitHub repository clone
* Cron/background automation

Estimated infrastructure cost:

* ~10 €/month

# VPS Deployment

Clone repository:

```bash
git clone https://github.com/allienka/kaaiot-report-cleaner.git
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Run script:

```bash
python3 fix_report.py sample_reports/input.xlsx

```

# Learning Goals

This project is also used to practice:

* Python automation
* Excel processing
* Git and GitHub workflows
* Linux server basics
* Cloud deployment concepts
* Backend automation architecture
* Node-RED integration

---

# GitHub Repository

Repository:

```text
https://github.com/allienka/kaaiot-report-cleaner
```

---

# Author

Alena Hakkarainen
