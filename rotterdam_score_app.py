import streamlit as st

st.title("Rotterdam Score for Acute Budd-Chiari Syndrome")

# Inputs
he = st.radio("Hepatic encephalopathy present?", ["no", "yes"])
ascites = st.radio("Ascites present?", ["no", "yes"])
inr = st.number_input("Enter INR", min_value=0.0, step=0.1)
bilirubin = st.number_input("Enter bilirubin (µmol/L)", min_value=0.0, step=1.0)

# Logic
he_score = 1 if he == "yes" else 0
ascites_score = 1 if ascites == "yes" else 0
inr_score = 1 if inr > 2.3 else 0

rotterdam = (1.27 * he_score) + (1.04 * ascites_score) + (0.72 * inr_score) + (0.004 * bilirubin)

# Output
if st.button("Calculate Rotterdam Score"):
    st.success(f"Rotterdam Score: {rotterdam:.2f}")
    st.caption("Formula: (1.27 × HE) + (1.04 × Ascites) + (0.72 × INR indicator) + (0.004 × Bilirubin in µmol/L)")