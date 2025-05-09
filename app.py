import streamlit as st
import pandas as pd
import os
from PIL import Image
import base64
import requests

st.set_page_config(page_title="Cultiva Crop Kits Planner", layout="wide")

# Set background image and style
def set_bg_image(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        encoded_string = base64.b64encode(response.content).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: white;
        }}
/* Comment out or remove this block from your set_bg_image style section */
/*
        h1 {{
            font-family: 'Arial', sans-serif;
            font-size: 4.5rem !important;
            font-weight: bold !important;
            text-align: center !important;
            color: #005f2f !important;
            margin-bottom: 20px;
        }}
*/        

        h2 {{
            color: #005f2f !important;
            font-size: 2.5rem !important;
            font-weight: 600;
            margin-top: 1.5rem;
        }}
        
        label, p, div, .stMarkdown, .stText, .css-10trblm, .css-1d391kg {{
            color: black !important;
            font-size: 1.3rem !important;
        }}

        /* Styling for Grand Total */
        .grand-total {{
            font-size: 3rem !important;
            font-weight: bold !important;
            color: white !important;
            background-color: #005f2f !important;
            padding: 1rem 2rem !important;
            border-radius: 8px;
            text-align: center !important;
            margin: 0 !important;
        }}

        .subtotal-box {{
            background-color: #76B947;
            padding: 1rem;
            border-radius: 0.5rem;
            color: white;
            font-weight: bold;
            margin-top: 1.5rem;
            margin-bottom: 1.5rem;
            font-size: 1.5rem;
        }}

        .css-1kyxreq, .css-1l269bu {{
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
            margin-bottom: 0.25rem;
        }}
        
        .image-container {{
            float: right;
            width: 60%;
            margin-left: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}

        .text-container {{
            width: 40%;
        }}

        .product-item {{
            background-color: #f9f9f9;
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        
        .product-total {{
            background-color: #f0f0f0;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 1.2rem;
            font-weight: bold;
            color: #005f2f;
        }}
        
        .section-title {{
            font-size: 3rem !important;
            font-weight: 800 !important;
            color: #005f2f !important;
            margin-top: 2.5rem !important;
            margin-bottom: 1rem !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Background image
set_bg_image("https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/ab1ec1cd8b1399e75da0c1a2067a6445.jpg")

# Logo
logo_path = "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Cultiva_Tec_logo_with_BG__1_-removebg-preview.png"
st.image(logo_path, width=400)

# Title with updated size using HTML and inline styling
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 2rem;">
        <span style="
            font-size: 5rem;
            font-weight: bold;
            color: #005f2f;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        ">
            🌾 Cultiva Crop Kits Planner – Dealer Wise
        </span>
        <div style="
            font-size: 1.8rem;
            color: #333;
            margin-top: 0.5rem;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        ">
            Plan your crop kit orders with precision and clarity.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


category_images = {
    "EXOME": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Exome-Photoroom.png",
    "CULTIVATEC": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/CultivaTec%20Planner-1-Photoroom.png",
    "GROWTH PROMOTOR": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Growth%20promoter-Photoroom.png",
    "ADDITIONAL": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Additional-Photoroom%20(1).png"
}

# Product data
products = {
    "EXOME": [
        {"Product": "NEMARID", "SKU": "500 ML", "Qty": 24, "Value": 30816},
        {"Product": "MINBOOST", "SKU": "250 ML", "Qty": 12, "Value": 21780},
        {"Product": "TETRA POWER", "SKU": "250 ML", "Qty": 1, "Value": 1546},
        {"Product": "K BIO", "SKU": "250 ML", "Qty": 1, "Value": 1508},
        {"Product": "CAL RATNA", "SKU": "250 ML", "Qty": 12, "Value": 14628},
    ],
    "CULTIVATEC": [
        {"Product": "RHODY POTASH", "SKU": "150 GMS", "Qty": 7, "Value": 20223},
        {"Product": "GLY ZN", "SKU": "250 ML", "Qty": 20, "Value": 13360},
        {"Product": "MAX ZN", "SKU": "250 ML", "Qty": 20, "Value": 26880},
    ],
    "GROWTH PROMOTOR": [
        {"Product": "BLACK DIAMOND", "SKU": "500 ML", "Qty": 50, "Value": 69000},
    ],
    "ADDITIONAL": [
        {"Product": "HARVESTER", "SKU": "250 ML", "Qty": 1, "Value": 1340},
        {"Product": "BUD GROW", "SKU": "500 ML", "Qty": 1, "Value": 1300},
    ]
}

# Display sections
total_value = 0
for section, items in products.items():
    st.markdown(f"""<div class="section-title">📦 {section}</div>""", unsafe_allow_html=True)
    image_url = category_images.get(section)    # Display category image once per section
    if image_url:
        # Convert the image to base64 to embed it in HTML
        response = requests.get(image_url)
        if response.status_code == 200:
            encoded_string = base64.b64encode(response.content).decode()
            # Embed the image in HTML
            image_html = f'<div class="image-container"><img src="data:image/png;base64,{encoded_string}" width="400"/></div>'
            st.markdown(image_html, unsafe_allow_html=True)
        else:
            st.warning(f"⚠️ Image for {section} not found.")

    section_total = 0

    # For each product in the section
    for idx, item in enumerate(items):
        cols = st.columns([1, 1, 1, 1], gap="small")  # More compact columns
        with cols[0]:
            st.markdown(f"**{item['Product']}**")
        with cols[1]:
            st.write(item['SKU'])
        with cols[2]:
            qty = st.number_input("Qty", min_value=0, value=item["Qty"], step=1, key=f"{section}_{idx}")
        with cols[3]:
            unit_price = item["Value"] / item["Qty"] if item["Qty"] else 0
            value = qty * unit_price
            section_total += value
            st.markdown(f"<div class='product-total'>₹{value:,.0f}</div>", unsafe_allow_html=True)

    st.markdown(
        f"""<div class='subtotal-box'>Subtotal for {section}: ₹{section_total:,.0f}</div>""",
        unsafe_allow_html=True
    )
    total_value += section_total

# Grand total
st.markdown("---")
# Grand total styling for better highlight
st.markdown(
    f"""
    <div class="grand-total">
        🧮 Grand Total: ₹{total_value:,.0f}
    </div>
    """,
    unsafe_allow_html=True
)
