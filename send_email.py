import resend
import base64

from pathlib import Path
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# Resend API key
resend.api_key = getenv("RESEND_API_KEY")

# Recipient email
RECIPIENT = "alena.rebova@gmail.com"

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

clean_name = latest_file.name
clean_name = clean_name.replace("_fixed", "")

# Remove timestamp
parts = clean_name.rsplit("_", 2)

if len(parts) == 3:
    clean_name = parts[0] + ".xlsx"

print(f"Sending file: {clean_name}")

# Read and encode file
with open(latest_file, "rb") as f:
    file_content = base64.b64encode(
        f.read()
    ).decode("utf-8")

# Send email
resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": [RECIPIENT],
    "subject": "Monthly KaaIoT Report",
    "html": """
    <p>Hei,</p>

    <p>Liitteenä KaaIoT-järjestelmästä muodostettu kuukausittainen energiaraportti.</p>

    <p>
    Ystävällisin terveisin,<br>
    Etec Automation Oy      
    </p>
    """,
    "attachments": [
        {
            "filename": clean_name,
            "content": file_content
        }
    ]
})

print("Email sent successfully!")