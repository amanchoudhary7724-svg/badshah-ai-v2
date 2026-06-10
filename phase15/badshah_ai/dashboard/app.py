import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v1.5 Voice + Wake Word")

brain = Brain()
tab1, tab2, tab3 = st.tabs(["Chat", "Voice", "Plugins"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    st.code("scripts\\run_voice.bat")
    st.write("Wake word: badshah")
    st.write("Example: badshah help")

with tab3:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
