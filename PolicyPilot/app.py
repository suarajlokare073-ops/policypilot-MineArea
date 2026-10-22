import streamlit as st

st.set_page_config(page_title="PolicyPilot", page_icon="🛡️")

st.title("🛡️ PolicyPilot")
st.write("MineArena Project")

policy = st.text_area("Policy text yaha dalo:")
question = st.text_input("Sawal pucho:")

if st.button("Check"):
    if "accident" in policy.lower():
        st.success("✅ Haan, Accident Cover Hai!")
    else:
        st.error("❌ Cover Nahi Hai")
    st.write(f"Tumne pucha: {question}")