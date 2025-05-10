import streamlit as st
import pandas as pd
from datetime import datetime

logo_path = "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Cultiva_Tec_logo_with_BG__1_-removebg-preview.png"
st.image(logo_path, width=400)

st.markdown(
    "<h1 style='color:#1B5E20;'>🌾 Cultiva Crop Kit Order Planner</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<style>
.subtotal-box {
    background-color: #e8f5e9;
    padding: 10px;
    margin: 10px 0;
    border-left: 6px solid #43a047;
    border-radius: 4px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("Use this tool to plan your product orders and see estimated totals instantly.")

# User input section
st.markdown("### 👤 Dealer Information")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        customer_name = st.text_input("Name")
    with col2:
        customer_code = st.text_input("Customer Code")
    with col3:
        today_date = st.date_input("Date")

# Product data
category_images = {
    "EXOME": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Exome-Photoroom.png",
    "CULTIVATEC": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/CultivaTec%20Planner-1-Photoroom.png",
    "GROWTH PROMOTOR": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Growth%20promoter-Photoroom.png",
    "ADDITIONAL": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Additional-Photoroom%20(1).png"
}

data = {
    "🌱EXOME": [
        {"Product": "NEMARID", "SKU": "500 ML", "Qty": 1, "Value": 1284},
        {"Product": "MINBOOST", "SKU": "250 ML", "Qty": 1, "Value": 1815},
        {"Product": "TETRA POWER", "SKU": "250 ML", "Qty": 1, "Value": 1546},
        {"Product": "K BIO", "SKU": "250 ML", "Qty": 1, "Value": 1508},
        {"Product": "CAL RATNA", "SKU": "250 ML", "Qty": 1, "Value": 1219},
    ],
    "🍃CULTIVATEC": [
        {"Product": "RHODY POTASH", "SKU": "150 GMS", "Qty": 1, "Value": 2889},
        {"Product": "GLY ZN", "SKU": "250 ML", "Qty": 1, "Value": 668},
        {"Product": "MAX ZN", "SKU": "250 ML", "Qty": 1, "Value": 1344},
    ],
    "🌿GROWTH PROMOTOR": [
        {"Product": "BLACK DIAMOND", "SKU": "500 ML", "Qty": 1, "Value": 1380},
    ],
    "🧰ADDITIONAL": [
        {"Product": "HARVESTER", "SKU": "250 ML", "Qty": 1, "Value": 1340},
        {"Product": "BUD GROW", "SKU": "500 ML", "Qty": 1, "Value": 1300},
    ]
}

# Build DataFrame
rows = []
for category, products in data.items():
    for product in products:
        rows.append({
            "Category": category,
            "Product": product["Product"],
            "SKU": product["SKU"],
            "Qty": product["Qty"],
            "Value": product["Value"]
        })
df = pd.DataFrame(rows)

# --- Quantity Inputs and Subtotals ---
st.subheader("📦 Select Product Quantities")
total_value = 0
for category in df["Category"].unique():
    st.markdown(f"### {category}")
    if category in category_images:
        st.image(category_images[category], width=150)

    category_df = df[df["Category"] == category].copy()
    section_total = 0

    for i in category_df.index:
        col1, col2, col3, col4, col5 = st.columns([2, 3, 2, 2, 2])
        with col1:
            st.markdown(df.at[i, "Product"])
        with col2:
            st.markdown(f"SKU: {df.at[i, 'SKU']}")
        with col3:
            df.at[i, "Qty"] = st.number_input(
                f"Qty_{i}", min_value=0, value=int(df.at[i, "Qty"]), step=1
            )
        with col4:
            product_total = df.at[i, "Value"] * df.at[i, "Qty"]
            st.markdown(
                f"<div style='background-color:#f5f5dc; padding: 5px 10px; border-radius: 5px;'> ₹{product_total:.2f} </div>",
                unsafe_allow_html=True
            )

        section_total += product_total

    # Show subtotal after category
    st.markdown(
        f"""<div class='subtotal-box'>Subtotal: ₹{section_total:,.0f}</div>""",
        unsafe_allow_html=True
    )
    total_value += section_total

# --- Order Summary ---
df["Total"] = df["Value"] * df["Qty"]

st.subheader("📊 Order Summary")
summary_rows = []

for category in df["Category"].unique():
    cat_df = df[df["Category"] == category]
    subtotal = cat_df["Total"].sum()
    for _, row in cat_df.iterrows():
        if row["Qty"] > 0:
            summary_rows.append({
                "Customer Name": customer_name,
                "Customer Code": customer_code,
                "Date": today_date,
                "Category": category,
                "Product": row["Product"],
                "Quantity": row["Qty"],
                "Total": f"₹{row['Total']:.2f}"
            })
    if subtotal > 0:
        summary_rows.append({
            "Customer Name": customer_name,
            "Customer Code": customer_code,
            "Date": today_date,
            "Category": "",
            "Product": f"Subtotal ({category})",
            "Quantity": "",
            "Total": f"₹{subtotal:.2f}"
        })

# Display table and download
if summary_rows:
    summary_df = pd.DataFrame(summary_rows)
    st.table(summary_df[["Category", "Product", "Quantity", "Total"]])

    st.markdown(f"### 🧳 Grand Total: ₹{total_value:.2f}", unsafe_allow_html=True)

    csv = summary_df.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📥 Download Summary as CSV",
        data=csv,
        file_name="order_summary.csv",
        mime="text/csv"
    )
else:
    st.info("Add quantities to see the order summary and download options.")