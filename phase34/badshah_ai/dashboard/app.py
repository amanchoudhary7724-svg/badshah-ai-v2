import streamlit as st
from badshah_ai.core.brain import Brain

st.set_page_config(page_title="BADSHAH-AI", layout="wide")
st.title("BADSHAH-AI v3.4 Migration Helper")
brain = Brain()

if st.button("Doctor"):
    st.code(brain.run("doctor"))
if st.button("Repo Validate"):
    st.code(brain.run("repo validate"))
if st.button("Migration Checklist"):
    st.code(brain.run("migration checklist"))
