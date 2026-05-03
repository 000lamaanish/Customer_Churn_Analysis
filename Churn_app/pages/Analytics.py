import streamlit as st
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="Churn Analytics",
    layout="wide",
    page_icon="📊"
)

st.title("📊 Customer Churn Analytics Dashboard")
st.caption("Understand customer behavior and churn patterns")

# -----------------------
# FIXED PATH (YOUR STRUCTURE)
# -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # pages/
APP_DIR = os.path.dirname(BASE_DIR)                      # Churn_app/
ROOT_DIR = os.path.dirname(APP_DIR)                      # customerchurnanalysis/

data_path = os.path.join(
    ROOT_DIR,
    "notebook",
    "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# -----------------------
# LOAD DATA
# -----------------------
df = pd.read_csv(data_path)

# -----------------------
# BASIC CLEANING
# -----------------------
df.drop("customerID", axis=1, inplace=True)

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)

# -----------------------
# KPI SECTION
# -----------------------
st.markdown("## 📌 Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Customers", len(df))

with col2:
    churn_rate = df["Churn"].value_counts(normalize=True)["Yes"]
    st.metric("Churn Rate", f"{churn_rate:.2%}")

with col3:
    st.metric("Avg Monthly Charges", f"${df['MonthlyCharges'].mean():.2f}")

st.markdown("---")

# -----------------------
# CHURN DISTRIBUTION
# -----------------------
st.subheader("📉 Churn Distribution")

fig, ax = plt.subplots()
sns.countplot(x="Churn", data=df, ax=ax)
st.pyplot(fig)

# -----------------------
# CONTRACT VS CHURN
# -----------------------
st.subheader("📄 Contract Type vs Churn")

fig, ax = plt.subplots(figsize=(6,4))
sns.countplot(x="Contract", hue="Churn", data=df, ax=ax)
st.pyplot(fig)

# -----------------------
# TENURE ANALYSIS
# -----------------------
st.subheader("⏳ Tenure vs Churn")

fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(x="Churn", y="tenure", data=df, ax=ax)
st.pyplot(fig)

# -----------------------
# MONTHLY CHARGES
# -----------------------
st.subheader("💰 Monthly Charges vs Churn")

fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(x="Churn", y="MonthlyCharges", data=df, ax=ax)
st.pyplot(fig)

# -----------------------
# FILTER SECTION
# -----------------------
st.markdown("---")
st.subheader("🔍 Interactive Data Explorer")

contract_filter = st.selectbox(
    "Filter by Contract Type",
    ["All"] + list(df["Contract"].unique())
)

if contract_filter != "All":
    filtered_df = df[df["Contract"] == contract_filter]
else:
    filtered_df = df

st.dataframe(filtered_df.head(20))

# -----------------------
# FOOTER
# -----------------------
st.markdown("---")
st.caption("ChurnIQ Analytics • Built with Streamlit + Machine Learning")