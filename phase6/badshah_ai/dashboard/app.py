import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.config.settings import settings

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2 Phase 6 — Safe Patch Apply")

@st.cache_resource
def get_brain():
    return Brain()

brain = get_brain()

tab1, tab2, tab3, tab4 = st.tabs(["Chat","Self Modify","Tasks","Settings"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Backup Workspace"):
            st.write(brain.run("backup workspace"))
    with col2:
        if st.button("Export Workspace"):
            st.write(brain.run("export workspace"))

with tab2:
    req = st.text_area("Improvement request", "self modify add dark mode to dashboard")
    if st.button("Create Safe Patch Proposal"):
        st.write(brain.run(req))
    if st.button("Show Patches"):
        st.code(brain.run("show patches"))
    if st.button("Apply Latest Patch to Sandbox"):
        st.write(brain.run("apply latest patch"))

with tab3:
    for t in brain.tasks.recent(20):
        st.write(t)

with tab4:
    st.write("Workspace:", settings.safe_workspace)
    st.write("Sandbox:", settings.safe_workspace / "sandbox_project")
    st.write("Exports:", settings.export_dir)
    st.write("Memory DB:", settings.memory_db)
