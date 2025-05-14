from datetime import datetime, timezone, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def log_to_google_sheets(gateway_status, device_status):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("example").worksheet("example worksheets")

    now = datetime.now(timezone(timedelta(hours=7)))
    row = [
        now.strftime("%Y-%m-%d"),
        now.strftime("%H:%M:%S"),
        gateway_status.get("gateway-id", "UNKNOWN"),
        device_status.get("device-id-1", "UNKNOWN"),
    ]
    sheet.append_row(row)
