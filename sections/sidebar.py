import streamlit as st


def sidebar():
    st.sidebar.container(height=30, border=False)

    st.sidebar.subheader("Quick Links")

    for image, link, text in [
        (
            "static/gh_fav_logo.png",
            "https://github.com/ArthurVerrez/crewai-streamlit-hackernews-demo",
            "Github Repository",
        ),
        (
            "static/cai_fav_logo.png",
            "https://docs.crewai.com/introduction",
            "CrewAI Documentation",
        ),
        (
            "static/hn_fav_logo.png",
            "https://news.ycombinator.com/",
            "Hacker News",
        ),
        (
            "static/st_fav_logo.png",
            "https://streamlit.io/",
            "Streamlit",
        ),
    ]:
        with st.sidebar.container(border=True):
            col1, col2 = st.columns([1, 6])
            col1.markdown(
                f'<image src="app/{image}" width="25" style="display: block; margin-left: auto; margin-right: auto; background:white; border-radius: 25%;">',
                unsafe_allow_html=True,
            )
            col2.markdown(f"[{text}]({link})")
