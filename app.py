import streamlit as st
from datetime import date
import pandas as pd

# Constants
CASE_VOLUME_LITERS = 12
SCHEME_TARGET_SALES = 300000
SCHEME_REWARD_AMOUNT = 90000
total_rhody_grams = 0

# Logo and title
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Cultiva_Tec_logo_with_BG__1_-removebg-preview.png' width='400'>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("""
<div style='text-align: center;'>
    <h2 style='color:#1B5E20;font-size:22px;'>🌾 Nutrition Navaratnalu Scheme Planner</h2>
    <p style='font-size:16px; color:#444;'>Plan Smart. Earn Big. Unlock Rewards.</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: center; margin-top: -10px;'>
        <img src='https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/49227985b502547253ed8c285346624a17b30a67/NN.png?raw=true' 
             width='500' 
             style='box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3); border-radius: 10px;'>
    </div>
    """,
    unsafe_allow_html=True
)\
# Dealer info
st.header("👤 Dealer Information")
col1, col2, col3 = st.columns(3)
with col1:
    customer_name = st.text_input("Name")
with col2:
    customer_code = st.text_input("Customer Code")
with col3:
    order_date = st.date_input("Date", value=date.today())

# Product Info Helper
product_info_data = {
    "Nemarid": {
        "Overview": ["📏 No. of Acres Suggested:", "👨‍🌾 No. of Farmers Required:"],
        "Application": [
            {"Stage": "🌱 Soil Application", "Details": "Nemarid (500 ml) + Farm Yard Manure"},
            {"Stage": "🌿 Vegetative Period", "Details": "Nemarid + 1 Bag Urea"},
        ],
        "Dosage": ["🧪 500 ml / acre", "🧪 0.5 ml–2 ml / liter"],
        "Benefits": [
            "🌾 100% Germination",
            "🌿 More branches",
            "🐛 Kills root grubs & nematodes",
            "🛡️ Pest Resistance"
        ],
        "Crops": ["🌶️ Chilli", "👕 Cotton", "🌾 Paddy"]
    },

    "Tetrapower": {
        "Overview": ["📏 No. of Acres Suggested:", "👨‍🌾 No. of Farmers Required:"],
        "Application": [
            {"Stage": "🌿 Vegetative Period", "Details": "Tetrapower + 1 Bag Urea"},
            {"Stage": "🌼 Reproductive Stage", "Details": "Foliar spray or Fertigation"},
        ],
        "Dosage": ["🧪 250 ml / acre", "🧪 1 ml–2 ml / liter"],
        "Benefits": [
            "🛡️ Resistance to abiotic stress",
            "🌸 Reduces buds & flower drop",
            "🌱 More buds per branch",
            "🌼 Enhances flowering & bud formation"
        ],
        "Crops": ["🌶️ Chilli", "👕 Cotton", "🌾 Paddy"]
    },

    "K-Bio": {
        "Overview": ["📏 No. of Acres Suggested:", "👨‍🌾 No. of Farmers Required:"],
        "Application": [
            {"Stage": "🌿 Vegetative Period", "Details": "K-Bio + 1 Bag Urea"},
            {"Stage": "🌼 Flowering Stage", "Details": "Spray with pesticide or water soluble fertilizer"},
            {"Stage": "🍎 Seed & Fruit Development", "Details": "Spray with pesticide or water soluble fertilizer"},
        ],
        "Dosage": ["🧪 250 ml / acre", "🧪 0.5 ml–2 ml / liter"],
        "Benefits": [
            "🟢 Uniform maturity & ripening",
            "🍎 Improved size of produce",
            "✅ Spotless harvest",
            "🌾 Full grain/pod development"
        ],
        "Crops": ["🌶️ Chilli", "👕 Cotton", "🌾 Paddy"]
    },

    "Calratna": {
        "Overview": ["📏 No. of Acres Suggested:", "👨‍🌾 No. of Farmers Required:"],
        "Application": [
            {"Stage": "🌱 Shoot Development", "Details": "Foliar spray"},
            {"Stage": "🌼 Bud Formation & Flowering", "Details": "Spray with pesticide or water soluble fertilizer"},
            {"Stage": "🍎 Seed & Fruit Development", "Details": "Spray with pesticide or water soluble fertilizer"},
        ],
        "Dosage": ["🧪 250 ml / acre", "🧪 0.5 ml–2 ml / liter"],
        "Benefits": [
            "🍎 Reduced fruit abnormalities",
            "⚖️ Corrects root zone pH",
            "🥇 Better fruit setting, Stromger cell Walls",
            "💪 Improves fruit quality & size"
        ],
        "Crops": ["🌶️ Chilli", "👕 Cotton", "🌾 Paddy"]
    },

    "Rhody Potash": {
        "Overview": ["📏 No. of Acres Suggested:", "👨‍🌾 No. of Farmers Required:"],
        "Application": [
            {"Stage": "🚜 Tilling Stage", "Details": "Foliar spray or Fertigation"},
            {"Stage": "🌼 Pre-Flowering Stage", "Details": "Foliar spray or Fertigation"},
            {"Stage": "🍎 Seed & Fruit Development", "Details": "Foliar spray or Fertigation"},
        ],
        "Dosage": ["🧪 150 gms / acre", "🧪 1.5 g / liter"],
        "Benefits": [
            "🍎 Enhanced fruit size & quality",
            "📈 Improved yield",
            "🛡️ Resistance to abiotic stress",
            "🌼 Faster Flowering & Uniform blooming"
        ],
        "Crops": ["🌶️ Chilli", "👕 Cotton", "🌾 Paddy"]
    },

    "Black Diamond": {
        "Overview": ["📏 No. of Acres Suggested:", "👨‍🌾 No. of Farmers Required:"],
        "Application": [
            {"Stage": "🌱 Shoot Development", "Details": "Soil Drenching (500 ml)"},
            {"Stage": "🌼 Bud Formation & Flowering", "Details": "Foliar spray"},
            {"Stage": "🍎 Fruit Development", "Details": "Foliar spray"},
        ],
        "Dosage": ["🧪 500 ml / acre", "🧪 3 ml–5 ml / liter"],
        "Benefits": [
            "🌿 Rapid canopy establishment with dark green leaves",
            "🌱 Quick root emergence",
            "🍎 Uniform fruit development with enhanced colour & firmness",
            "❌ Significant reduction in early flower & fruit drop"
        ],
        "Crops": ["🌶️ Chilli", "👕 Cotton", "🌾 Paddy"]
    },

    "Gly-Zinc": {
        "Overview": ["📏 No. of Acres Suggested:", "👨‍🌾 No. of Farmers Required:"],
        "Application": [
            {"Stage": "🌱 Shoot Development", "Details": "Foliar spray or Fertigation"},
            {"Stage": "🌿 Vegetative Stage", "Details": "Foliar spray or Fertigation"},
            {"Stage": "🌼 Flowering", "Details": "Foliar spray or Fertigation"},
        ],
        "Dosage": ["🧪 250 ml / acre", "🧪 1 ml / liter"],
        "Benefits": [
            "🌿 Greener plants - no Zn deficiency symptoms",
            "🌼 Better Flower Hold & Reduced  Flower Drop",
            "🌱 Early Shoot and Branch Development",
            "🌸 Increased Bud Initiation & Uniform Flowering"
        ],
        "Crops": ["🌶️ Chilli", "👕 Cotton", "🌾 Paddy"]
    },

    "Harvester": {
        "Overview": ["📏 No. of Acres Suggested:", "👨‍🌾 No. of Farmers Required:"],
        "Application": [
            {"Stage": "🌸 Early Reproductive Stage", "Details": "Foliar spray"},
            {"Stage": "🌼 Flowering", "Details": "Foliar spray"},
        ],
        "Dosage": ["🧪 2 ml / liter"],
        "Benefits": [
            "🌸 More flowers -> Reduced flower drop",
            "🧬 Better pollination → More fruits formation",
            "🚀 Faster Crop Growth & Maturity",
            "📈 Increased yield & quality"
        ],
        "Crops": ["🌶️ Chilli", "👕 Cotton", "🌾 Paddy"]
    },

    "Gainup": {
        "Overview": ["📏 No. of Acres Suggested:", "👨‍🌾 No. of Farmers Required:"],
        "Application": [
            {"Stage": "🌿 Vegetative Stage", "Details": "Basal Application"},
            {"Stage": "🌼 Reproductive Stage", "Details": "Foliar spray"},
        ],
        "Dosage": ["🧪 500 ml / acre", "🧪 1–2 ml / liter"],
        "Benefits": [
            "🍎 Improved fruit/seed size, color, and surface shine",
            "🌿 Increased branching & vegetative growth",
            "🌱 Higher Root initiation",
            "✅ Reduced deformities, black spots, & poor texture."
        ],
        "Crops": ["🌶️ Chilli", "👕 Cotton", "🌾 Paddy"]
    }
}

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
    st.markdown(f"""
    <div style='text-align: center; margin-bottom: 15px;'>
        <h2 style='color: #33691E;'>{product['Name']}</h3>
        <img src="{product['Image']}" width="140">
    </div>
""", unsafe_allow_html=True)

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
        label = f"{product['Size']} {product['Unit']} packs"
        qty = st.number_input(label, min_value=0, step=1, key=product['Name'])
        value = qty * product["Unit Value"]
        profit = qty * product["Unit Profit"]

        if product["Unit"] == "ml":
            volume = qty * product["Size"] / 1000  # ml to liters
        else:
            volume = qty * product["Size"]

        if product["Name"] == "Rhody Potash":
            total_rhody_grams += volume

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

    # ✅ Insert the following block here:
    if product["Name"] in product_info_data:
        with st.expander("📘 Product Information"):
            info = product_info_data[product["Name"]]

            if "Overview" in info:
                st.markdown("<b>📋 Overview:</b>", unsafe_allow_html=True)
                for line in info["Overview"]:
                    st.markdown(f"<p style='margin:0;'>{line}</p>", unsafe_allow_html=True)

            if "Application" in info:
                st.markdown("<br><b>🧪 Application Methodology:</b>", unsafe_allow_html=True)
                for stage in info["Application"]:
                    st.markdown(f"<p style='margin:0;'><b>{stage['Stage']}</b>: {stage['Details']}</p>", unsafe_allow_html=True)

            if "Dosage" in info:
                st.markdown("<br><b>🧴 Dosage:</b>", unsafe_allow_html=True)
                for dose in info["Dosage"]:
                    st.markdown(f"<p style='margin:0;'>{dose}</p>", unsafe_allow_html=True)

            if "Benefits" in info:
                st.markdown("<br><b>✨ Benefits:</b>", unsafe_allow_html=True)
                for benefit in info["Benefits"]:
                    st.markdown(f"<p style='margin:0;'>{benefit}</p>", unsafe_allow_html=True)

            if "Crops" in info:
                st.markdown("<br><b>🌾 Suitable Crops:</b>", unsafe_allow_html=True)
                st.markdown(f"<p style='margin:0;'>{' | '.join(info['Crops'])}</p>", unsafe_allow_html=True)

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
# Progress calculation
scheme_progress_percent = min((total_value / SCHEME_TARGET_SALES) * 100, 100)

# Colored progress bar function
def color_progress_bar(percent):
    if percent < 50:
        color = "#e53935"  # 🔴 Red
    elif percent < 90:
        color = "#fb8c00"  # 🟠 Orange
    else:
        color = "#43a047"  # 🟢 Green

    st.markdown(f"""
    <div style="margin-top: 10px; margin-bottom: 6px; font-weight: bold; color: #1B5E20;">
        🎯 Scheme Eligibility Progress: {percent:.1f}% of ₹3,00,000 Target
    </div>
    <div style="height: 24px; background-color: #eee; border-radius: 12px; overflow: hidden;">
      <div style="width: {percent}%; height: 100%; background-color: {color}; border-radius: 12px;"></div>
    </div>
    """, unsafe_allow_html=True)

# Display progress
color_progress_bar(scheme_progress_percent)


# Scheme Rewards
if total_value >= SCHEME_TARGET_SALES:
    st.success("🎉 Congratulations! You're eligible for the full scheme rewards worth ₹90,000.")
    with st.expander("💎 Scheme Reward Breakdown"):
        st.markdown("""
        | ✨ Reward Item | Value | Includes |
        |---------------|--------|----------|
        | ✈️ **Foreign Trip** | ₹50,000 | Flight tickets, Hotel |
        | 🪙 **Gold Coin** | ₹9,000 | 1 Gold Coin |
        | 💸 **Advance Payment Discount** | ₹21,000 | Instant Cashback |
        | **Total** | **₹90,000** | 🎁 |
        """, unsafe_allow_html=True)
    total_profit_combined = total_profit + SCHEME_REWARD_AMOUNT
else:
    st.info("ℹ️ To unlock ₹90,000 in rewards, reach ₹3,00,000 in total purchases.")
    total_profit_combined = total_profit + SCHEME_REWARD_AMOUNT

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