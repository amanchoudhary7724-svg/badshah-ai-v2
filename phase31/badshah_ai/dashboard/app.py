import streamlit as st
from badshah_ai.core.brain import Brain
st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v3.1 Integrated Repo")
brain = Brain()
tab1, tab2, tab3, tab4 = st.tabs(["Chat", "Planner", "Plugins", "QA"])
with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip(): st.write(brain.run(msg))
with tab2:
    req = st.text_area("Plan", "create website portfolio and test smoke")
    if st.button("Preview"): st.code(brain.run("plan " + req))
    if st.button("Run Plan"): st.code(brain.run("run plan " + req))
with tab3:
    st.code(brain.run("plugin marketplace"))
    name = st.text_input("Plugin", "custom_notes")
    if st.button("Enable"): st.write(brain.run("plugin enable " + name))
    if st.button("Test Plugin"): st.write(brain.run("custom note hello from dashboard"))
with tab4:
    if st.button("Smoke Test"): st.code(brain.run("test smoke"))
    if st.button("QA Checklist"): st.code(brain.run("qa checklist"))
    if st.button("Release Package"): st.write(brain.run("release package"))
