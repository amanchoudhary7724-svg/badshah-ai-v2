import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2.6 PyQt Desktop UI")
brain = Brain()
tab1, tab2 = st.tabs(["Chat", "Desktop UI"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    st.code("installer\\START_DESKTOP_UI.bat")
    st.write("Use this to launch the PyQt6 Jarvis-style desktop interface.")
    st.subheader("Plugins")
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
