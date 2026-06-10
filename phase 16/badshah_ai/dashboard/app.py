import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v1.6 Browser Automation")

brain = Brain()
tab1, tab2, tab3, tab4 = st.tabs(["Chat", "Browser", "Voice", "Plugins"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    url = st.text_input("URL", "https://example.com")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Title"): st.write(brain.run("browser title " + url))
    with c2:
        if st.button("Text"): st.text(brain.run("browser text " + url))
    with c3:
        if st.button("Screenshot"): st.write(brain.run("browser screenshot " + url))

with tab3:
    st.code("scripts\\run_voice.bat")
    st.write("Wake word: badshah")

with tab4:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
