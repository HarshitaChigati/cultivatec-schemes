import streamlit as st
from datetime import date
import pandas as pd

# Constants
CASE_VOLUME_LITERS = 12
SCHEME_TARGET_SALES = 300000
SCHEME_REWARD_AMOUNT = 90000
#total_rhody_grams = 0

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
        "Overview": ["📏 No. of Acres Recommendation:", "👨‍🌾 No. of Farmers Purchased:", "Note: Average acres per farmer is considered to be 3 acres."],
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
        "Crops": ["🌶️Suitable for all crops🌾"]
    },

    "Tetrapower": {
        "Overview": ["📏 No. of Acres Recommendation:", "👨‍🌾 No. of Farmers Purchased:", "Note: Average acres per farmer is considered to be 3 acres."],
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
        "Crops": ["🌶️Suitable for all crops🌾"]
    },

    "K-Bio": {
        "Overview": ["📏 No. of Acres Recommendation:", "👨‍🌾 No. of Farmers Purchased:", "Note: Average acres per farmer is considered to be 3 acres."],
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
        "Crops": ["🌶️Suitable for all crops🌾"]
    },

    "Calratna": {
        "Overview": ["📏 No. of Acres Recommendation:", "👨‍🌾 No. of Farmers Purchased:", "Note: Average acres per farmer is considered to be 3 acres."],
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
        "Crops": ["🌶️Suitable for all crops🌾"]
    },

    "Rhody Potash": {
        "Overview": ["📏 No. of Acres Recommendation:", "👨‍🌾 No. of Farmers Purchased:", "Note: Average acres per farmer is considered to be 3 acres."],
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
        "Crops": ["🌶️Suitable for all crops🌾"]
    },

    "Black Diamond": {
        "Overview": ["📏 No. of Acres Recommendation:", "👨‍🌾 No. of Farmers Purchased:", "Note: Average acres per farmer is considered to be 3 acres."],
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
        "Crops": ["🌶️Suitable for all crops🌾"]
    },

    "Gly-Zinc": {
        "Overview": ["📏 No. of Acres Recommendation:", "👨‍🌾 No. of Farmers Purchased:", "Note: Average acres per farmer is considered to be 3 acres."],
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
        "Crops": ["🌶️Suitable for all crops🌾"]
    },

    "Harvester": {
        "Overview": ["📏 No. of Acres Recommendation:", "👨‍🌾 No. of Farmers Purchased:", "Note: Average acres per farmer is considered to be 3 acres."],
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
        "Crops": ["🌶️Suitable for all crops🌾"]
    },

    "Gainup": {
        "Overview": ["📏 No. of Acres Recommendation:", "👨‍🌾 No. of Farmers Purchased:", "Note: Average acres per farmer is considered to be 3 acres."],
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
        "Crops": ["🌶️Suitable for all crops🌾"]
    }
}

# Product List
products = [
    {"Name": "Nemarid", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Nemarid.jpg?raw=true", "Type": "case", 
     "Highlight": "A soil conditioner that boosts soil health & fertility and Fights Nematodes",
     "SKUs": [
        {"Label": "250 ml", "Dealer Price": 16128, "Profit": 6576},
        {"Label": "500 ml", "Dealer Price": 15456, "Profit": 5976},
    ]},
    {"Name": "Tetrapower", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Tetrapower?raw=true", "Type": "case",
     "Highlight": "Activates Potassium, Phosphorus, Magnesium, and Zinc in the soil, making them bio-available for plant uptake.",
      "SKUs": [
        {"Label": "250 ml", "Dealer Price": 18576, "Profit": 4128},
    ]},
    {"Name": "K-Bio", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/K-Bio?raw=true", "Type": "case", 
     "Highlight": "Activates Potassium in soil and makes it 100% available for plant absorption.",
     "SKUs": [
        {"Label": "250 ml", "Dealer Price": 18096, "Profit": 4608},
    ]},
    {"Name": "Calratna", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Calratna?raw=true", "Type": "case", 
     "Highlight": "Converts soil-bound Calcium into a bio-available form for plant uptake.",
     "SKUs": [
        {"Label": "250 ml", "Dealer Price": 14640, "Profit": 5520},
    ]},
    {"Name": "Gainup", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Gainup?raw=true", "Type": "case", 
     "Highlight": "Gainup unlocks Zinc from the soil and enhances its availability for effective plant absorption.",
     "SKUs": [
        {"Label": "250 ml", "Dealer Price": 14112, "Profit": 6048},
    ]},
    {"Name": "Harvester", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Harvester?raw=true", "Type": "case", 
     "Highlight": "Harvester enhances Boron availability in the soil, supporting better flower, fruit, and seed development.",
     "SKUs": [
        {"Label": "250 ml", "Dealer Price": 18576, "Profit": 4128},
    ]},
    {"Name": "Rhody Potash", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Rhody%20Potash?raw=true", "Type": "unit", "Unit": "gms", "Size": 150, "Unit Value": 413, "Unit Profit": 262,
     "Highlight": "Rhody Potash is a red seaweed-based potash supplement that enhances nutrient uptake and boosts plant resilience.",},
    {"Name": "Gly-Zinc", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Gly%20Zn.png?raw=true", "Type": "unit", "Unit": "ml", "Size": 250, "Unit Value": 167, "Unit Profit": 183,
     "Highlight": "Gly-Zn is a Zinc-Glycine-based chelated micronutrient that ensures efficient zinc absorption and utilization by plants.",},
    {"Name": "Black Diamond", "Image": "https://github.com/HarshitaChigati/cultivatec-schemes/blob/dbb8d3a28dddbffc341a1f0615cf7a52d8fa895a/Black%20Diamond?raw=true", "Type": "unit", "Unit": "ml", "Size": 500, "Unit Value": 599, "Unit Profit": 201,
     "Highlight": "A plant growth promoter enriched with fulvic acid, humic acid, and organic carbon – for healthier soil and vigorous plant growth.",},
]

# Tracking totals
order_list = []
total_value = 0
total_liters = 0
total_profit = 0

for product in products:
    col_img, col_desc = st.columns([1, 3])  # Image on the left, text on the right

    with col_img:
        st.image(product["Image"], width=140)

    with col_desc:
        st.markdown(f"### 🌿 {product['Name']}")
        st.markdown(f"""
    <p style='font-size:18px; font-weight:600; color:#B8860B; margin-top: 18px;'>
        {product.get('Highlight', '')}
    </p>
""", unsafe_allow_html=True)


    subtotal_value = 0
    subtotal_volume = 0
    subtotal_profit = 0

    if product["Type"] == "case":
        cols = st.columns(len(product["SKUs"]))
        for i, sku in enumerate(product["SKUs"]):
            with cols[i]:
                st.markdown(f"<p style='font-size:18px; font-weight:600;'>No. Of Cases – {sku['Label']}</p>", unsafe_allow_html=True)
                qty = st.number_input("", min_value=0, step=1, key=f"{product['Name']}_{sku['Label']}")

                liters = qty * CASE_VOLUME_LITERS
                value = qty * sku["Dealer Price"]
                profit = qty * sku["Profit"]
                subtotal_value += value
                subtotal_volume += liters
                subtotal_profit += profit

    elif product["Type"] == "unit":
        label = f"{product['Size']} {product['Unit']}"
        st.markdown(f"<p style='font-size:18px; font-weight:600;'>No. of Packs – {label}</p>", unsafe_allow_html=True)
        qty = st.number_input("", min_value=0, step=1, key=product['Name'])
        value = qty * product["Unit Value"]
        profit = qty * product["Unit Profit"]

        if product["Unit"] == "ml":
            volume = qty * product["Size"] / 1000  # ml to liters
        else:
            volume = qty * product["Size"]

#        if product["Name"] == "Rhody Potash":
#            total_rhody_grams += volume

        subtotal_value += value
        subtotal_volume += volume
        subtotal_profit += profit

    volume_unit = "L" if product.get("Unit") != "gms" else "g"
    st.markdown(f"""
<div style="display: flex; justify-content: center;">
  <div style="background-color: #F1F8E9; padding: 10px 20px; border-radius: 10px; margin-top: 10px; border-left: 6px solid #4CAF50; text-align: center; max-width: 500px;">
    <p style="margin: 0; font-weight: 600; color: #2E7D32; font-size: 16px;">
      💰 <span style='font-size: 18px;'>Sales:</span> 
      ₹ <span style='font-size: 18px;'>{subtotal_value:,.0f}</span> &nbsp;&nbsp;
      🧪 Qty: {subtotal_volume} {volume_unit} &nbsp;&nbsp;
      📈 ₹ {subtotal_profit:,.0f} profit
    </p>
  </div>
</div>
""", unsafe_allow_html=True)


    # ✅ Insert the following block here:
    if product["Name"] in product_info_data:
        with st.expander("📘 Product Usage & Benefits"):
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
#if total_rhody_grams > 0:
#    volume_display += f" + {total_rhody_grams:.0f} Gms"

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

# Calculate scheme multiplier
scheme_multiplier = total_value // SCHEME_TARGET_SALES  # For every ₹3L

# Updated reward values based on multiplier
trip_value = 50000 * scheme_multiplier
coin_value = 9000 * scheme_multiplier
discount_value = 21000 * scheme_multiplier
total_scheme_rewards = SCHEME_REWARD_AMOUNT * scheme_multiplier

scheme_multiplier = total_value // SCHEME_TARGET_SALES
total_scheme_rewards = SCHEME_REWARD_AMOUNT * scheme_multiplier
total_profit_combined = total_profit + total_scheme_rewards
# Only show success message if eligible
if total_value >= SCHEME_TARGET_SALES:
    st.success(f"🎉 Congratulations! You're eligible for scheme rewards worth ₹{total_scheme_rewards:,.0f}.")
else:
    st.info(f"ℹ️ To unlock ₹90,000 in rewards, reach ₹3,00,000 in total purchases.")

#Grand Total
st.markdown(f"""
<div style='text-align: center; margin-top: 20px;'>
  <p style='font-size: 18px; color: #FFD700; font-weight: 400; background-color: #800000; padding: 10px 20px; border-radius: 8px; display: inline-block; box-shadow: 0 2px 6px rgba(0,0,0,0.08);'>
    🧾 Total Sales: ₹ {total_value:,.0f} &nbsp;&nbsp;|&nbsp;&nbsp; 🧪 Total Quantity {volume_display} &nbsp;&nbsp;|&nbsp;&nbsp; 📈 Total Profit: ₹ {total_profit:,.0f}
  </p>
</div>
""", unsafe_allow_html=True)

# Calculate scheme multiplier (integer division)
scheme_multiplier = total_value // SCHEME_TARGET_SALES

# Rewards calculation based on multiplier
trip_value = 50000 * scheme_multiplier
coin_value = 9000 * scheme_multiplier
discount_value = 21000 * scheme_multiplier
total_scheme_rewards = SCHEME_REWARD_AMOUNT * scheme_multiplier

# Combined profit only when eligible
total_profit_combined = total_profit + total_scheme_rewards if total_value >= SCHEME_TARGET_SALES else 0

# Display values (these control what’s shown on the screen)
display_trip_value = 50000 if scheme_multiplier == 0 else trip_value
display_coin_value = 9000 if scheme_multiplier == 0 else coin_value
display_discount_value = 21000 if scheme_multiplier == 0 else discount_value
display_total_scheme_rewards = 90000 if scheme_multiplier == 0 else total_scheme_rewards

current_slab = int(scheme_multiplier)
if "last_scheme_slab" not in st.session_state:
    st.session_state.last_scheme_slab = 0

if current_slab > st.session_state.last_scheme_slab:
    st.session_state.last_scheme_slab = current_slab

    # Optional visual effect
    st.balloons()  # or st.snow() for variety

    # Optional: show a message
    st.success(f"🎉 You unlocked a new scheme slab worth ₹{current_slab * SCHEME_REWARD_AMOUNT:,.0f}!")

    # Play sound
    st.markdown("""
    <audio autoplay>
        <source src="https://www.soundjay.com/human/cheering-01.mp3" type="audio/mpeg">
    </audio>
    """, unsafe_allow_html=True)


st.markdown(f"""
<style>
@keyframes glow {{
  0% {{ box-shadow: 0 0 5px #FFD700; }}
  50% {{ box-shadow: 0 0 20px #FFD700; }}
  100% {{ box-shadow: 0 0 5px #FFD700; }}
}}
.reward-table {{
    border-collapse: collapse;
    width: 100%;
    font-size: 16px;
    color: #444;
}}
.reward-table th, .reward-table td {{
    padding: 10px 12px;
    border-bottom: 1px solid #ddd;
}}
.reward-table thead {{
    background-color: #f1f8e9;
    color: #1B5E20;
    font-weight: bold;
}}
.glow-row {{
    animation: glow 2s infinite;
    border: 2px solid #FFD700;
    background-color: #FFF8E1;
    color: #4E342E;
    font-weight: bold;
}}
</style>

<h3>💎 Scheme Reward Breakdown</h3>

<table class="reward-table">
    <thead>
        <tr>
            <th>✨ Reward Item</th>
            <th>Value</th>
            <th>Includes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>✈️ <b>Foreign Trip</b></td>
            <td>₹{display_trip_value:,.0f}</td>
            <td>Flight tickets, Hotel</td>
        </tr>
        <tr>
            <td>🪙 <b>Gold Coin</b></td>
            <td>₹{display_coin_value:,.0f}</td>
            <td>{max(1, scheme_multiplier)} Gold Coin(s)</td>
        </tr>
        <tr>
            <td>💸 <b>Advance Payment Discount</b></td>
            <td>₹{display_discount_value:,.0f}</td>
            <td>Instant Cashback</td>
        </tr>
        <tr style="font-weight: bold;">
            <td><b>Total Scheme Rewards</b></td>
            <td>₹{display_total_scheme_rewards:,.0f}</td>
            <td>🎁</td>
        </tr>
        {"<tr style='font-weight: bold;'><td>💼 <b>Your Profit from Sales</b></td><td>₹{:,}</td><td>Based on quantity sold</td></tr>".format(total_profit) if total_value >= SCHEME_TARGET_SALES else ""}
        {"<tr class='glow-row'><td style='font-size:18px;'>🧾 <b>Total Profit (including rewards)</b></td><td style='font-size:18px;'>₹{:,}</td><td style='font-size:16px;'>Sales + Scheme</td></tr>".format(total_profit_combined) if total_value >= SCHEME_TARGET_SALES else ""}
    </tbody>
</table>
""", unsafe_allow_html=True)

# Order Summary
if order_list:
    st.header("📄 Order Summary")

    # Create DataFrame with all data (including customer info)
    df = pd.DataFrame(order_list)
    df["Customer Name"] = customer_name
    df["Customer Code"] = customer_code
    df["Order Date"] = order_date

    # For screen display – remove Customer Name & Code
    display_columns = [col for col in df.columns if col not in ["Customer Name", "Customer Code", "Order Date"]]
    st.dataframe(df[display_columns], use_container_width=True)

    # For download – full data including customer info
    csv_data = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="📥 Download order summary as CSV",
        data=csv_data,
        file_name="cultivatec_order_summary.csv",
        mime="text/csv"
    )

else:
    st.info("Add quantities above to see order summary and download option.")
