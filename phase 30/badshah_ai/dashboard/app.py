import streamlit as st
from badshah_ai.core.brain import Brain

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v3.0 Final EXE Release")
brain = Brain()
tab1, tab2 = st.tabs(["Chat", "Release"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    if st.button("Smoke Test"):
        st.code(brain.run("test smoke"))
    if st.button("QA Checklist"):
        st.code(brain.run("qa checklist"))
    if st.button("Build EXE Guide"):
        st.code(brain.run("build exe guide"))
    if st.button("Release Package"):
        st.write(brain.run("release package"))
