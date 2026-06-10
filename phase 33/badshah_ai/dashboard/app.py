import streamlit as st
from badshah_ai.core.brain import Brain

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v3.3 GitHub Clean Release")
brain = Brain()

tab1, tab2 = st.tabs(["Chat", "GitHub"])
with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))
with tab2:
    if st.button("Doctor"):
        st.code(brain.run("doctor"))
    if st.button("Repo Tree"):
        st.code(brain.run("repo tree"))
    if st.button("GitHub Guide"):
        st.code(brain.run("github guide"))
