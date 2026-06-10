import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.config.settings import settings

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2 Phase 5 — Self Modification Safe Mode")

@st.cache_resource
def get_brain():
    return Brain()

brain = get_brain()

tab1, tab2, tab3, tab4 = st.tabs(["Chat","Self Modify","Tasks","Settings"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))
    if st.button("Export Workspace"):
        st.write(brain.run("export workspace"))

with tab2:
    req = st.text_area("Improvement request", "self modify improve dashboard UI")
    if st.button("Create Safe Patch Proposal"):
        st.write(brain.run(req))
    if st.button("Show Patches"):
        st.code(brain.run("show patches"))

with tab3:
    for t in brain.tasks.recent(20):
        st.write(t)

with tab4:
    st.write("Workspace:", settings.safe_workspace)
    st.write("Exports:", settings.export_dir)
    st.write("Memory DB:", settings.memory_db)
