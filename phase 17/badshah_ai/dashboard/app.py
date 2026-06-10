import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v1.7 Advanced Memory")

brain = Brain()
tab1, tab2, tab3, tab4 = st.tabs(["Chat", "Memory", "Browser", "Plugins"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    memory_text = st.text_input("Remember")
    if st.button("Remember") and memory_text:
        st.write(brain.run("remember " + memory_text))
    search = st.text_input("Search memory")
    if st.button("Search") and search:
        st.write(brain.run("memory search " + search))
    if st.button("Show Recent Memory"):
        st.code(brain.run("memory"))

with tab3:
    url = st.text_input("URL", "https://example.com")
    if st.button("Title"): st.write(brain.run("browser title " + url))
    if st.button("Text"): st.text(brain.run("browser text " + url))
    if st.button("Screenshot"): st.write(brain.run("browser screenshot " + url))

with tab4:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
