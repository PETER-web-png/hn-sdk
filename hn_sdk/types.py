from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class HNUser:
    id: str
    created: datetime
    karma: int
    about: str | None = None
    submitted: list[int] = field(default_factory=list)


@dataclass
class HNItem:
    id: int
    type: str
    by: str | None = None
    time: datetime | None = None
    text: str | None = None
    dead: bool = False
    deleted: bool = False
    poll: int | None = None
    parent: int | None = None
    parts: list[int] = field(default_factory=list)
    descendants: int = 0
    score: int = 0
    title: str | None = None
    url: str | None = None


def item_from_dict(data: dict[str, Any]) -> HNItem:
    return HNItem(
        id=data["id"],
        type=data.get("type", ""),
        by=data.get("by"),
        time=datetime.fromtimestamp(data["time"]) if "time" in data else None,
        text=data.get("text"),
        dead=data.get("dead", False),
        deleted=data.get("deleted", False),
        poll=data.get("poll"),
        parent=data.get("parent"),
        parts=data.get("parts", []),
        descendants=data.get("descendants", 0),
        score=data.get("score", 0),
        title=data.get("title"),
        url=data.get("url"),
    )


def user_from_dict(data: dict[str, Any]) -> HNUser:
    return HNUser(
        id=data["id"],
        created=datetime.fromtimestamp(data["created"]),
        karma=data.get("karma", 0),
        about=data.get("about"),
        submitted=data.get("submitted", []),
    )
