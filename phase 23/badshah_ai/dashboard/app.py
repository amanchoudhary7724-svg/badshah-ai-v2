import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.plugins.manifest import list_plugins

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v2.3 Gmail + Calendar Agents")
brain = Brain()
tab1, tab2, tab3 = st.tabs(["Chat", "Productivity", "Plugins"])

with tab1:
    msg = st.text_area("Message")
    if st.button("Send") and msg.strip():
        st.write(brain.run(msg))

with tab2:
    st.subheader("Contact")
    name = st.text_input("Name")
    value = st.text_input("Email/Phone")
    if st.button("Add Contact") and name and value:
        st.write(brain.run(f"add contact {name} {value}"))
    if st.button("Show Contacts"):
        st.code(brain.run("contacts"))

    st.subheader("Email / Calendar Draft")
    target = st.text_input("Target", "Aman")
    msg2 = st.text_area("Message / Meeting details")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Email Draft") and msg2:
            st.write(brain.run(f"draft email {target} {msg2}"))
    with c2:
        if st.button("Followup") and msg2:
            st.write(brain.run(f"followup email {target} {msg2}"))
    with c3:
        if st.button("Meeting Invite") and msg2:
            st.write(brain.run(f"meeting invite {target} {msg2}"))
    if st.button("Show Drafts"):
        st.code(brain.run("show drafts"))
    if st.button("Show Calendar Drafts"):
        st.code(brain.run("show calendar drafts"))

with tab3:
    for p in list_plugins():
        st.markdown(f"**{p['name']}** — {p['description']}")
