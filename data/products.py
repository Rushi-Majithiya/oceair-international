"""
All editable content for the site lives here, as plain Python data —
no HTML editing needed to update prices, categories, or company details.
"""

COMPANY = {
    "name": "Oceair International Private Limited",
    "short_name": "Oceair International Pvt Ltd",
    "tagline": "Importer and dealer of all kinds of polymers and additives.",
    "phone_display": "+91 73593 63308",
    "phone_tel": "+917359363308",
    "phone2_display": "+91 97663 09771",
    "phone2_tel": "+919766309771",
    "whatsapp": "917359363308",
    "email": "oceairinternationalpl@gmail.com",
    "gst": "24AACCO7558C1ZJ",
    "address_lines": [
        "Plot No 1, Akshar Industrial Park,",
        "Opp. Zydus Cadila Healthcare Ltd,",
        "Ahmedabad-Rajkot Highway,",
        "Ahmedabad, Gujarat - 382213, India.",
    ],
    "location": "Ahmedabad, Gujarat, India",
    "director": "K. Thakkar",
    "indiamart_url": "https://m.indiamart.com/oceair-international/",
    "indiamart_products_url": "https://m.indiamart.com/oceair-international/products.html",
}

STATS = [
    {"number": "8 yrs", "label": "In the PVC trade"},
    {"number": "5.0★", "label": "Buyer rating, 10 reviews"},
    {"number": "86%", "label": "Enquiry response rate"},
    {"number": "6+", "label": "Product categories stocked"},
]

PRODUCT_CATEGORIES = [
    {
        "icon": "granule",
        "count": "27 PRODUCTS",
        "name": "PVC Resin",
        "description": "Near-prime and off-grade suspension PVC resin, pipe-grade, K-value 65–68.",
        "price_from": "₹65/kg",
        "example": "Pvc Resin Near Prime",
    },
    {
        "icon": "bag",
        "count": "8 PRODUCTS",
        "name": "PVC Resin (Poly Vinyl Chloride)",
        "description": "Branded resin from East Hope, Formosa, Hygain, Zhongtai and other producers.",
        "price_from": "₹68/kg",
        "example": "East Hope SG5",
    },
    {
        "icon": "regrind",
        "count": "7 PRODUCTS",
        "name": "PVC Regrind",
        "description": "Grey, white and natural regrind from clean industrial PVC pipe scrap.",
        "price_from": "₹50/kg",
        "example": "Grey PVC Regrind, Japan",
    },
    {
        "icon": "powder",
        "count": "5 PRODUCTS",
        "name": "PVC Pulverized Powder",
        "description": "Ground PVC powder in white, grey and mixed-colour grades.",
        "price_from": "₹42/kg",
        "example": "Mix Colour Pulverized",
    },
    {
        "icon": "pipe",
        "count": "2 PRODUCTS",
        "name": "PVC Pipe Scrap",
        "description": "Fitting regrind and white PVC scrap sourced from pipe manufacturing.",
        "price_from": "₹55/kg",
        "example": "PVC Fitting Regrind",
    },
    {
        "icon": "flask",
        "count": "POLYMER ADDITIVES",
        "name": "Wax & Titanium Dioxide",
        "description": "Polyethylene wax and rutile titanium dioxide for plastics processing and pigmentation.",
        "price_from": "₹115/kg",
        "example": "Paraffin & PE Wax",
    },
]

PROCESS_STEPS = [
    {
        "step": "01",
        "title": "Tell us what you need",
        "description": "Send your requirement by WhatsApp, call, or the form below — product, grade, and quantity.",
    },
    {
        "step": "02",
        "title": "Get a same-day quote",
        "description": "We confirm current rate, available lot size, and dispatch timeline directly with you.",
    },
    {
        "step": "03",
        "title": "Confirm & dispatch",
        "description": "Order is confirmed, payment is handled through IndiaMART's protected payment route, and material ships.",
    },
]

FAQS = [
    {
        "question": "What quantities can you supply?",
        "answer": "We handle both trial-order quantities and regular monthly volumes. Tell us your requirement and we'll confirm what's available from current stock.",
    },
    {
        "question": "Can I get a sample before placing a full order?",
        "answer": "For most product lines, yes — ask when you enquire and we'll let you know what's possible for that specific grade.",
    },
    {
        "question": "Is payment protected?",
        "answer": "Yes. Transactions placed through IndiaMART are covered under their TrustSEAL and Payment Protection programme.",
    },
    {
        "question": "Which areas do you deliver to?",
        "answer": "We're based in Ahmedabad and regularly dispatch across Gujarat and pan-India. Share your delivery location for a freight estimate.",
    },
]
