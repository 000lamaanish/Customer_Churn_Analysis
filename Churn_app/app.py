import streamlit as st
import numpy as np
import joblib
import os

# -----------------------
# PAGE CONFIG (MUST BE FIRST)
# -----------------------
st.set_page_config(
    page_title="ChurnIQ - Customer Analytics",
    page_icon="📉",
    layout="wide"
)

# -----------------------
# LOAD MODEL (FIXED)
# -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "churn_model.pkl")

model = joblib.load(model_path)

# -----------------------
# CUSTOM CSS
# -----------------------
st.markdown("""
<style>

.main {
    background-color: #0f172a;
    color: white;
}

.stSidebar {
    background-color: #111827;
}

h1, h2, h3 {
    color: #38bdf8;
}

.card {
    background-color: #1f2937;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
}

.metric {
    font-size: 20px;
    font-weight: bold;
    color: #22c55e;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# HEADER
# -----------------------
st.title("📉 ChurnIQ Dashboard")
st.markdown("AI-powered customer churn prediction system")

# -----------------------
# SIDEBAR INPUTS
# -----------------------
st.sidebar.header("Customer Profile")

tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
monthly = st.sidebar.slider("Monthly Charges", 0, 150, 70)
total = st.sidebar.slider("Total Charges", 0, 8000, 1000)

contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

payment = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Credit card", "Bank transfer"]
)

# -----------------------
# FEATURE ENGINEERING
# -----------------------
contract_1y = 1 if contract == "One year" else 0
contract_2y = 1 if contract == "Two year" else 0

fiber = 1 if internet == "Fiber optic" else 0
no_internet = 1 if internet == "No" else 0

electronic = 1 if payment == "Electronic check" else 0
mailed = 1 if payment == "Mailed check" else 0
credit = 1 if payment == "Credit card" else 0

# -----------------------
# INPUT ARRAY
# -----------------------
input_data = np.array([[
    tenure,
    monthly,
    total,
    contract_1y,
    contract_2y,
    fiber,
    no_internet,
    electronic,
    mailed,
    credit
]])

# -----------------------
# PREDICTION
# -----------------------
if st.button("🚀 Analyze Customer Risk"):

    prob = model.predict_proba(input_data)[0][1]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
            <h3>Churn Probability</h3>
            <p class="metric">{prob:.2%}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        risk_level = "Low" if prob < 0.3 else "Medium" if prob < 0.6 else "High"
        st.markdown(f"""
        <div class="card">
            <h3>Risk Level</h3>
            <p class="metric">{risk_level}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        status = "Retain" if prob < 0.5 else "At Risk"
        st.markdown(f"""
        <div class="card">
            <h3>Recommendation</h3>
            <p class="metric">{status}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📊 Risk Breakdown")
    st.progress(int(prob * 100))

    if prob < 0.3:
        st.success("Customer is stable.")
    elif prob < 0.6:
        st.warning("Moderate churn risk.")
    else:
        st.error("High churn risk!")

# -----------------------
# FOOTER
# -----------------------
st.markdown("---")
st.markdown("ChurnIQ • ML Powered Dashboard")