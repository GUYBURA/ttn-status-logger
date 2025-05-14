APP_ID = "application id"
USERNAME = "user name from ttn" 
PASSWORD = "ttn api mqtt"
REGION = "ttn region"
BROKER = f"{REGION}.cloud.thethings.industries" 
PORT = 1883
TENANT_DOMAIN = "ttn domain"
LAST_SEEN_FILE = "last_seen.json"
STATUS_CACHE_FILE = "status_cache.json"

GATEWAY_API_KEYS = {
    "gateway-id": "api for gateway status"
}


target_devices = [
    "device-id-1", "device-id-1", "device-id-1"
]

# map sensor using which gateway
device_gateway_map = {
    "device-id-1": "gateway-id",

}
