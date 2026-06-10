import streamlit as st
from badshah_ai.core.brain import Brain

st.set_page_config(page_title="BADSHAH-AI", layout="centered")
st.title("BADSHAH-AI v1.2")

brain = Brain()
msg = st.text_area("Message")
if st.button("Send") and msg.strip():
    st.write(brain.run(msg))

st.caption("Use CLI for full experience.")
