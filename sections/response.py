import streamlit as st
import agents.agents as agents
import json
import time
import os

from crewai.agents.crew_agent_executor import ToolResult
from crewai.agents.parser import AgentAction, AgentFinish
from crewai.tasks.task_output import TaskOutput

from constants import OUTPUT_FORMAT


def step_callback(x):
    if isinstance(x, ToolResult):
        with st.expander("🛠️ Called a Tool"):
            st.write(x.result)
    elif isinstance(x, AgentAction):
        with st.expander(
            f"🤖 Agent Action{' - Tool Call: **'+x.tool +'**' if x.tool else ''}"
        ):
            if x.thought:
                st.info(x.thought, icon="🤔")
            if x.tool:
                st.json(x.tool_input)
            st.write(x.result)
    elif isinstance(x, AgentFinish):
        with st.expander("🏁 Agent Finish"):
            if x.thought:
                st.info(x.thought, icon="🤔")
            st.text(x.output)
    else:
        with st.expander(f"Unhandled Step Type: {type(x)}"):
            st.write(x)


def task_callback(x):
    if isinstance(x, TaskOutput):
        with st.expander("🏁 Task Output"):
            st.write(x)
    else:
        with st.expander(f"Unhandled Step Type: {type(x)}"):
            st.write(x)


def response():

    # Set the OPENAI_API_KEY environment variable
    os.environ["OPENAI_API_KEY"] = st.session_state.api_key
    # We have to do it like this so that the knowledge sources can be embedded correctly

    if st.session_state.show_thinking_process:

        st.divider()
        st.markdown(
            f"<small>Thinking process callbacks</small>",
            unsafe_allow_html=True,
        )
    start_time = time.time()

    results = agents.run(
        request=st.session_state.instructions,
        llm_id=st.session_state.llm_id,
        step_callback=step_callback if st.session_state.show_thinking_process else None,
        task_callback=task_callback if st.session_state.show_thinking_process else None,
    )

    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(round(elapsed_time), 60)

    st.divider()
    st.markdown(
        f"<small>Output (took {(str(minutes) + 'min ') if minutes>0 else ''}{seconds}s)</small>",
        unsafe_allow_html=True,
    )

    if OUTPUT_FORMAT == "json":
        st.json(json.loads(results.raw))
    else:
        st.markdown(results.raw)

    with st.expander("🔍 Full Output"):
        st.write(results)
