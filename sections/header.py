import streamlit as st
from constants import CURRENT_VERSION


def header():
    col1, col2, col3, _ = st.columns([3, 1, 3, 5])
    col1.image("static/cai_logo.png")
    col2.markdown("## ×")
    col3.image("static/hn_logo.png")

    st.markdown(
        f"<h1>Hacker News Analyzer<small>{CURRENT_VERSION}</small></h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """Welcome! 👋 This is a simple example on using Streamlit as the UI for your CrewAI agents .
        Here you can ask something like __"Analyze the latest trends on Hacker News"__ ✨"""
    )

    st.divider()
