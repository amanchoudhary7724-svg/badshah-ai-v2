import streamlit as st
from badshah_ai.core.brain import Brain

st.set_page_config(page_title="BADSHAH-AI v2", layout="wide")
st.title("BADSHAH-AI v2 Dashboard")

@st.cache_resource
def get_brain():
    return Brain()

brain = get_brain()

tab_chat, tab_memory = st.tabs(["Chat", "Memory"])

with tab_chat:
    message = st.text_area("Message", height=120)
    if st.button("Send"):
        if message.strip():
            st.write(brain.run(message.strip()))

with tab_memory:
    limit = st.slider("Recent memories", 1, 50, 10)
    for item in brain.memory.recent(limit):
        st.markdown(f"**{item['created_at']}**")
        st.write("User:", item["query"])
        st.write("BADSHAH:", item["response"])
        st.divider()
