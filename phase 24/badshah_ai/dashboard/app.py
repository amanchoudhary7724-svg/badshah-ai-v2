import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2.4 Screen Vision")
brain = Brain()
tab1, tab2, tab3 = st.tabs(["Chat", "Screen Vision", "Plugins"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    if st.button("Take Screenshot"):
        st.write(brain.run("screen shot"))
    if st.button("Screen OCR"):
        st.code(brain.run("screen ocr"))
    img = st.text_input("Image path")
    if st.button("Image OCR") and img:
        st.code(brain.run("image ocr " + img))
    if st.button("Safety"):
        st.code(brain.run("screen safety"))

with tab3:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
