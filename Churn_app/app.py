# import streamlit as st
# import pandas as pd
# import joblib
# import os

# # -----------------------
# # PAGE CONFIG
# # -----------------------
# st.set_page_config(
#     page_title="ChurnIQ Dashboard",
#     layout="wide",
#     page_icon="📉"
# )

# # -----------------------
# # LOAD MODEL
# # -----------------------
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# model_path = os.path.join(BASE_DIR, "churn_model.pkl")
# model = joblib.load(model_path)

# # -----------------------
# # CUSTOM CSS (PRO LOOK)
# # -----------------------
# st.markdown("""
# <style>

# body {
#     background-color: #0f172a;
# }

# .main {
#     background-color: #0f172a;
#     color: white;
# }

# section[data-testid="stSidebar"] {
#     background-color: #111827;
# }

# h1, h2, h3 {
#     color: #38bdf8;
# }

# /* Cards */
# .card {
#     background: #1f2937;
#     padding: 20px;
#     border-radius: 15px;
#     box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
# }

# /* Metric */
# .metric {
#     font-size: 28px;
#     font-weight: bold;
#     color: #22c55e;
# }

# /* Labels */
# .label {
#     font-size: 14px;
#     color: #94a3b8;
# }

# </style>
# """, unsafe_allow_html=True)

# # -----------------------
# # HEADER
# # -----------------------
# st.title("📉 ChurnIQ Analytics Platform")
# st.caption("AI-powered customer churn intelligence dashboard")

# # -----------------------
# # SIDEBAR INPUT
# # -----------------------
# st.sidebar.header("Customer Profile")

# tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
# monthly = st.sidebar.slider("Monthly Charges", 0, 150, 70)
# total = st.sidebar.slider("Total Charges", 0, 8000, 1000)

# contract = st.sidebar.selectbox(
#     "Contract",
#     ["Month-to-month", "One year", "Two year"]
# )

# internet = st.sidebar.selectbox(
#     "Internet Service",
#     ["DSL", "Fiber optic", "No"]
# )

# payment = st.sidebar.selectbox(
#     "Payment Method",
#     ["Electronic check", "Mailed check", "Credit card (automatic)", "Bank transfer (automatic)"]
# )

# paperless = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
# security = st.sidebar.selectbox("Online Security", ["Yes", "No", "No internet service"])
# tech = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])
# protection = st.sidebar.selectbox("Device Protection", ["Yes", "No", "No internet service"])

# # -----------------------
# # INPUT DATA
# # -----------------------
# input_df = pd.DataFrame([{
#     "TotalCharges": total,
#     "tenure": tenure,
#     "MonthlyCharges": monthly,
#     "Contract": contract,
#     "InternetService": internet,
#     "PaymentMethod": payment,
#     "PaperlessBilling": paperless,
#     "OnlineSecurity": security,
#     "TechSupport": tech,
#     "DeviceProtection": protection
# }])

# # -----------------------
# # MAIN ACTION
# # -----------------------
# st.markdown("## 📊 Churn Risk Analysis")

# if st.button("🚀 Run Analysis"):

#     prob = model.predict_proba(input_df)[0][1]

#     # -----------------------
#     # KPI CARDS
#     # -----------------------
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.markdown(f"""
#         <div class="card">
#             <div class="label">Churn Probability</div>
#             <div class="metric">{prob:.2%}</div>
#         </div>
#         """, unsafe_allow_html=True)

#     with col2:
#         risk = "Low" if prob < 0.3 else "Medium" if prob < 0.6 else "High"
#         st.markdown(f"""
#         <div class="card">
#             <div class="label">Risk Level</div>
#             <div class="metric">{risk}</div>
#         </div>
#         """, unsafe_allow_html=True)

#     with col3:
#         action = "Retain" if prob < 0.5 else "At Risk"
#         st.markdown(f"""
#         <div class="card">
#             <div class="label">Recommendation</div>
#             <div class="metric">{action}</div>
#         </div>
#         """, unsafe_allow_html=True)

#     # -----------------------
#     # PROGRESS BAR
#     # -----------------------
#     st.markdown("### 📈 Risk Score")
#     st.progress(int(prob * 100))

#     # -----------------------
#     # INSIGHT SECTION
#     # -----------------------
#     st.markdown("### 🧠 AI Insights")

#     if prob < 0.3:
#         st.success("Customer shows strong retention signals. Maintain engagement.")
#     elif prob < 0.6:
#         st.warning("Customer may churn. Offer discounts or engagement strategies.")
#     else:
#         st.error("High churn risk detected. Immediate intervention recommended.")

# # -----------------------
# # FOOTER
# # -----------------------
# st.markdown("---")
# st.caption("ChurnIQ • Built with Machine Learning • 2026")
import streamlit as st

st.set_page_config(layout="wide")

st.title("📉 ChurnIQ Platform")
st.markdown("""
Welcome to ChurnIQ 🚀  

Use the sidebar to navigate:

📊 Analytics → Understand customer behavior  
🔮 Prediction → Predict churn risk  
""")