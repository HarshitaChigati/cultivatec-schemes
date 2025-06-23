import streamlit as st
from datetime import date
import pandas as pd

# Constants
CASE_VOLUME_LITERS = 12
SCHEME_TARGET_SALES = 300000
SCHEME_REWARD_AMOUNT = 88000
total_rhody_grams = 0

# Logo and title
st.image("https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Cultiva_Tec_logo_with_BG__1_-removebg-preview.png", width=400)
st.markdown("<h1 style='color:#1B5E20;'>🌾 Nutrition Navaratnalu Scheme Planner</h1>", unsafe_allow_html=True)
st.write("Plan your product orders with cases and units. Totals in ₹, liters, and grams.")

# Dealer info
st.header("👤 Dealer Information")
col1, col2, col3 = st.columns(3)
with col1:
    customer_name = st.text_input("Name")
with col2:
    customer_code = st.text_input("Customer Code")
with col3:
    order_date = st.date_input("Date", value=date.today())

# Product List
products = [
    {"Name": "Nemarid", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Nemarid.jpg?raw=true", "Type": "case", "SKUs": [
        {"Label": "250 ml", "Dealer Price": 16128, "Profit": 6576},
        {"Label": "500 ml", "Dealer Price": 15456, "Profit": 5976},
    ]},
    {"Name": "Tetrapower", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Tetrapower?raw=true", "Type": "case", "SKUs": [
        {"Label": "250 ml", "Dealer Price": 18576, "Profit": 4128},
    ]},
    {"Name": "K-Bio", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/K-Bio?raw=true", "Type": "case", "SKUs": [
        {"Label": "250 ml", "Dealer Price": 18096, "Profit": 4608},
    ]},
    {"Name": "Calratna", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Calratna?raw=true", "Type": "case", "SKUs": [
        {"Label": "250 ml", "Dealer Price": 14640, "Profit": 5520},
    ]},
    {"Name": "Gainup", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Gainup?raw=true", "Type": "case", "SKUs": [
        {"Label": "250 ml", "Dealer Price": 14112, "Profit": 6048},
    ]},
    {"Name": "Harvester", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Harvester?raw=true", "Type": "case", "SKUs": [
        {"Label": "250 ml", "Dealer Price": 18576, "Profit": 4128},
    ]},
    {"Name": "Rhody Potash", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Rhody%20Potash?raw=true", "Type": "unit", "Unit": "gms", "Size": 150, "Unit Value": 413, "Unit Profit": 262},
    {"Name": "Gly-Zinc", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Gly%20Zn.png?raw=true", "Type": "unit", "Unit": "ml", "Size": 250, "Unit Value": 167, "Unit Profit": 183},
    {"Name": "Black Diamond", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Black%20Diamond?raw=true", "Type": "unit", "Unit": "ml", "Size": 500, "Unit Value": 599, "Unit Profit": 201},
]

# Tracking totals
order_list = []
total_value = 0
total_liters = 0
total_profit = 0

for product in products:
    st.markdown(f"### {product['Name']}")
    st.image(product["Image"], width=150)

    subtotal_value = 0
    subtotal_volume = 0
    subtotal_profit = 0

    if product["Type"] == "case":
        cols = st.columns(len(product["SKUs"]))
        for i, sku in enumerate(product["SKUs"]):
            with cols[i]:
                qty = st.number_input(f"{sku['Label']} cases", min_value=0, step=1, key=f"{product['Name']}_{sku['Label']}")
                liters = qty * CASE_VOLUME_LITERS
                value = qty * sku["Dealer Price"]
                profit = qty * sku["Profit"]
                
                subtotal_value += value
                subtotal_volume += liters
                subtotal_profit += profit

    elif product["Type"] == "unit":
        label = f"{product['Size']} {product['Unit']} packs" if "Size" in product else f"{product['Unit']} packs"
        qty = st.number_input(label, min_value=0, step=1, key=product['Name'])

        value = qty * product["Unit Value"]
        profit = qty * product["Unit Profit"]
        
        if product["Unit"] == "ml":
            volume = qty * product["Size"] / 1000  # ml to liters
        else:
            volume = qty * product["Size"] if "Size" in product else qty  # grams or count

        if product["Name"] == "Rhody Potash":
            total_rhody_grams += volume  # volume = qty × 150 gms

        subtotal_value += value
        subtotal_volume += volume
        subtotal_profit += profit

    volume_unit = "L" if product.get("Unit") != "gms" else "g"
    st.markdown(f"""
    <div style="background-color: #F1F8E9; padding: 10px; border-radius: 10px; margin-top: 10px; border-left: 6px solid #4CAF50;">
      <p style="margin: 0; font-weight: 600; color: #2E7D32;">
        💰 <span style='font-size: 18px;'>Subtotal:</span> 
        ₹ <span style='font-size: 18px;'>{subtotal_value:,.0f}</span> &nbsp;&nbsp;
        🧪 {subtotal_volume} {volume_unit} &nbsp;&nbsp;
        📈 ₹ {subtotal_profit:,.0f} profit
      </p>
    </div>
    """, unsafe_allow_html=True)

    if subtotal_value > 0:
        order_list.append({
            "Product": product["Name"],
            "Quantity": subtotal_volume if product.get("Unit") != "gms" else f"{int(subtotal_volume)} gms",
            "Subtotal Value (₹)": subtotal_value,
            "Subtotal Profit (₹)": subtotal_profit
        })

    total_value += subtotal_value
    total_liters += subtotal_volume if product.get("Unit") != "gms" else 0
    total_profit += subtotal_profit

volume_display = f"{total_liters:.2f} L"
if total_rhody_grams > 0:
    volume_display += f" + {total_rhody_grams:.0f} Gms"

# Final Summary
st.markdown(f"# 🧾 Grand Total: ₹ {total_value:,.0f} | 🧪 {volume_display} | 📈 ₹ {total_profit:,.0f} Margin")

# Scheme Progress
scheme_progress = total_value / SCHEME_TARGET_SALES * 100
st.markdown(f"### 🎯 Scheme Eligibility Progress: {scheme_progress:.1f}% of ₹3,00,000 Target")

# Scheme Rewards
if total_value >= SCHEME_TARGET_SALES:
    st.success("🎉 Congratulations! You're eligible for the full scheme rewards worth ₹88,000.")
    with st.expander("💎 Scheme Reward Breakdown"):
        st.markdown("""
        | ✨ Reward Item | Value | Includes |
        |---------------|--------|----------|
        | ✈️ **Foreign Trip** | ₹50,000 | Flight tickets, Hotel |
        | 🪙 **Gold Coin** | ₹9,000 | 1 Gold Bar |
        | 💸 **Advance Payment Discount** | ₹21,000 | Instant Cashback |
        | **Total** | **₹90,000** | 🎁 |
        """, unsafe_allow_html=True)
    total_profit_combined = total_profit + SCHEME_REWARD_AMOUNT
else:
    st.info("ℹ️ To unlock ₹88,000 in rewards, reach ₹3,00,000 in total purchases.")
    total_profit_combined = total_profit

st.markdown(f"## 💼 Total Profit (including scheme): ₹ {total_profit_combined:,.0f}")

# Order Summary
if order_list:
    st.header("📄 Order Summary")
    df = pd.DataFrame(order_list)
    df["Customer Name"] = customer_name
    df["Customer Code"] = customer_code
    df["Order Date"] = order_date
    st.dataframe(df)

    csv_data = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="Download order summary as CSV",
        data=csv_data,
        file_name="cultivatec_order_summary.csv",
        mime="text/csv"
    )
else:
    st.info("Add quantities above to see order summary and download option.")
