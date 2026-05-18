import imaplib
import email
import re
import requests

from pathlib import Path
from dotenv import load_dotenv
from os import getenv
from urllib.parse import unquote

load_dotenv()

EMAIL_USER = getenv("GMAIL_USER")
EMAIL_PASS = getenv("GMAIL_APP_PASSWORD")

incoming_dir = Path("incoming")
incoming_dir.mkdir(exist_ok=True)

mail = imaplib.IMAP4_SSL("imap.gmail.com")

mail.login(EMAIL_USER, EMAIL_PASS)

print("Login successful!")

mail.select("inbox")

status, messages = mail.search(None, "UNSEEN")

email_ids = messages[0].split()

print(f"Total emails: {len(email_ids)}")

if email_ids:

    latest_email_id = email_ids[-1]

    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

    raw_email = msg_data[0][1]

    msg = email.message_from_bytes(raw_email)

    subject = msg["subject"]

    print("Latest subject:", subject)

    if "KaaIoT Monthly Energy Report" not in subject:
        print("Email subject does not match.")
        mail.logout()
        exit()

    # Read email body
    body = ""

    for part in msg.walk():

        content_type = part.get_content_type()

        if content_type == "text/html":

            body = part.get_payload(decode=True).decode()

    # Find download link
    match = re.search(r'https://[^\s"]+\.xlsx[^\s"]*', body)

    if not match:
        print("No XLSX download link found.")
        mail.logout()
        exit()

    download_url = match.group(0)

    print("Download URL found:")
    print(download_url)

    # Extract filename
    filename = unquote(
        download_url.split("/")[-1].split("?")[0]
    )

    filepath = incoming_dir / filename

    # Skip if file already exists
    if filepath.exists():
        print(f"File already exists: {filepath}")

    else:

        response = requests.get(download_url)

        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"Downloaded report: {filepath}")

    # Mark email as read
    mail.store(latest_email_id, '+FLAGS', '\\Seen')

mail.logout()