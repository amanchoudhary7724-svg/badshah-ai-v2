import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2.5 LLM Router")
brain = Brain()
tab1, tab2, tab3 = st.tabs(["Chat", "Model Router", "Plugins"])

with tab1:
    msg = st.text_area("Message")
    role = st.selectbox("Role", ["default", "fast", "coding", "smart"])
    if st.button("Send") and msg.strip():
        st.write(brain.run(f"ask {role} {msg}"))

with tab2:
    if st.button("Show Models"):
        st.code(brain.run("models"))
    if st.button("Health"):
        st.code(brain.run("model health"))
    role2 = st.selectbox("Set active role", ["default", "fast", "coding", "smart"], key="role2")
    if st.button("Set Role"):
        st.write(brain.run("model use " + role2))

with tab3:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
