import streamlit as st
from badshah_ai.core.brain import Brain
st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v3.2 Real Run Fix Pack")
brain = Brain()
tab1, tab2, tab3 = st.tabs(["Chat", "Doctor", "Plugins"])
with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip(): st.write(brain.run(msg))
with tab2:
    if st.button("Doctor"): st.code(brain.run("doctor"))
    if st.button("Smoke Test"): st.code(brain.run("test smoke"))
    if st.button("QA Checklist"): st.code(brain.run("qa checklist"))
with tab3:
    st.code(brain.run("plugin marketplace"))
    if st.button("Enable custom_notes"): st.write(brain.run("plugin enable custom_notes"))
