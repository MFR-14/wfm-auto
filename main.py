from flask import Flask
import gspread
from google.oauth2.service_account import Credentials
import os
import json

app = Flask(__name__)

# Scope akses
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Ambil credentials dari environment variable
creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)

client = gspread.authorize(creds)
spreadsheet = client.open_by_key("17SL1HE0YSyJCcq68znfPOFewUp1ctrHckBKUfHqEdh4")
sheet = spreadsheet.sheet1

@app.route("/")
def home():
    data = sheet.get_all_records()
    return {"data": data}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
