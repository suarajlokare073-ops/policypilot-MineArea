import streamlit as st

st.set_page_config(page_title="PolicyPilot", page_icon="🌾")
st.title("🌾 PolicyPilot - Farmer Insurance Helper")
st.write("Kisan ke liye insurance policy check karna ab easy!")

user_input = st.text_area("Apni problem yaha likho:", placeholder="Example: My crop damaged due to flood")

if st.button("Check Coverage"):
    if not user_input:
        st.warning("Pehle kuch likho!")
    else:
        text = user_input.lower()
        
        if "accident" in text or "injury" in text:
            st.success("✅ COVERED - Accident Cover hai!")
            st.write("📄 Documents: Medical Report, FIR copy, Aadhaar")
        
        elif "flood" in text or "baadh" in text or "water" in text:
            st.success("✅ COVERED - Natural Calamity Cover hai!")
            st.write("📄 Documents: Crop photo, Patwari report, Insurance copy")
            st.write("💰 Claim: 80% tak mil sakta hai")

        elif "drought" in text or "sukha" in text:
            st.success("✅ COVERED - Drought Cover hai!")
            st.write("📄 Documents: Weather report, Field photo")

        elif "tractor" in text or "machine" in text:
            st.success("✅ COVERED - Farm Equipment Cover hai!")
            st.write("📄 Documents: Bill, Repair estimate")

        else:
            st.error("❌ NOT COVERED - Is policy me cover nahi hai")
            st.write("Suggestion: Comprehensive policy lo")

st.divider()
st.caption("Made for MineArena 1.0 | Helps Farmers")
