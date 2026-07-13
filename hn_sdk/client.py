import requests
from typing import Any

from hn_sdk.types import HNItem, HNUser, item_from_dict, user_from_dict

BASE_URL = "https://hacker-news.firebaseio.com/v0"


class HNClient:
    def __init__(self, timeout: int = 10):
        self._session = requests.Session()
        self._timeout = timeout

    def _get(self, path: str) -> Any:
        resp = self._session.get(f"{BASE_URL}{path}", timeout=self._timeout)
        resp.raise_for_status()
        return resp.json()

    # --- Items ---

    def get_item(self, item_id: int) -> HNItem:
        data = self._get(f"/item/{item_id}.json")
        return item_from_dict(data)

    # --- Users ---

    def get_user(self, username: str) -> HNUser:
        data = self._get(f"/user/{username}.json")
        return user_from_dict(data)

    # --- Story IDs ---

    def top_stories(self, limit: int = 30) -> list[int]:
        return self._get("/topstories.json")[:limit]

    def new_stories(self, limit: int = 30) -> list[int]:
        return self._get("/newstories.json")[:limit]

    def best_stories(self, limit: int = 30) -> list[int]:
        return self._get("/beststories.json")[:limit]

    def ask_stories(self, limit: int = 30) -> list[int]:
        return self._get("/askstories.json")[:limit]

    def show_stories(self, limit: int = 30) -> list[int]:
        return self._get("/showstories.json")[:limit]

    def job_stories(self, limit: int = 30) -> list[int]:
        return self._get("/jobstories.json")[:limit]

    # --- Metadata ---

    def max_item_id(self) -> int:
        return self._get("/maxitem.json")

    def updates(self) -> dict[str, Any]:
        return self._get("/updates.json")
