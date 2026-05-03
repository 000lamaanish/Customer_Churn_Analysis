import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="Churn Prediction",
    layout="wide"
)

# -----------------------
# LOAD MODEL
# -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../churn_model.pkl")

model = joblib.load(model_path)

# -----------------------
# HEADER
# -----------------------
st.title("🔮 Customer Churn Prediction")
st.caption("Predict whether a customer is likely to churn")

# -----------------------
# SIDEBAR INPUTS
# -----------------------
st.sidebar.header("Customer Profile")

tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
monthly = st.sidebar.slider("Monthly Charges", 0, 150, 70)
total = st.sidebar.slider("Total Charges", 0, 8000, 1000)

contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

internet = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

payment = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Credit card (automatic)", "Bank transfer (automatic)"]
)

paperless = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
security = st.sidebar.selectbox("Online Security", ["Yes", "No", "No internet service"])
tech = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])
protection = st.sidebar.selectbox("Device Protection", ["Yes", "No", "No internet service"])

# -----------------------
# INPUT DATA
# -----------------------
input_df = pd.DataFrame([{
    "TotalCharges": total,
    "tenure": tenure,
    "MonthlyCharges": monthly,
    "Contract": contract,
    "InternetService": internet,
    "PaymentMethod": payment,
    "PaperlessBilling": paperless,
    "OnlineSecurity": security,
    "TechSupport": tech,
    "DeviceProtection": protection
}])

# -----------------------
# PREDICTION
# -----------------------
if st.button("🚀 Predict Churn"):

    prob = model.predict_proba(input_df)[0][1]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Churn Probability", f"{prob:.2%}")

    with col2:
        risk = "Low" if prob < 0.3 else "Medium" if prob < 0.6 else "High"
        st.metric("Risk Level", risk)

    with col3:
        action = "Retain" if prob < 0.5 else "At Risk"
        st.metric("Recommendation", action)

    st.progress(int(prob * 100))

    if prob < 0.3:
        st.success("Customer is stable.")
    elif prob < 0.6:
        st.warning("Customer shows churn signals.")
    else:
        st.error("High churn risk detected!")