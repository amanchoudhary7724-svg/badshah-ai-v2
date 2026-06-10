import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins
from badshah_ai.agents.agent_registry import list_agents

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2.0 Multi-Agent Planner")
brain = Brain()
tab1, tab2, tab3, tab4 = st.tabs(["Chat", "Planner", "Agents", "Plugins"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    plan_req = st.text_area("Plan request", "create website portfolio and export workspace")
    if st.button("Preview Plan"):
        st.code(brain.run("plan " + plan_req))
    if st.button("Run Plan"):
        st.code(brain.run("run plan " + plan_req))

with tab3:
    for a in list_agents():
        st.markdown(f"**{a['name']}** — {', '.join(a['skills'])}")

with tab4:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
