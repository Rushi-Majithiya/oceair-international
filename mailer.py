"""
Sends an email alert (via Gmail SMTP) every time a client submits the
"Request a Quote" form.

Configuration comes entirely from environment variables — no credentials
are ever hardcoded here. See .env.example for what to set, and the README
for how to generate a Gmail App Password.

If the environment variables aren't set (e.g. while developing locally
without email configured), sending is silently skipped and a note is
printed to the console — the enquiry still gets saved either way, so a
missing/broken email setup never blocks a real customer's submission.
"""

import os
import smtplib
import socket
from email.message import EmailMessage

GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")
ALERT_TO_EMAIL = os.environ.get("ALERT_TO_EMAIL", GMAIL_ADDRESS)

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


def mail_is_configured() -> bool:
    return bool(GMAIL_ADDRESS and GMAIL_APP_PASSWORD and ALERT_TO_EMAIL)

def _connect_ipv4_smtp(host: str, port: int, timeout: float = 10.0) -> smtplib.SMTP:
    """Connect to SMTP forcing IPv4 to prevent [Errno 101] Network is unreachable on Render."""
    res = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
    if not res:
        raise OSError(f"Could not resolve IPv4 address for {host}")

    af, socktype, proto, canonname, sa = res[0]
    sock = socket.socket(af, socktype, proto)
    sock.settimeout(timeout)
    sock.connect(sa)

    smtp = smtplib.SMTP(timeout=timeout)
    smtp.connect(host, port, sock=sock)
    return smtp

def send_quote_alert(entry: dict) -> bool:
    """
    Emails ALERT_TO_EMAIL with the details of a new quote enquiry.
    Returns True if the email was sent, False if it was skipped or failed
    (failures are logged to the console, never raised — a broken mail
    setup should never break the form for the visitor).
    """
    if not mail_is_configured():
        print("[mailer] Gmail SMTP not configured — skipping email alert. "
              "Set GMAIL_ADDRESS / GMAIL_APP_PASSWORD / ALERT_TO_EMAIL to enable it.")
        return False

    msg = EmailMessage()
    msg["Subject"] = f"New Product enquiry — {entry['product']} ({entry['name']})"
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = ALERT_TO_EMAIL
    msg["Reply-To"] = entry.get("phone", GMAIL_ADDRESS)

    body = (
        "New enquiry from the Oceair International website:\n\n"
        f"Name:        {entry['name']}\n"
        f"Phone:       {entry['phone']}\n"
        f"Product:     {entry['product']}\n"
        f"Quantity:    {entry.get('quantity') or '-'}\n"
        f"Message:     {entry.get('message') or '-'}\n"
        f"Submitted:   {entry['submitted_at']}\n\n"
        f"Call or WhatsApp: {entry['phone']}\n"
    )
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as server:
            server.starttls()
            server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as exc:  # noqa: BLE001 — we want to swallow *any* mail failure
        print(f"[mailer] Failed to send quote alert email: {exc}")
        return False
