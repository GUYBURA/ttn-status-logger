import requests
from datetime import datetime, timezone, timedelta
from config import TENANT_DOMAIN, GATEWAY_API_KEYS

def get_gateway_status(gateway_id):
    url = f"https://{TENANT_DOMAIN}/api/v3/gs/gateways/{gateway_id}/connection/stats"
    token = GATEWAY_API_KEYS.get(gateway_id)

    if not token:
        return "UNKNOWN", "❌ ไม่พบ API Key สำหรับ gateway นี้"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    try:
        res = requests.get(url, headers=headers, timeout=5)
        if res.status_code == 200 and res.text.strip():
            data = res.json()
            last_seen = data.get("last_status_received_at")
            if last_seen:
                timestamp = datetime.strptime(last_seen[:26] + "Z", "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
                diff = datetime.now(timezone.utc) - timestamp
                th_time = timestamp.astimezone(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S")
                return ("ONLINE" if diff < timedelta(minutes=30) else "OFFLINE", th_time)
            return "OFFLINE", "ไม่มีการส่ง status"
        return "OFFLINE", f"HTTP {res.status_code}"
    except Exception as e:
        return "ERROR", str(e)
