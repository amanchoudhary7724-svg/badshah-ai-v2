import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.config.settings import settings
st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2 Phase 4")
@st.cache_resource
def get_brain(): return Brain()
brain=get_brain()
tab1,tab2,tab3=st.tabs(["Chat","Tasks","Settings"])
with tab1:
    msg=st.text_area("Message")
    if st.button("Send") and msg.strip(): st.write(brain.run(msg))
    if st.button("Export Workspace"): st.write(brain.run("export workspace"))
with tab2:
    for t in brain.tasks.recent(20):
        st.write(t)
with tab3:
    st.write("Workspace:", settings.safe_workspace)
    st.write("Exports:", settings.export_dir)
