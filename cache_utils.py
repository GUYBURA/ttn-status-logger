import json
from datetime import datetime, timezone, timedelta
from config import LAST_SEEN_FILE, STATUS_CACHE_FILE

def load_status_cache():
    try:
        with open(STATUS_CACHE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_status_cache(status_map):
    with open(STATUS_CACHE_FILE, "w") as f:
        json.dump(status_map, f)

def load_last_seen():
    try:
        with open(LAST_SEEN_FILE, "r") as f:
            data = json.load(f)
            return {k: datetime.fromisoformat(v) for k, v in data.items()}
    except FileNotFoundError:
        print("ℹ️ No previous last_seen file found.")
        return {}

def save_last_seen(last_seen):
    th_tz = timezone(timedelta(hours=7))
    with open(LAST_SEEN_FILE, "w") as f:
        json.dump({k: v.astimezone(th_tz).isoformat() for k, v in last_seen.items()}, f)
