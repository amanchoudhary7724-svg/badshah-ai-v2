import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2.1 VS Code Coding Agent")
brain = Brain()
tab1, tab2, tab3 = st.tabs(["Chat", "Coding Agent", "Plugins"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    if st.button("Code Scan"):
        st.code(brain.run("code scan"))
    file_path = st.text_input("Explain file", "main.py")
    if st.button("Explain Code"):
        st.write(brain.run("code explain " + file_path))
    patch_req = st.text_area("Patch request", "add dark mode to dashboard")
    if st.button("Create Patch Proposal"):
        st.write(brain.run("code patch " + patch_req))
    if st.button("Run Tests"):
        st.code(brain.run("code test"))

with tab3:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
