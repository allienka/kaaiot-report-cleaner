import smtplib

from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv
from os import getenv

load_dotenv()

EMAIL_USER = getenv("GMAIL_USER")
EMAIL_PASS = getenv("GMAIL_APP_PASSWORD")

# Recipient email
RECIPIENT = "alena.hakkarainen@gmail.com"
#RECIPIENT = getenv("REPORT_RECIPIENT")

output_dir = Path("output")

# Find newest XLSX file
xlsx_files = list(output_dir.glob("*.xlsx"))

if not xlsx_files:
    print("No XLSX files found.")
    exit()

latest_file = max(
    xlsx_files,
    key=lambda f: f.stat().st_mtime
)

print(f"Sending file: {latest_file.name}")

# Create email
msg = EmailMessage()

msg["Subject"] = "Processed KaaIoT Report"
msg["From"] = EMAIL_USER
msg["To"] = RECIPIENT

msg.set_content(
    "Attached is the processed KaaIoT report."
)

# Attach file
with open(latest_file, "rb") as f:

    file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=latest_file.name
    )

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

    smtp.login(EMAIL_USER, EMAIL_PASS)

    smtp.send_message(msg)

print("Email sent successfully!")