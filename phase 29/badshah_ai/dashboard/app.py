import streamlit as st
from badshah_ai.core.brain import Brain

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2.9 Testing + Optimization")
brain = Brain()
tab1, tab2 = st.tabs(["Chat", "QA"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Smoke Test"):
            st.code(brain.run("test smoke"))
        if st.button("All Tests"):
            st.code(brain.run("test all"))
    with c2:
        if st.button("Performance"):
            st.code(brain.run("perf check"))
        if st.button("Dependency Audit"):
            st.code(brain.run("dependency audit"))
    with c3:
        if st.button("Error Report"):
            st.write(brain.run("error report"))
        if st.button("Bug Template"):
            st.write(brain.run("bug template"))
    if st.button("QA Checklist"):
        st.code(brain.run("qa checklist"))
