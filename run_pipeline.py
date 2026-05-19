import subprocess
from pathlib import Path

incoming_dir = Path("incoming")

# Check files before email check
before_files = set(incoming_dir.glob("*.xlsx"))

print("Checking emails...")
subprocess.run(["python3", "check_email.py"])

# Check files after email check
after_files = set(incoming_dir.glob("*.xlsx"))

new_files = after_files - before_files

if new_files:
    print("New report found!")

    subprocess.run(["python3", "process_folder.py"])
    subprocess.run(["python3", "send_email.py"])

else:
    print("No new reports.")