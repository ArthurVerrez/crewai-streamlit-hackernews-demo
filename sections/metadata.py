import streamlit as st
from constants import DEFAULT_SESSION_STATE


def metadata():
    st.set_page_config(
        page_title="CrewAI Agent",
        page_icon="🤖",
        initial_sidebar_state="expanded",
    )
    with open("./static/style.css") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    st.session_state.update(DEFAULT_SESSION_STATE)
