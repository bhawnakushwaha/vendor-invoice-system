import streamlit as st
import pandas as pd
import plotly.express as px

from inference.predict_freight import predict_freight_cost
from inference.predict_invoice_flag import predict_invoice_flag

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="📦",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>

.main-title {
    font-size:42px;
    font-weight:700;
    color:#1f4e79;
}

.subtitle {
    font-size:20px;
    color:#555;
}

.stMetric {
    background-color: #f5f7fa;
    padding: 15px;
    border-radius: 10px;
}

.block-container {
    padding-top: 4rem;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header Section
# -----------------------------
st.markdown('<h2 class="main-title">📦 Vendor Invoice Intelligence Portal</h2>', unsafe_allow_html=True)

st.markdown('<p class="subtitle">AI-Driven Freight Cost Prediction & Invoice Risk Detection</p>', unsafe_allow_html=True)

st.markdown("""
This internal analytics portal helps finance teams:

- 📊 **Forecast freight costs**
- 🚨 **Detect risky vendor invoices**
- ⚡ **Reduce manual approval workload**
""")

st.divider()


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("⚙️ Prediction Modules")

selected_model = st.sidebar.radio(
    "Select Module",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 📈 Business Impact

- Improved cost forecasting  
- Reduced invoice anomalies  
- Faster finance approvals
""")

# =========================================================
# Freight Cost Prediction
# =========================================================
if selected_model == "Freight Cost Prediction":

    st.subheader("🚚 Freight Cost Prediction")

    st.markdown("""
Predict freight cost for a vendor invoice using **Quantity** and **Invoice Dollars**
to support budgeting, forecasting, and vendor negotiations.
""")

    with st.form("freight_form"):

        col1, col2 = st.columns(2)

        with col1:
            quantity = st.number_input(
                "Quantity",
                min_value=1,
                value=1200
            )

        with col2:
            dollars = st.number_input(
                "Invoice Dollars",
                min_value=1.0,
                value=18500.0
            )

        submit_freight = st.form_submit_button("Predict Freight Cost")

    if submit_freight:

        input_data = {
            "Quantity": quantity,
            "Dollars": dollars
        }

        prediction = predict_freight_cost(input_data)['Predicted_Freight']

        st.success("Prediction Completed")

        st.metric(
            label="🚚 Estimated Freight Cost",
            value=f"${prediction[0]:,.2f}"
        )



# =========================================================
# Invoice Risk Prediction
# =========================================================
else:

    st.subheader("🚨 Invoice Manual Approval Prediction")

    st.markdown("""
Predict whether a vendor invoice should be **flagged for manual approval**
based on abnormal cost, freight, or delivery patterns.
""")

    with st.form("invoice_flag_form"):

        col1, col2, col3 = st.columns(3)

        with col1:
            invoice_quantity = st.number_input(
                "Invoice Quantity",
                min_value=1,
                value=50
            )

            freight = st.number_input(
                "Freight Cost",
                min_value=0.0,
                value=1.73
            )

        with col2:
            invoice_dollars = st.number_input(
                "Invoice Dollars",
                min_value=1.0,
                value=352.92
            )

            total_item_quantity = st.number_input(
                "Total Item Quantity",
                min_value=1,
                value=162
            )

        with col3:
            total_item_dollars = st.number_input(
                "Total Item Dollars",
                min_value=1.0,
                value=2476.0
            )

        submit_flag = st.form_submit_button("Evaluate Invoice Risk")

    if submit_flag:

        input_data = {
            "invoice_quantity": [invoice_quantity],
            "invoice_dollars": [invoice_dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        }

        flag_prediction = predict_invoice_flag(input_data)['Predicted_Flag']

        is_flagged = bool(flag_prediction[0])

        if is_flagged:
            st.error("🚨 Invoice requires **Manual Approval**")
        else:
            st.success("✅ Invoice is **Safe for Auto-Approval**")

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption("Internal AI Tool • Finance Analytics • Built with Streamlit")

