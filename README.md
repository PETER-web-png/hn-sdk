# hn-sdk

A minimal Python SDK for the [HackerNews Firebase API](https://github.com/HackerNews/API).

## Install

```bash
pip install hn-sdk
```

## Usage

```python
from hn_sdk import HNClient

client = HNClient()

# Top 10 stories
for story_id in client.top_stories(limit=10):
    item = client.get_item(story_id)
    print(f"[{item.score}] {item.title}")

# User info
user = client.get_user("pg")
print(f"{user.id} — karma: {user.karma}, joined: {user.created.date()}")
```

## API

| Method | Description |
|--------|-------------|
| `get_item(id)` | Get a story/comment/job by ID |
| `get_user(name)` | Get a user profile |
| `top_stories(limit)` | Current top story IDs |
| `new_stories(limit)` | Newest story IDs |
| `best_stories(limit)` | Highest-scoring recent stories |
| `ask_stories(limit)` | Ask HN story IDs |
| `show_stories(limit)` | Show HN story IDs |
| `job_stories(limit)` | Job story IDs |
| `max_item_id()` | Largest item ID |
| `updates()` | Recent items and profiles |

## License

MIT
