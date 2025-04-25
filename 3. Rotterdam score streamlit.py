import streamlit as st

st.title("Rotterdam Score Calculator for Budd-Chiari Syndrome")

he = st.selectbox("Hepatic Encephalopathy (HE)", ["Absent", "Present"])
ascites = st.selectbox("Ascites", ["Absent", "Present"])
inr = st.number_input("INR", min_value=0.0, step=0.1)
bilirubin = st.number_input("Bilirubin (μmol/L)", min_value=0.0, step=1.0)

# Convert inputs to score components
he_val = 1 if he == "Present" else 0
ascites_val = 1 if ascites == "Present" else 0
inr_val = 1 if inr > 2.3 else 0

rotterdam_score = (1.27 * he_val) + (1.04 * ascites_val) + (0.72 * inr_val) + (0.004 * bilirubin)

st.write(f"### Rotterdam Score: {rotterdam_score:.2f}")
