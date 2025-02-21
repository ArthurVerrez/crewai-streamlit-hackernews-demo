import streamlit as st
from sections.metadata import metadata
from sections.header import header
from sections.input_form import input_form
from sections.response import response
from sections.footer import footer
from sections.sidebar import sidebar

metadata()
sidebar()
header()
input_form()

if st.session_state.instructions and st.session_state.llm_id:
    with st.spinner("Processing...", show_time=True):
        response()

footer()
