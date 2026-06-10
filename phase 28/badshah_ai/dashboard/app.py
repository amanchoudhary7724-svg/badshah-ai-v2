import streamlit as st
from badshah_ai.core.brain import Brain

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2.8 Self Updater")
brain = Brain()
tab1, tab2 = st.tabs(["Chat", "Updater"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    if st.button("Update Status"):
        st.code(brain.run("update status"))
    if st.button("Backup Before Update"):
        st.write(brain.run("update backup"))
    if st.button("Git Pull"):
        st.code(brain.run("update pull"))
    if st.button("Release Notes"):
        st.write(brain.run("release notes"))
    if st.button("GitHub Push Guide"):
        st.code(brain.run("github push guide"))
