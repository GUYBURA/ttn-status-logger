import json
from datetime import datetime, timezone, timedelta
from cache_utils import save_last_seen

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected successfully.")
        client.subscribe("your ttn device topic")
    else:
        print("❌ MQTT connection failed:", rc)

def on_disconnect(client, userdata, rc):
    print(f"⚠️ Disconnected from MQTT broker (rc={rc})")

def on_message(client, userdata, msg):
    print("📩 Received message")
    try:
        payload = json.loads(msg.payload.decode())
        dev_id = payload["end_device_ids"]["device_id"]
        received_at = payload["received_at"][:26] + 'Z'
        timestamp_utc = datetime.strptime(received_at, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
        userdata['last_seen'][dev_id] = timestamp_utc
        th_time = timestamp_utc.astimezone(timezone(timedelta(hours=7)))
        print(f"[{dev_id}] Uplink at {th_time.strftime('%Y-%m-%d %H:%M:%S')} (GMT+7)")
        save_last_seen(userdata['last_seen'])
    except Exception as e:
        print("⚠️ Error decoding message:", e)
