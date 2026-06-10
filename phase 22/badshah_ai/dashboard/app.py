import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2.2 Communication Agents")
brain = Brain()
tab1, tab2, tab3 = st.tabs(["Chat", "Communication", "Plugins"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    st.subheader("Contacts")
    name = st.text_input("Name")
    value = st.text_input("Phone/Email/Handle")
    if st.button("Add Contact") and name and value:
        st.write(brain.run(f"add contact {name} {value}"))
    if st.button("Show Contacts"):
        st.code(brain.run("contacts"))

    st.subheader("Draft")
    channel = st.selectbox("Channel", ["whatsapp","email","telegram","discord"])
    target = st.text_input("Target", "Aman")
    message = st.text_area("Message draft")
    if st.button("Create Draft") and message:
        st.write(brain.run(f"draft {channel} {target} {message}"))
    if st.button("Show Drafts"):
        st.code(brain.run("show drafts"))

with tab3:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
