"""
Oceair International Private Limited — website backend.

A small Flask app that:
- renders the site from Jinja2 templates (templates/index.html)
- serves product data from Python (data/products.py) instead of hardcoding
  it into the HTML
- accepts the "Request a Quote" form, validates it, and saves each
  enquiry to data/enquiries.json so you have a record of every lead
  that comes through the site
"""

from datetime import datetime, timezone
from pathlib import Path
import json
# import os

import dotenv
    
dotenv.load_dotenv()  # reads a local .env file if present; on Render, env vars are set in the dashboard instead

from flask import Flask, render_template, request, redirect, url_for, flash

from data.products import PRODUCT_CATEGORIES, COMPANY, STATS, PROCESS_STEPS, FAQS
from mailer import send_quote_alert

app = Flask(__name__)
app.secret_key = dotenv.get_key(".env", "FLASK_KEY")  # used only to sign the flash-message cookie

ENQUIRIES_FILE = Path(__file__).parent / "data" / "enquiries.json"


def load_enquiries():
    if ENQUIRIES_FILE.exists():
        with open(ENQUIRIES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_enquiry(entry: dict):
    enquiries = load_enquiries()
    enquiries.append(entry)
    with open(ENQUIRIES_FILE, "w", encoding="utf-8") as f:
        json.dump(enquiries, f, indent=2, ensure_ascii=False)


@app.route("/")
def home():
    return render_template(
        "index.html",
        company=COMPANY,
        stats=STATS,
        categories=PRODUCT_CATEGORIES,
        steps=PROCESS_STEPS,
        faqs=FAQS,
    )


@app.route("/quote", methods=["POST"])
def request_quote():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    product = request.form.get("product", "").strip()
    quantity = request.form.get("quantity", "").strip()
    message = request.form.get("message", "").strip()

    # Basic server-side validation — never trust the browser alone.
    errors = []
    if not name:
        errors.append("Please enter your name.")
    if not phone or len(phone) < 7:
        errors.append("Please enter a valid phone number.")
    if not product:
        errors.append("Please select a product.")

    if errors:
        for e in errors:
            flash(e, "error")
        return redirect(url_for("home") + "#contact")

    entry = {
        "name": name,
        "phone": phone,
        "product": product,
        "quantity": quantity,
        "message": message,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    }
    save_enquiry(entry)
    send_quote_alert(entry)  # emails the alert; silently skips/logs if SMTP isn't configured

    flash(
        "Thanks, {}! Your enquiry for {} has been received — "
        "we'll call or WhatsApp you shortly.".format(name, product),
        "success",
    )
    return redirect(url_for("home") + "#contact")


if __name__ == "__main__":
    # debug=True is for local development only — turn it off in production.
    app.run(debug=True, port=5000)
