import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2 v1.1 GitHub Pro")

brain = Brain()
msg = st.text_area("Message")
if st.button("Send") and msg.strip():
    st.write(brain.run(msg))

st.subheader("Plugins")
for p in list_plugins():
    st.write(p)
