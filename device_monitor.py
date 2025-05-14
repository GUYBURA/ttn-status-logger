from datetime import datetime, timedelta, timezone
from config import target_devices, device_gateway_map, GATEWAY_API_KEYS
from gateway_status import get_gateway_status
from google_logger import log_to_google_sheets
from cache_utils import load_status_cache, save_status_cache
from config import LAST_SEEN_FILE

def should_log_daily(now):
    return now.strftime("%H:%M") in ["23:58", "23:59", "0:00"]

def check_device_status(last_seen):
    prev_status = load_status_cache()
    now = datetime.now(timezone(timedelta(hours=7)))
    gateway_status = {}
    current_status = {}
    device_status = {}
    changed = False

    for gw in GATEWAY_API_KEYS:
        status, detail = get_gateway_status(gw)
        print(f"{gw}: {status} (ล่าสุด: {detail})")
        gateway_status[gw] = status
        current_status[gw] = status
        if prev_status.get(gw) != status:
            changed = True

    print("\n🔌 End Device Status:")
    for dev in target_devices:
        seen = last_seen.get(dev)
        gw = device_gateway_map[dev]
        if gateway_status.get(gw) == "OFFLINE":
            device_status[dev] = "UNKNOWN"
            continue

        if seen:
            diff = now - seen.astimezone(timezone(timedelta(hours=7)))
            status = "ONLINE" if diff < timedelta(hours=1) else "OFFLINE"
            device_status[dev] = status
            current_status[dev] = status
            if prev_status.get(dev) != status:
                changed = True
        else:
            device_status[dev] = "OFFLINE"

    if changed or should_log_daily(now):
        log_to_google_sheets(gateway_status, device_status)

    save_status_cache(current_status)
