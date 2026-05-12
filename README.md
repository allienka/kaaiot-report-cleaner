# KaaIoT Report Cleaner

Python utility for post-processing KaaIoT-generated Excel reports.

The tool converts numeric values stored as text into proper Excel numeric cells, improving compatibility with formulas, localization, and reporting workflows.

## Features

- Converts Excel text values into numeric cells
- Processes multiple worksheets automatically
- Preserves workbook structure
- Supports reusable command-line input/output paths
- Designed for KaaIoT energy reporting workflows

## Technologies

- Python
- openpyxl
- Node-RED (planned integration)

## Usage

Run the script with:

```bash
python fix_report.py <input_file> <output_file>
```

Example:

```bash
python fix_report.py sample_reports/input.xlsx output/output_fixed.xlsx
```

## Project Status

Current version:
- XLSX numeric conversion working
- Multi-sheet support implemented
- Preparing for Node-RED automation integration