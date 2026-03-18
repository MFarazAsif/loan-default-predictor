import streamlit as st
import requests

st.set_page_config(
    page_title="Loan Default Predictor",
    page_icon="bank",
    layout="wide"
)

st.title("AI Loan Default Predictor")
st.markdown("Enter applicant details to predict default risk")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Loan Details")
    loan_amnt = st.slider("Loan Amount ($)", 1000, 35000, 10000)
    int_rate = st.slider("Interest Rate (%)", 5.0, 30.0, 12.0)
    installment = st.slider("Monthly Installment ($)", 50, 1400, 300)

with col2:
    st.subheader("Applicant Profile")
    annual_inc = st.slider("Annual Income ($)", 10000, 500000, 65000)
    dti = st.slider("Debt to Income Ratio", 0.0, 50.0, 15.0)
    fico_low = st.slider("FICO Score", 580, 850, 680)

with col3:
    st.subheader("Credit History")
    open_acc = st.slider("Open Accounts", 1, 40, 8)
    revol_bal = st.slider("Revolving Balance ($)", 0, 100000, 10000)
    revol_util = st.slider("Revolving Utilization (%)", 0.0, 100.0, 45.0)
    total_acc = st.slider("Total Accounts", 1, 80, 20)
    mort_acc = st.slider("Mortgage Accounts", 0, 10, 1)
    pub_rec = st.slider("Public Records", 0, 5, 0)

if st.button("Predict Default Risk", type="primary"):
    payload = {
        "loan_amnt": loan_amnt,
        "int_rate": int_rate,
        "installment": installment,
        "annual_inc": annual_inc,
        "dti": dti,
        "fico_range_low": fico_low,
        "fico_range_high": fico_low + 4,
        "open_acc": open_acc,
        "revol_bal": revol_bal,
        "revol_util": revol_util,
        "total_acc": total_acc,
        "mort_acc": mort_acc,
        "pub_rec": pub_rec
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = response.json()

        st.divider()
        col_a, col_b, col_c = st.columns(3)

        with col_a:
            st.metric("Default Probability", f"{result['default_probability']}%")
        with col_b:
            st.metric("Risk Level", result['risk_level'])
        with col_c:
            st.metric("Recommendation", result['recommendation'])

        if result['default_prediction'] == 1:
            st.error("HIGH RISK — This applicant is likely to default")
        else:
            st.success("LOW RISK — This applicant is likely to repay")

    except Exception as e:
        st.error(f"API not running. Start the API first. Error: {e}")