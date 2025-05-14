# TTN Log to Google Sheets

Log uplinks, device and gateway status from [The Things Stack (TTN)](https://www.thethingsindustries.com/) to Google Sheets in real-time using **MQTT**, **TTN HTTP API**, and **Google Sheets API**.

---

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-API-green?logo=google-sheets)
![MQTT](https://img.shields.io/badge/MQTT-Client-orange?logo=eclipse-mosquitto)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## Features

Real-time uplink monitoring from LoRaWAN devices  
Check if gateways or devices are online  
Automatically log results to Google Sheets  
Store recent status in local JSON cache  
Periodic status checking with configurable intervals

---

## Project Structure

```plaintext
mqtt_monitor/
├── main.py                # Main entry point
├── config.py              # Constants and configuration (API keys, devices)
├── mqtt_handlers.py       # MQTT on_connect/on_message handlers
├── cache_utils.py         # Load/save local status cache files
├── gateway_status.py      # Fetch gateway status via TTI HTTP API
├── google_logger.py       # Log data to Google Sheets
├── device_monitor.py      # Check device/gateway status and trigger logging
├── requirements.txt       # Python dependencies
└── credentials.json       # Your Google service account key (add manually)
```

---

## How to Create `credentials.json` for Google Sheets

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable these APIs:
   - **Google Sheets API**
   - **Google Drive API**
4. Go to **Credentials** from the left menu
5. Click **"Create Credentials" → "Service Account"**
6. Name it something like `sheets-logger` → Click **"Create and Continue"**
7. Grant it the **Editor** role (or "Basic → Editor")
8. After creation, go to the **Keys** tab → click **"Add Key" → JSON**
9. Download the file as `credentials.json`
10. Place `credentials.json` in the same directory as your Python code

---

## Important: Share Your Google Sheet with the Service Account

- Open your Google Sheet (e.g., `gapv2 tasks`)
- Click **Share**
- Add the email address found in your `credentials.json`, for example:

  ```
  sheets-logger@yourproject.iam.gserviceaccount.com
  ```

- Set permission to **Editor**

---

## Installation

1. Clone or download the repository
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Add your `credentials.json` to the project root
4. Configure `config.py`:
   - Set `USERNAME`, `PASSWORD`, and `GATEWAY_API_KEYS`
   - Define your `target_devices` and the `device_gateway_map`

---

## How to Run

1. Open terminal in the project directory
2. Start the monitor:

```bash
python main.py
```

### The system will:
- Connect to MQTT broker (TTI)
- Listen for uplinks from devices and store timestamps
- Check device and gateway status every 600 seconds (default)
- Write logs to Google Sheets if there are any changes or at scheduled times

---

## Google Sheet Format

1. Create a Google Sheet named **`gapv2 tasks`**
2. Add a worksheet named **`Log`**
3. Include the following column headers:

| Date | Time | GW1 | Dev1 | Dev2 | Dev3 | GW2 | Dev4 | Dev5 | GW3 | Dev6 | Dev7 |
|------|------|-----|------|------|------|-----|------|------|-----|------|------|

*Make sure the column order matches the script in `google_logger.py`.

---

## Configuration Guide

### 1. Set check interval in `main.py`

```python
def start_monitoring(interval=600)  # 600 seconds = 10 minutes
```

---

### 2. Edit configuration in `config.py`

```python
GATEWAY_API_KEYS = { ... }
target_devices = [ ... ]
device_gateway_map = { ... }
```

---

### 3. Adjust daily logging time in `device_monitor.py`

```python
def should_log_daily(now):
    return now.strftime("%H:%M") in ["23:58", "23:59", "00:00"]
```

The system logs at those exact times once per day.

---

### 4. Customize Sheet/Worksheet name in `google_logger.py`

```python
sheet = client.open("gapv2 tasks").worksheet("Log")
```

You can change these to match your actual sheet names.

---
