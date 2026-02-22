import gspread
from google.oauth2.service_account import Credentials

# Scope akses
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials
creds = Credentials.from_service_account_file(
    "wfm-auto.json",
    scopes=scope
)

# Authorize
client = gspread.authorize(creds)

# Buka pakai Spreadsheet ID (LEBIH AMAN)
spreadsheet = client.open_by_key("17SL1HE0YSyJCcq68znfPOFewUp1ctrHckBKUfHqEdh4")

# Ambil sheet pertama
sheet = spreadsheet.sheet1

# Print semua data
data = sheet.get_all_records()

print(data)
