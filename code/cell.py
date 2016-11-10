import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = "https://spreadsheets.google.com/feeds"
credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)
gs = gspread.authorize(credentials)

def getVal(spreadSheet, workSheet, cell):

    sheet = gs.open(spreadSheet)
    ws = sheet.worksheet(workSheet)
    value = ws.acell(cell).value

    return value

def setVal(spreadSheet, workSheet, cell, newVal):
    
    sheet = gs.open(spreadSheet)
    ws = sheet.worksheet(workSheet)
    ws.update_acell(cell,newVal)