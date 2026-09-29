import os

import resend


RESEND_API_KEY = os.environ.get("RESEND_API_KEY")
ALERT_TO_EMAIL = os.environ.get("ALERT_TO_EMAIL")
MAIL_FROM = os.environ.get("MAIL_FROM", "Oceair International <onboarding@resend.dev>")


def mail_is_configured() -> bool:
    return bool(
        RESEND_API_KEY
        and ALERT_TO_EMAIL
        and MAIL_FROM
    )


def send_quote_alert(entry: dict) -> bool:
    """
    Sends an email alert when a new quote enquiry is submitted.

    Returns True if the email was sent successfully.
    Returns False if email configuration is missing or sending fails.
    """

    if not mail_is_configured():
        print(
            "[mailer] Resend email not configured — skipping email alert. "
            "Set RESEND_API_KEY, ALERT_TO_EMAIL and MAIL_FROM."
        )
        return False

    resend.api_key = RESEND_API_KEY

    subject = (
        f"New Product enquiry — "
        f"{entry.get('product', 'Unknown product')} "
        f"({entry.get('name', 'Unknown name')})"
    )

    phone = entry.get("phone", "-")
    product = entry.get("product", "-")
    quantity = entry.get("quantity") or "-"
    message = entry.get("message") or "-"
    submitted_at = entry.get("submitted_at", "-")

    # Plain-text version
    text_body = (
        "New enquiry from the Oceair International website.\n\n"
        f"Name:        {entry.get('name', '-')}\n"
        f"Phone:       {phone}\n"
        f"Product:     {product}\n"
        f"Quantity:    {quantity}\n"
        f"Message:     {message}\n"
        f"Submitted:   {submitted_at}\n\n"
        f"Call or WhatsApp: {phone}\n"
    )

    # HTML version
    html_body = f"""
    <html>
        <body>
            <h2>New Product Enquiry</h2>

            <p>
                A new enquiry was submitted from the
                <strong>Oceair International</strong> website.
            </p>

            <table cellpadding="8" cellspacing="0" border="1">
                <tr>
                    <td><strong>Name</strong></td>
                    <td>{entry.get('name', '-')}</td>
                </tr>

                <tr>
                    <td><strong>Phone</strong></td>
                    <td>{phone}</td>
                </tr>

                <tr>
                    <td><strong>Product</strong></td>
                    <td>{product}</td>
                </tr>

                <tr>
                    <td><strong>Quantity</strong></td>
                    <td>{quantity}</td>
                </tr>

                <tr>
                    <td><strong>Message</strong></td>
                    <td>{message}</td>
                </tr>

                <tr>
                    <td><strong>Submitted</strong></td>
                    <td>{submitted_at}</td>
                </tr>
            </table>

            <p>
                <strong>Call or WhatsApp:</strong> {phone}
            </p>
        </body>
    </html>
    """

    try:
        params = {
            "from": MAIL_FROM,
            "to": [ALERT_TO_EMAIL],
            "subject": subject,
            "text": text_body,
            "html": html_body,
        }

        email = resend.Emails.send(params)

        print(f"[mailer] Quote alert email sent successfully: {email}")

        return True

    except Exception as exc:
        print(f"[mailer] Failed to send quote alert email: {exc}")
        return False
