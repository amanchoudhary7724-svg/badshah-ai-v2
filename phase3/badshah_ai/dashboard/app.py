import streamlit as st
from badshah_ai.core.brain import Brain
from badshah_ai.config.settings import settings

st.set_page_config(page_title="BADSHAH-AI v2", layout="wide")
st.title("BADSHAH-AI v2 Dashboard")

@st.cache_resource
def get_brain():
    return Brain()

brain = get_brain()

tab_chat, tab_tools, tab_memory, tab_settings = st.tabs(["Chat", "Tools", "Memory", "Settings"])

with tab_chat:
    message = st.text_area("Message", height=120)
    if st.button("Send"):
        if message.strip():
            st.write(brain.run(message.strip()))

with tab_tools:
    st.subheader("Quick Commands")
    col1, col2 = st.columns(2)
    with col1:
        project_name = st.text_input("Create static website", "portfolio_site")
        if st.button("Create Website"):
            st.write(brain.run(f"create website {project_name}"))
    with col2:
        image_path = st.text_input("OCR image path")
        if st.button("Run OCR"):
            st.write(brain.run(f"ocr image {image_path}"))

with tab_memory:
    limit = st.slider("Recent memories", 1, 50, 10)
    for item in brain.memory.recent(limit):
        st.markdown(f"**{item['created_at']}** · `{item.get('tag','chat')}`")
        st.write("User:", item["query"])
        st.write("BADSHAH:", item["response"])
        st.divider()

with tab_settings:
    st.write("Workspace:", str(settings.safe_workspace))
    st.write("Memory DB:", str(settings.memory_db))
    st.write("Ollama URL:", settings.ollama_url)
    st.write("Default Model:", settings.default_model)
