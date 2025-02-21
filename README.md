# CrewAI Streamlit Hacker News Demo

## Overview

A simple demonstration of leveraging a CrewAI agent inside a Streamlit UI to analyze top posts from Hacker News. This project creates a crew, a tool, an agent, a task and leverages knowledge to showcase basic functionalities.

![App Screenshot](app_screenshot.png)

## Installation

```bash
git clone https://github.com/ArthurVerrez/crewai-streamlit-hackernews-demo
cd crewai-streamlit-hackernews-demo
python -m venv env
```

Activate the environment:
On **Mac/Linux**

```bash
source env/bin/activate
```

On **Windows**

```bash
env\Scripts\activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. _\[OPTIONAL\]_ set `LLM_API_KEY` in the `.env` file before starting the app.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Links

- [CrewAI](https://crewai.com/)
- [Hacker News](https://news.ycombinator.com/)
- [Streamlit](https://streamlit.io/)

## Disclaimer

Not affiliated with CrewAI or Hacker News.
