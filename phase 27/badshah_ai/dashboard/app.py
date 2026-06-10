import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2.7 Plugin Marketplace")
brain = Brain()
tab1, tab2, tab3 = st.tabs(["Chat", "Plugin Manager", "Built-ins"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    st.code(brain.run("plugin marketplace"))
    name = st.text_input("Plugin name", "custom_notes")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Enable"):
            st.write(brain.run("plugin enable " + name))
    with c2:
        if st.button("Disable"):
            st.write(brain.run("plugin disable " + name))
    test = st.text_input("Test command", "custom note hello from dashboard")
    if st.button("Run Plugin Command"):
        st.write(brain.run(test))

with tab3:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
