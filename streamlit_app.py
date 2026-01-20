import streamlit as st

# Function containing your updated auction logic
def calculate_total_cost(bid_price, title_status):
    # Updated fee structures based on your latest list
    title_fees = {
        'clean': [
            (0, 49.99, 1.00), (50.00, 99.99, 1.00), (100.00, 199.99, 25.00), 
            (200.00, 299.99, 50.00), (300.00, 349.99, 75.00), (350.00, 399.99, 75.00), 
            (400.00, 449.99, 110.00), (450.00, 499.99, 110.00), (500.00, 549.99, 125.00), 
            (550.00, 599.99, 130.00), (600.00, 699.99, 140.00), (700.00, 799.99, 155.00), 
            (800.00, 899.99, 170.00), (900.00, 999.99, 185.00), (1000.00, 1199.99, 200.00), 
            (1200.00, 1299.99, 225.00), (1300.00, 1399.99, 240.00), (1400.00, 1499.99, 250.00), 
            (1500.00, 1599.99, 260.00), (1600.00, 1699.99, 275.00), (1700.00, 1799.99, 285.00), 
            (1800.00, 1999.99, 300.00), (2000.00, 2399.99, 325.00), (2400.00, 2499.99, 335.00), 
            (2500.00, 2999.99, 350.00), (3000.00, 3499.99, 400.00), (3500.00, 3999.99, 455.00), 
            (4000.00, 4499.99, 600.00), (4500.00, 4999.99, 625.00), (5000.00, 5499.99, 625.00), 
            (5500.00, 5999.99, 625.00), (6000.00, 6499.99, 675.00), (6500.00, 6999.99, 675.00), 
            (7000.00, 7499.99, 675.00), (7500.00, 7999.99, 690.00), (8000.00, 8499.99, 715.00), 
            (8500.00, 8999.99, 715.00), (9000.00, 9999.99, 715.00), (10000.00, 10499.99, 720.00), 
            (10500.00, 10999.99, 720.00), (11000.00, 11499.99, 720.00), (11500.00, 11999.99, 720.00), 
            (12000.00, 12499.99, 720.00), (12500.00, 14999.99, 720.00), (15000, float('inf'), 0.0575)
        ],
        'non': [
            (0, 49.99, 1.00), (50.00, 99.99, 1.00), (100.00, 199.99, 25.00), 
            (200.00, 299.99, 60.00), (300.00, 349.99, 85.00), (350.00, 399.99, 100.00), 
            (400.00, 449.99, 125.00), (450.00, 499.99, 135.00), (500.00, 549.99, 145.00), 
            (550.00, 599.99, 155.00), (600.00, 699.99, 170.00), (700.00, 799.99, 195.00), 
            (800.00, 899.99, 215.00), (900.00, 999.99, 230.00), (1000.00, 1199.99, 250.00), 
            (1200.00, 1299.99, 270.00), (1300.00, 1399.99, 285.00), (1400.00, 1499.99, 300.00), 
            (1500.00, 1599.99, 315.00), (1600.00, 1699.99, 330.00), (1700.00, 1799.99, 350.00), 
            (1800.00, 1999.99, 370.00), (2000.00, 2399.99, 390.00), (2400.00, 2499.99, 425.00), 
            (2500.00, 2999.99, 460.00), (3000.00, 3499.99, 505.00), (3500.00, 3999.99, 555.00), 
            (4000.00, 4499.99, 600.00), (4500.00, 4999.99, 625.00), (5000.00, 5499.99, 650.00), 
            (5500.00, 5999.99, 675.00), (6000.00, 6499.99, 700.00), (6500.00, 6999.99, 720.00), 
            (7000.00, 7499.99, 755.00), (7500.00, 7999.99, 775.00), (8000.00, 8499.99, 800.00), 
            (8500.00, 8999.99, 820.00), (9000.00, 9999.99, 820.00), (10000.00, 10499.99, 850.00), 
            (10500.00, 10999.99, 850.00), (11000.00, 11499.99, 850.00), (11500.00, 11999.99, 860.00), 
            (12000.00, 12499.99, 875.00), (12500.00, 14999.99, 890.00), (15000, float('inf'), 0.06)
        ]
    }

    live_bid_fees = [
        (0, 99.99, 0), (100.00, 499.99, 49.00), (500.00, 999.99, 59.00), 
        (1000.00, 1499.99, 79.00), (1500.00, 1999.99, 89.00), (2000.00, 3999.99, 99.00), 
        (4000.00, 5999.99, 109.00), (6000.00, 7999.99, 139.00), (8000, float('inf'), 149.00)
    ]

    # Calculate Title Fee
    title_fee = 0
    for start, end, fee in title_fees[title_status]:
        if start <= bid_price <= end:
            title_fee = bid_price * fee if bid_price >= 15000 else fee
            break

    # Calculate Live Bid Fee
    v_fee = next((f for s, e, f in live_bid_fees if s <= bid_price <= e), 0)

    # Updated Gate, Env, and Mail Fees
    gate_f = 79.00 if title_status == 'clean' else 95.00
    env_f = 0.00 if title_status == 'clean' else 15.00
    mail_f = 15.00  # Updated from $20 to $15

    total = bid_price + title_fee + v_fee + gate_f + env_f + mail_f
    return total, title_fee, v_fee, gate_f, env_f, mail_f

# --- Streamlit Interface ---
st.set_page_config(page_title="Copart Estimator", layout="centered")

# Branding Sidebar
with st.sidebar:
    st.title("👤 App Owner")
    st.header("Hamza Albernawi")
    st.write("Auction Price Specialist")
    st.divider()
    st.info("Updated with Jan 2026 Copart Fee Schedule.")

st.title("🚗 Copart Bid Estimator")
st.caption("Developed by Hamza")

# Input Section
bid = st.number_input("Final Bid Price ($)", min_value=0.0, value=5000.0, step=100.0)
status = st.selectbox("Title Status", ["Clean", "Non-Clean"]).lower()
if status == "non-clean": status = "non"

dealer_fees = st.number_input("Dealer Fees ($)", value=150.0)
towing_fees = st.number_input("Towing Fees ($)", value=120.0)

if st.button("Calculate Total"):
    total_auc, t_f, v_f, g_f, e_f, m_f = calculate_total_cost(bid, status)
    grand_total = total_auc + dealer_fees + towing_fees
    
    st.divider()
    st.metric("GRAND TOTAL (ALL-IN)", f"${grand_total:,.2f}")
    
    with st.expander("Detailed Fee Breakdown"):
        st.write(f"**Final Bid:** ${bid:,.2f}")
        st.write(f"**Auction Buy Fee:** ${t_f:,.2f}")
        st.write(f"**Live Bid Fee:** ${v_f:.2f}")
        st.write(f"**Gate Fee:** ${g_f:.2f}")
        st.write(f"**Environmental Fee:** ${e_f:.2f}")
        st.write(f"**Mailing Fee:** ${m_f:.2f}")
        st.divider()
        st.write(f"**Other Fees (Dealer/Towing):** ${dealer_fees + towing_fees:.2f}")
