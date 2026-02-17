import streamlit as st
from model import generate_explanation
from prompts import (build_prompt)

# Title
st.set_page_config(page_title="Explain My Prescription", layout="centered")
st.title("💊 Explain My Prescription")
st.write("A privacy-preserving tool to help patients understand their medicines")

# Privacy notice
st.info("🔒 All information is processed locally on this device. No data is stored or sent online.")

# Input form
with st.form("prescription_form"):
    medicine = st.text_input("Medicine name *", placeholder="e.g., Metformin")
    strength = st.text_input("Strength / Dosage *", placeholder="e.g., 500 mg")
    frequency = st.selectbox( "How often is it taken? (optional)", ["Not specified", "Once daily", "Twice daily", "Thrice daily"] )
    Age = st.text_input("Age *", placeholder="e.g., 20")
    Others = st.text_input("Other special cases", placeholder="e.g., Pregnant,disable etc.")
    submitted = st.form_submit_button("Explain this medicine")

# Output placeholder
if submitted:
    if not medicine:
        st.error("Please enter the medicine name.")
    else:
        #Build prompt
        prompt = build_prompt( medicine_name=medicine,
                               dosage=strength,
                               frequency=frequency,
                               patient_age=Age,
                               Others=Others)
        # Run model inference
        response = generate_explanation(prompt)
        print(response)
        # Display results
        st.subheader(f"Medicine: {medicine} {strength}, Age {Age},frequency: {frequency},Others:{Others}")

        st.markdown(response)

        st.warning(
            "⚠️ This information is for educational purposes only and does not "
            "replace advice from a doctor or pharmacist.")
    if st.button("TEST MODEL"):
        test = generate_explanation("Explain what Paracetamol is used for.")
        st.write(test)
        print(test)
