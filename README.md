# Oceair International — Website

A single-page website for Oceair International Private Limited, built from the
company's IndiaMART listing (https://m.indiamart.com/oceair-international/).

It's one self-contained file: `index.html`. No build tools, no Node, no Python
needed to run it — just open it in a browser, or host it for free with GitHub
Pages (steps below).

## Preview it locally
Just double-click `index.html`, or run a tiny local server from this folder:

```bash
python3 -m http.server 8000
```
Then open http://localhost:8000 in your browser.

## Host it for free on GitHub Pages — step by step

### 1. Create a GitHub account (skip if you have one)
Go to https://github.com/join and sign up.

### 2. Create a new repository
1. Click the **+** icon top-right → **New repository**.
2. Name it something like `oceair-website` (this name will appear in your URL,
   e.g. `yourusername.github.io/oceair-website`).
3. Set it to **Public**.
4. Leave "Add a README" unchecked (you already have one).
5. Click **Create repository**.

### 3. Upload the website files
Easiest way — no command line needed:
1. On your new repo's page, click **Add file → Upload files**.
2. Drag in `index.html` and `README.md` from this folder.
3. Scroll down, click **Commit changes**.

Or, if you'd rather use git from a terminal (you already have Python, so you
likely have git too):
```bash
cd path/to/this/folder
git init
git add index.html README.md
git commit -m "Add Oceair International website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/oceair-website.git
git push -u origin main
```

### 4. Turn on GitHub Pages
1. In your repository, go to **Settings** (top menu of the repo).
2. In the left sidebar, click **Pages**.
3. Under "Build and deployment" → **Source**, choose **Deploy from a branch**.
4. Under **Branch**, choose `main` and folder `/ (root)`, then **Save**.
5. Wait about 1 minute, then refresh the page. GitHub will show your live URL:
   `https://YOUR_USERNAME.github.io/oceair-website/`

That URL is your live website — share it, put it on business cards, add it
to your IndiaMART profile, etc. It's free, and stays up as long as the repo
exists.

### 5. Use your own domain name (optional)
If you later buy a domain (e.g. `oceairinternational.com`) from any registrar:
1. In the domain's DNS settings, add a CNAME record pointing to
   `YOUR_USERNAME.github.io`.
2. In your repo's **Settings → Pages**, enter the domain under **Custom domain**
   and save. GitHub handles the rest (including free HTTPS).

## Editing the content later
Everything — text, prices, phone number, colors — lives in `index.html`.
Open it in any text editor (VS Code, Notepad, even a Jupyter/text cell), find
the text you want to change inside the `<body>` section, edit it, save, and
either re-upload it on GitHub (Add file → Upload files → overwrite) or, if
using git, run:
```bash
git add index.html
git commit -m "Update site content"
git push
```
GitHub Pages redeploys automatically within a minute of the push.

## What's on the site right now
- Hero section with company tagline and contact CTAs (WhatsApp + Call)
- About section: company snapshot, years in trade, director name
- Products: the 6 categories from the IndiaMART listing with indicative
  starting prices
- "Why buyers come back" section
- Contact section with phone, WhatsApp link, and a link back to the full
  IndiaMART catalogue

Update the phone number, address, and any prices if they change — they're
currently pulled from the public IndiaMART listing.
