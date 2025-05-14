import time
import threading
import paho.mqtt.client as mqtt
from config import USERNAME, PASSWORD, BROKER, PORT
from mqtt_handlers import on_connect, on_disconnect, on_message
from cache_utils import load_last_seen
from device_monitor import check_device_status

last_seen = load_last_seen()

def start_monitoring(interval=600):
    def loop():
        while True:
            check_device_status(last_seen)
            time.sleep(interval)
    threading.Thread(target=loop, daemon=True).start()

client = mqtt.Client(userdata={"last_seen": last_seen})
client.username_pw_set(USERNAME, PASSWORD)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.reconnect_delay_set(min_delay=5, max_delay=60)

client.connect(BROKER, PORT, 60)
start_monitoring()
client.loop_forever()
