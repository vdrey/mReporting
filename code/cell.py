import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = "https://spreadsheets.google.com/feeds"
credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)
gs = gspread.authorize(credentials)

gsheet = gs.open("testSheet")
ws = gsheet.worksheet("Sheet1")

print(ws.acell('G3').value)