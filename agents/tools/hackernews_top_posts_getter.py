from typing import Type
from pydantic import BaseModel, Field
import requests

from crewai.tools import BaseTool
from utils import tool_wrapper


class HackerNewsTopPostsGetterInput(BaseModel):
    """Input for retrieving top Hacker News posts."""

    limit: int = Field(30, description="Number of top posts to retrieve (default: 30).")


class HackerNewsTopPostsGetterTool(BaseTool):
    """Tool to retrieve top Hacker News posts with title, score, and URL."""

    name: str = "hackernews_top_posts"
    description: str = (
        "Fetches top posts from Hacker News using the official Firebase API."
    )
    args_schema: Type[BaseModel] = HackerNewsTopPostsGetterInput

    @tool_wrapper(display_name="Hacker News Top Posts Tool")
    def _run(self, limit: int = 30) -> str:
        """
        Retrieves top Hacker News posts.

        Args:
            limit (int): Number of posts to retrieve.

        Returns:
            str: JSON string containing a list of top posts with 'title', 'score', and 'url'.

        Example:
            tool = HackerNewsTopPostsTool()
            output = tool._run(limit=5)
            # output -> JSON string of 5 top Hacker News posts
        """
        top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

        # Get top story IDs
        response = requests.get(top_stories_url)
        response.raise_for_status()
        top_story_ids = response.json()[:limit]

        results = []
        for story_id in top_story_ids:
            story_response = requests.get(item_url.format(story_id))
            story_response.raise_for_status()
            data = story_response.json()
            if data and "title" in data and "score" in data and "url" in data:
                results.append(
                    {
                        "title": data["title"],
                        "score": data["score"],
                        "url": data["url"],
                    }
                )
        return str(results)
