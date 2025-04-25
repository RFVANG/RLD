import streamlit as st

st.title("ACLF Classification Tool")

# User inputs
bilirubin = st.number_input("Enter bilirubin (µmol/L)", min_value=0.0, step=1.0)
creatinine = st.number_input("Enter creatinine (µmol/L)", min_value=0.0, step=1.0)
crrt = st.radio("Is the patient on CRRT?", ["no", "yes"])
circulation = st.radio("Is the patient on vasopressors?", ["no", "yes"])
inr = st.number_input("Enter INR", min_value=0.0, step=0.1)
he_grade = st.selectbox("Enter grade of hepatic encephalopathy (HE)", [0, 1, 2, 3, 4])
respiratory = st.radio("Is the patient on a ventilator?", ["no", "yes"])

# Classification function
def classify_aclf(bilirubin, creatinine, crrt, circulation, inr, he_grade, respiratory):
    liver_failure = bilirubin > 205
    kidney_failure = creatinine > 175 or crrt == "yes"
    circulation_failure = circulation == "yes"
    coagulation_failure = inr > 2.5
    brain_failure = he_grade >= 3
    respiratory_failure = respiratory == "yes"

    total_failing = sum([liver_failure, kidney_failure, circulation_failure,
                         coagulation_failure, brain_failure, respiratory_failure])

    explanation = []

    if liver_failure: explanation.append("Liver failure: bilirubin > 205 µmol/L")
    if kidney_failure: explanation.append("Kidney failure: creatinine > 175 µmol/L or CRRT")
    if circulation_failure: explanation.append("Circulatory failure: vasopressors")
    if coagulation_failure: explanation.append("Coagulation failure: INR > 2.5")
    if brain_failure: explanation.append("Brain failure: HE grade ≥ 3")
    if respiratory_failure: explanation.append("Respiratory failure: ventilator use")

    classification = ""
    mortality = ""

    if total_failing == 0:
        classification = "ACLF-0"
        mortality = "30-day mortality: ~4.3%"
    elif total_failing == 1:
        if kidney_failure:
            classification = "ACLF-1a"
            mortality = "30-day mortality: ~20%"
        elif brain_failure:
            if 133 <= creatinine <= 175:
                classification = "ACLF-1b"
                mortality = "30-day mortality: ~27.5%"
            elif creatinine < 133:
                classification = "ACLF-0"
                mortality = "30-day mortality: ~4.3%"
        else:
            if 133 <= creatinine <= 175:
                classification = "ACLF-1b"
                mortality = "30-day mortality: ~27.5%"
            elif creatinine < 133 and he_grade == 0:
                classification = "ACLF-0"
                mortality = "30-day mortality: ~4.3%"
            elif he_grade > 0:
                classification = "ACLF-1b"
                mortality = "30-day mortality: ~27.5%"
    elif total_failing == 2:
        classification = "ACLF-2"
        mortality = "30-day mortality: ~32.8%"
    elif total_failing == 3:
        classification = "ACLF-3a"
        mortality = "30-day mortality: ~70%"
    else:
        classification = "ACLF-3b"
        mortality = "30-day mortality: ~90%"

    return classification, mortality, explanation, total_failing

# Run and display results
if st.button("Classify ACLF"):
    classification, mortality, explanation, total_failing = classify_aclf(
        bilirubin, creatinine, crrt, circulation, inr, he_grade, respiratory
    )

    st.markdown(f"### Result: **{classification}**")
    st.markdown(f"**{mortality}**")
    st.markdown(f"Number of organ systems failing: **{total_failing}**")
    
    with st.expander("Explanation of failing organ systems"):
        for item in explanation:
            st.write("- " + item)