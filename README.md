# TTN Log to Google Sheets

Log uplinks, device and gateway status from [The Things Stack (TTN)](https://www.thethingsindustries.com/) to Google Sheets in real-time using **MQTT**, **TTN HTTP API**, and **Google Sheets API**.

---

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-API-green?logo=google-sheets)
![MQTT](https://img.shields.io/badge/MQTT-Client-orange?logo=eclipse-mosquitto)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## Features

- Real-time uplink logging from TTN via MQTT
- Gateway status check via TTN HTTP API
- Write logs into Google Sheets automatically
- Scheduled logging every 10 minutes and daily logs
- Local caching to reduce API calls and retry logic

---

## 🧰 Requirements

```bash
pip install -r requirements.txt
