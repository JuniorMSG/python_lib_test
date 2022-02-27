import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

json_file_name = 'autospreadsheet-307408-7669865df701.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1apjnr4BDSPLNqeEuxlz89NIgWtMJ25PkHcN-5ijjh_A/edit?usp=sharing'

doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet('시트1')