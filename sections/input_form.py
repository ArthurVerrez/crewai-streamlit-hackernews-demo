import os
import streamlit as st
from constants import LLM_OPTIONS


def input_form():
    form = st.form("agent_form")
    st.session_state.api_key = form.text_input(
        "OpenAI API Key _(only stored in your browser during this session)_",
        type="password",
        value=os.getenv("LLM_API_KEY") or "",
    )
    st.session_state.instructions = form.text_area(
        "Enter your instructions", height=100
    )

    st.session_state.llm_id = form.pills(
        "Model",
        options=LLM_OPTIONS.keys(),
        format_func=lambda option: LLM_OPTIONS[option],
        selection_mode="single",
        default=next(iter(LLM_OPTIONS.keys())),
    )

    st.session_state.show_thinking_process = form.toggle(
        "Show thinking process", value=True
    )
    form.form_submit_button("Submit", type="primary")
