CURRENT_VERSION = 0.01

LLM_OPTIONS = {"gpt-4o-mini": "🧠 4o-mini", "gpt-4o": "🚀 4o"}

DEFAULT_SESSION_STATE = {
    "api_key": "",
    "instructions": "",
    "llm_id": next(iter(LLM_OPTIONS.keys())),
    "show_thinking_process": True,
}

OUTPUT_FORMAT = "markdown"  # or "markdown"
