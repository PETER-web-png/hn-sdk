from hn_sdk import HNClient

client = HNClient()

for sid in client.top_stories(limit=10):
    item = client.get_item(sid)
    print(f"[{item.score:>4}] {item.title}")
    if item.url:
        print(f"       {item.url}")
    print()
