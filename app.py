import streamlit as st
from datetime import date
import pandas as pd

# Constants
CASE_VOLUME_LITERS = 12
SCHEME_TARGET_SALES = 300000
SCHEME_REWARD_AMOUNT = 88000

# Logo and title
logo_url = "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Cultiva_Tec_logo_with_BG__1_-removebg-preview.png"
st.image(logo_url, width=400)
st.markdown("<h1 style='color:#1B5E20;'>🌾 Nutrition Navaratnalu Scheme Planner</h1>", unsafe_allow_html=True)
st.write("Plan your product orders with case sizes and get totals in ₹ and liters.")

# Dealer info
st.header("👤 Dealer Information")
col1, col2, col3 = st.columns(3)
with col1:
    customer_name = st.text_input("Name")
with col2:
    customer_code = st.text_input("Customer Code")
with col3:
    order_date = st.date_input("Date", value=date.today())

# Images per category
category_images = {
    "EXOME": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Exome-Photoroom.png",
    "CULTIVATEC": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/CultivaTec%20Planner-1-Photoroom.png",
    "GROWTH PROMOTOR": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Growth%20promoter-Photoroom.png",
    "ADDITIONAL": "https://raw.githubusercontent.com/HarshitaChigati/cultivatec-schemes/63527d8b3150a783a707d822e072e74ccf49dc7d/Additional-Photoroom%20(1).png"
}

# Full product dataset (keep your data here)
data = {
    "EXOME": {
        "Nemarid": {
            "100 ml": {"Dealer Price Case": 20400, "Farmer Price Case": 31560, "Dealer Profit Case": 11160, "Profit%": 55},
            "250 ml": {"Dealer Price Case": 16128, "Farmer Price Case": 25200, "Dealer Profit Case": 9072, "Profit%": 56},
            "500 ml": {"Dealer Price Case": 15456, "Farmer Price Case": 23400, "Dealer Profit Case": 7944, "Profit%": 51},
            "1 Ltr":  {"Dealer Price Case": 15060, "Farmer Price Case": 23940, "Dealer Profit Case": 8880, "Profit%": 59},
            "5 Ltr":  {"Dealer Price Case": 14640, "Farmer Price Case": 22428, "Dealer Profit Case": 7788, "Profit%": 53},
        },
        "Minboost": {
            "100 ml": {"Dealer Price Case": 28560, "Farmer Price Case": 37800, "Dealer Profit Case": 9240, "Profit%": 32},
            "250 ml": {"Dealer Price Case": 25392, "Farmer Price Case": 30240, "Dealer Profit Case": 4848, "Profit%": 19},
            "500 ml": {"Dealer Price Case": 22848, "Farmer Price Case": 27720, "Dealer Profit Case": 4872, "Profit%": 21},
            "1 Ltr":  {"Dealer Price Case": 21780, "Farmer Price Case": 25200, "Dealer Profit Case": 3420, "Profit%": 16},
            "5 Ltr":  {"Dealer Price Case": 21180, "Farmer Price Case": 23940, "Dealer Profit Case": 2760, "Profit%": 13},
        },
        "Tetrapower": {
            "100 ml": {"Dealer Price Case": 22320, "Farmer Price Case": 31560, "Dealer Profit Case": 9240, "Profit%": 41},
            "250 ml": {"Dealer Price Case": 18552, "Farmer Price Case": 22680, "Dealer Profit Case": 4128, "Profit%": 22},
            "500 ml": {"Dealer Price Case": 17016, "Farmer Price Case": 21432, "Dealer Profit Case": 4416, "Profit%": 26},
            "1 Ltr":  {"Dealer Price Case": 15900, "Farmer Price Case": 20160, "Dealer Profit Case": 4260, "Profit%": 27},
            "5 Ltr":  {"Dealer Price Case": 15444, "Farmer Price Case": 17640, "Dealer Profit Case": 2196, "Profit%": 14},
        },
        "K-Bio": {
            "100 ml": {"Dealer Price Case": 21840, "Farmer Price Case": 25200, "Dealer Profit Case": 3360, "Profit%": 15},
            "250 ml": {"Dealer Price Case": 18096, "Farmer Price Case": 22680, "Dealer Profit Case": 4584, "Profit%": 25},
            "500 ml": {"Dealer Price Case": 17256, "Farmer Price Case": 21432, "Dealer Profit Case": 4176, "Profit%": 24},
            "1 Ltr":  {"Dealer Price Case": 15816, "Farmer Price Case": 20160, "Dealer Profit Case": 4344, "Profit%": 27},
            "5 Ltr":  {"Dealer Price Case": 15408, "Farmer Price Case": 18900, "Dealer Profit Case": 3492, "Profit%": 23},
        },
        "Calratna": {
            "100 ml": {"Dealer Price Case": 16320, "Farmer Price Case": 22680, "Dealer Profit Case": 6360, "Profit%": 39},
            "250 ml": {"Dealer Price Case": 14628, "Farmer Price Case": 20160, "Dealer Profit Case": 5532, "Profit%": 38},
            "500 ml": {"Dealer Price Case": 12672, "Farmer Price Case": 17640, "Dealer Profit Case": 4968, "Profit%": 39},
            "1 Ltr":  {"Dealer Price Case": 11544, "Farmer Price Case": 15756, "Dealer Profit Case": 4212, "Profit%": 36},
            "5 Ltr":  {"Dealer Price Case": 11184, "Farmer Price Case": 13860, "Dealer Profit Case": 2676, "Profit%": 24},
        },
        "Gainup": {
            "100 ml": {"Dealer Price Case": 18480, "Farmer Price Case": 22680, "Dealer Profit Case": 6720, "Profit%": 39},
            "250 ml": {"Dealer Price Case": 14100, "Farmer Price Case": 20160, "Dealer Profit Case": 6060, "Profit%": 38},
            "500 ml": {"Dealer Price Case": 13824, "Farmer Price Case": 17640, "Dealer Profit Case": 5088, "Profit%": 39},
            "1 Ltr":  {"Dealer Price Case": 12240, "Farmer Price Case": 15756, "Dealer Profit Case": 4140, "Profit%": 36},
            "5 Ltr":  {"Dealer Price Case": 11880, "Farmer Price Case": 13860, "Dealer Profit Case": 3240, "Profit%": 24},        
        }
    },
    "CULTIVATEC": [
        {"Product": "RHODY POTASH", "SKUs": [150], "Unit_Price_per_case": [413], "Profit": [97], "Unit": "gms"},
        {"Product": "GLY ZN", "SKUs": [250], "Unit_Price_per_case": [167], "Profit": [183],"Unit": "ml"},
        {"Product": "MAX N-75", "SKUs": [5, 25], "Unit_Price_per_case": [650, 3250], "Profit": [150, 750], "Unit": "Kgs"},
    ],
    "GROWTH PROMOTOR": [
        {"Product": "BLACK DIAMOND", "SKUs": [500], "Unit_Price_per_case": [599], "Profit": [201], "Unit": "ml"},
    ],
    "ADDITIONAL": [
        {"Product": "HARVESTER", "SKUs": [100,250, 500, 1000, 5000],"Unit_Price_per_case": [22440, 19668, 17160, 16080, 15636], "Profit":[9120, 5292, 4272, 4080, 3264], "Unit": "ml"
        },
        {"Product": "BUD GROW", "SKU": [500], "Unit_Price_per_case": [580], "Profit": [116], "Unit": "ml"},
    ],
}

# Tracking totals
order_list = []
total_value = 0
total_liters = 0
total_profit = 0

# Iterate categories
for category, products in data.items():
    st.markdown(f"""
<div style="background-color: #F1F8E9; padding: 10px 20px; border-radius: 10px; margin-top: 30px;">
  <h2 style="color:#33691E; margin-bottom: 5px;">🌿 {category.title()}</h2>
</div>
""", unsafe_allow_html=True)

    if category in category_images:
        st.image(category_images[category], width=160)


    category_value = 0
    category_liters = 0
    category_profit = 0

    # 1. Nested dict format (like EXOME, ADDITIONAL['Harvester'])
    if isinstance(products, dict):
        for product_name, sku_dict in products.items():
            st.markdown(f"### {product_name}")
            cols = st.columns(len(sku_dict))

            subtotal_value = 0
            subtotal_liters = 0
            subtotal_profit = 0

            for i, (sku, info) in enumerate(sku_dict.items()):
                with cols[i]:
                    qty = st.number_input(f"{sku} cases", min_value=0, step=1, key=f"{category}_{product_name}_{sku}")
                    liters = qty * CASE_VOLUME_LITERS
                    value = qty * info["Dealer Price Case"]
                    profit = qty * info["Dealer Profit Case"]

                    st.markdown(f"₹ {value:,.0f} | {liters} L")
                    subtotal_value += value
                    subtotal_liters += liters
                    subtotal_profit += profit

            if subtotal_value > 0:
                order_list.append({
                    "Category": category,
                    "Product": product_name,
                    "Quantity (cases total)": subtotal_liters / CASE_VOLUME_LITERS,
                    "Subtotal Value (₹)": subtotal_value,
                    "Subtotal Liters": subtotal_liters,
                    "Subtotal Profit (₹)": subtotal_profit
                })

            st.markdown(f"""
<div style="background-color: #F1F8E9; padding: 10px; border-radius: 10px; margin: 10px 0; border-left: 6px solid #4CAF50;">
  <p style="margin: 0; font-weight: 600; color: #2E7D32;">
    💰 <span style='font-size: 18px;'>Subtotal:</span> 
    ₹ <span style='font-size: 18px;'>{subtotal_value:,.0f}</span> &nbsp;&nbsp;
    🧪 {subtotal_liters} L &nbsp;&nbsp;
    📈 ₹ {subtotal_profit:,.0f} profit
  </p>
</div>
""", unsafe_allow_html=True)


            category_value += subtotal_value
            category_liters += subtotal_liters
            category_profit += subtotal_profit

    # 2. List format (CULTIVATEC, GROWTH PROMOTOR, ADDITIONAL['BUD GROW'])
    elif isinstance(products, list):
        for i, product in enumerate(products):
            product_name = product["Product"]
            st.markdown(f"### {product_name}")
            skus = product.get("SKUs") or product.get("SKU")
            prices = product["Unit_Price_per_case"]
            profits = product["Profit"]
            Unit = product.get("Unit", "ml")

            cols = st.columns(len(skus))
            subtotal_value = 0
            subtotal_liters = 0
            subtotal_profit = 0

            for j, sku in enumerate(skus):
                with cols[j]:
                    qty = st.number_input(f"{sku} {Unit} cases", min_value=0, step=1, key=f"{category}_{i}_sku{sku}")
                    liters = qty * CASE_VOLUME_LITERS
                    value = qty * prices[j]
                    profit = qty * profits[j]

                    st.markdown(f"₹ {value:,.0f} | {liters} L")
                    subtotal_value += value
                    subtotal_liters += liters
                    subtotal_profit += profit

            if subtotal_value > 0:
                order_list.append({
                    "Category": category,
                    "Product": product_name,
                    "Quantity (cases total)": subtotal_liters / CASE_VOLUME_LITERS,
                    "Subtotal Value (₹)": subtotal_value,
                    "Subtotal Liters": subtotal_liters,
                    "Subtotal Profit (₹)": subtotal_profit
                })

            st.markdown(f"**Subtotal: ₹ {subtotal_value:,.0f} | {subtotal_liters} L | ₹ {subtotal_profit:,.0f} profit**")
            st.markdown("---")

            category_value += subtotal_value
            category_liters += subtotal_liters
            category_profit += subtotal_profit

    # Show subtotals for category
    st.markdown(f"""
<div style="border-radius: 10px; background-color: #E8F5E9; padding: 15px; margin: 10px 0;">
  <h4 style="color:#1B5E20; margin-bottom: 0;">{category.title()} Total</h4>
  <p style="margin-top: 5px;"><strong>Sales:</strong> ₹ {category_value:,.0f} &nbsp;&nbsp; | &nbsp;&nbsp;
     <strong>Volume:</strong> {category_liters} L &nbsp;&nbsp; | &nbsp;&nbsp;
     <strong>Margin:</strong> ₹ {category_profit:,.0f}</p>
</div>
""", unsafe_allow_html=True)

    total_value += category_value
    total_liters += category_liters
    total_profit += category_profit

# Final Summary
st.markdown(f"# 🧾 Grand Total: ₹ {total_value:,.0f} | {total_liters} L | ₹ {total_profit:,.0f} Margin")

# Scheme Progress
scheme_progress = total_value / SCHEME_TARGET_SALES * 100
st.markdown(f"### 🎯 Scheme Eligibility Progress: {scheme_progress:.1f}% of ₹3,00,000 Target")

# Conditional Scheme Reward Section
scheme_reward = 88000
if total_value >= 300000:
    st.success("🎉 Congratulations! You're eligible for the full scheme rewards worth ₹88,000.")
    
    with st.expander("💎 Scheme Reward Breakdown"):
        st.markdown("""
        | ✨ Reward Item | Value | Includes |
        |---------------|--------|----------|
        | ✈️ **Foreign Trip** | ₹50,000 | Flight tickets, Hotel |
        | 🪙 **Gold Coin** | ₹8,000 | 1 Gold Bar |
        | 💸 **Advance Payment Discount** | ₹30,000 | Instant Cashback |
        | **Total** | **₹88,000** | 🎁 |
        """, unsafe_allow_html=True)

    total_profit_combined = total_profit + scheme_reward
else:
    st.info("ℹ️ To unlock ₹88,000 in rewards, reach ₹3,00,000 in total purchases.")
    total_profit_combined = total_profit

# Display total profit (margin + scheme)
st.markdown(f"## 💼 Total Profit ({total_profit} + 88,000): ₹ {total_profit_combined:,.0f}")


# Order summary + download
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