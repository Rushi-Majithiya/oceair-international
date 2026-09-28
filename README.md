# Oceair International — website (Flask backend + HTML templates)

A website for Oceair International Private Limited:
- **Backend**: Python (Flask) — `app.py`, with content data in `data/products.py`
- **Frontend**: HTML templates (`templates/index.html`, using Jinja2) and
  separate CSS/JS (`static/css/style.css`, `static/js/script.js`) — no HTML
  is hardcoded in Python, and no content is hardcoded in the HTML.
- **Design**: logo mark, hero illustration, trust badges, product icons, a
  "how it works" section, an FAQ accordion, scroll-reveal animation, and a
  floating WhatsApp button.
- A working **"Request a Quote" form** that posts to the Flask backend,
  which validates it, saves every enquiry to `data/enquiries.json`, **and
  emails you an alert via Gmail SMTP** (`mailer.py`).

```
oceair-flask/
├── app.py                  ← Flask routes + form handling
├── mailer.py                ← Gmail SMTP email-alert logic
├── requirements.txt
├── Procfile                ← tells a host how to start the app
├── .env.example             ← template for your Gmail credentials
├── data/
│   ├── products.py         ← company + product content, edit prices/text here
│   └── enquiries.json      ← form submissions land here (auto-created)
├── templates/
│   └── index.html          ← Jinja2 template, no hardcoded content
└── static/
    ├── css/style.css
    └── js/script.js
```

## 1. Run it locally

You need Python 3.9+ (you already have this).

```bash
cd oceair-flask
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python3 app.py
```

Open **http://127.0.0.1:5000** in your browser. Fill in the quote form at the
bottom of the Contact section — it'll save to `data/enquiries.json`, which
you can open any time to see every lead that's come in.

## 2. Set up Gmail email alerts (optional but recommended)

Every time someone submits the quote form, the site can email you instantly.
It uses Gmail's SMTP server with an **App Password** (a 16-character code —
not your real Gmail password, which Google no longer allows apps to use
directly).

**Generate an App Password:**
1. Your Gmail account needs 2-Step Verification turned on first: go to
   https://myaccount.google.com/security → **2-Step Verification** → turn it on.
2. Then go to https://myaccount.google.com/apppasswords
3. Enter a name like "Oceair Website" → **Create**.
4. Google shows you a 16-character password (e.g. `abcd efgh ijkl mnop`) —
   copy it. You won't be able to see it again, but you can always generate a
   new one.

**Configure it locally:**
```bash
cp .env.example .env
```
Then open `.env` and fill in:
```
GMAIL_ADDRESS=youraddress@gmail.com
GMAIL_APP_PASSWORD=abcdefghijklmnop      # no spaces, the 16 characters from Google
ALERT_TO_EMAIL=youraddress@gmail.com     # where you want alerts to land
FLASK_SECRET_KEY=<a random string — see "Before deploying to production" below>
```
`.env` is already in `.gitignore`, so this password never gets committed or
pushed to GitHub. Restart `python3 app.py` and submit a test enquiry through
the form — you should get an email within a few seconds. If it doesn't
arrive, check the terminal running `app.py`: `mailer.py` prints the reason
(bad password, 2-Step Verification not enabled, etc.) rather than crashing
the site.

**Configure it on Render (for the live site):** in your Render service →
**Environment** tab → add the same four variables (`GMAIL_ADDRESS`,
`GMAIL_APP_PASSWORD`, `ALERT_TO_EMAIL`, `FLASK_SECRET_KEY`) as environment
variables, then save — Render redeploys automatically with them available.

If you skip this step entirely, the site still works fine — enquiries just
won't trigger an email, only the `data/enquiries.json` record.

## 3. Put the code on GitHub (source control / backup)

1. Create a GitHub account at github.com/join (skip if you have one).
2. New repository → name it e.g. `oceair-website` → Public → Create.
3. From this folder:
```bash
git init
git add .
git commit -m "Oceair International site — Flask backend + templates"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/oceair-website.git
git push -u origin main
```
`.gitignore` is already set up to skip `__pycache__`, virtual environments,
and the local `enquiries.json` (so old test leads don't get committed).

**Note:** GitHub itself (and GitHub Pages) only serves static files — it
cannot run your Flask backend. GitHub here is your code repository. For the
site to actually be live and running Python, deploy it with the next step.

## 4. Deploy it live (Render — free tier, Python-friendly)

1. Go to https://render.com and sign up (you can sign up directly with your
   GitHub account, which makes step 2 easier).
2. Click **New → Web Service**.
3. Connect your GitHub account and select the `oceair-website` repo.
4. Render will detect Python. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app` (already in the `Procfile`, Render
     usually picks it up automatically)
5. Choose the **Free** instance type → **Create Web Service**.
6. Wait for the build to finish — Render gives you a live URL like
   `https://oceair-website.onrender.com`.

Every time you `git push` to `main`, Render automatically rebuilds and
redeploys the site.

**Free-tier note:** Render's free web services sleep after periods of no
traffic and take ~30–50 seconds to wake up on the next visit. If that's a
problem for a business site, Render's cheapest paid tier (or alternatives
like PythonAnywhere or Railway) removes the sleep delay.

### Before deploying to production
- Set `FLASK_SECRET_KEY` as a real random string (see step 2 above) rather
  than relying on the placeholder default in `app.py`. Generate one with:
  ```bash
  python3 -c "import secrets; print(secrets.token_hex(32))"
  ```
- Turn off debug mode: in `app.py`, change `app.run(debug=True, ...)` to
  `debug=False` (Render running via `gunicorn` already ignores this, but
  it matters if you ever run `python3 app.py` on a public server directly).

## 5. Editing content later

- **Text, prices, phone number, FAQ, process steps**: edit `data/products.py`
  — plain Python dictionaries/lists, no HTML involved.
- **Page structure/layout, icons**: edit `templates/index.html` (product
  icons are inline SVGs chosen per category by the `icon` key in
  `data/products.py`).
- **Colors, spacing, fonts, animations**: edit `static/css/style.css`.
- **Enquiries**: open `data/enquiries.json` any time to see submitted leads,
  or check your inbox if Gmail alerts are configured (step 2).

Push changes with `git add . && git commit -m "update" && git push` and
Render redeploys automatically.

## 6. Logo, address and contact details

The real logo (cut from the company flyer) is in `static/img/logo.png`, with a
square copy at `static/img/favicon.png` for the browser tab. To replace it,
just overwrite those files with new PNGs of the same name.

The full address, both phone numbers, email and GST IN live in the `COMPANY`
dictionary in `data/products.py` and update everywhere on the site
automatically. The main phone number there is also used for the WhatsApp
button and the Call buttons.
