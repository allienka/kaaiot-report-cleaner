from openpyxl import load_workbook
from pathlib import Path

# File paths
input_file = Path("sample_reports/input.xlsx")
output_file = Path("output/output_fixed.xlsx")

# Load workbook
wb = load_workbook(input_file)

# Loop through all sheets
for ws in wb.worksheets:

    # Loop through all rows and cells
    for row in ws.iter_rows():
        for cell in row:

            # Process only text cells
            if isinstance(cell.value, str):

                value = cell.value.strip()

                try:
                    # Convert decimal numbers
                    if "." in value:
                        number = float(value)

                    # Convert integers
                    else:
                        number = int(value)

                    # Replace text with real number
                    cell.value = number

                except:
                    # Ignore non-numeric text
                    pass

# Save corrected workbook
wb.save(output_file)

print(f"Saved corrected file: {output_file}")