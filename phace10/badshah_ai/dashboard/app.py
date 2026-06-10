import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.config.settings import settings
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2 — v1.0 Final")

@st.cache_resource
def get_brain():
    return Brain()

brain = get_brain()
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Chat","Production","Self Modify","Plugins","Settings"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Validate ENV"): st.code(brain.run("validate env"))
        if st.button("Smoke Test"): st.code(brain.run("smoke test"))
    with col2:
        if st.button("Status"): st.code(brain.run("status"))
        if st.button("Logs"): st.code(brain.run("logs"))
    with col3:
        if st.button("Release Package"): st.write(brain.run("release package"))
        if st.button("Changelog"): st.code(brain.run("changelog"))

with tab3:
    req = st.text_area("Improvement request", "self modify add feature")
    if st.button("Create Patch"):
        st.write(brain.run(req))
    if st.button("Show Patches"):
        st.code(brain.run("show patches"))
    if st.button("Apply Latest Patch"):
        st.write(brain.run("apply latest patch"))

with tab4:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")

with tab5:
    st.json(settings.as_dict())
