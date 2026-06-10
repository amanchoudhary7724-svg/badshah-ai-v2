import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v1.4 Feature Complete")

brain = Brain()
tab1, tab2, tab3 = st.tabs(["Chat", "Tools", "Plugins"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Health"): st.code(brain.run("health check"))
        if st.button("Memory"): st.code(brain.run("memory"))
    with c2:
        if st.button("Tasks"): st.code(brain.run("tasks"))
        if st.button("Release"): st.write(brain.run("release package"))
    with c3:
        name = st.text_input("Website name", "portfolio")
        if st.button("Create Website"): st.write(brain.run("create website " + name))

with tab3:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
