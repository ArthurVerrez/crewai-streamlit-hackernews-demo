#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from agents.crew import HackerNewsAnalyzer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run(request, llm_id, step_callback=None, task_callback=None):
    """
    Run the crew.
    """
    inputs = {
        "request": request,
        "today": datetime.today().strftime("%Y-%m-%d"),
    }

    try:
        return (
            HackerNewsAnalyzer(llm_id)
            .crew(step_callback=step_callback, task_callback=task_callback)
            .kickoff(inputs=inputs)
        )
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
