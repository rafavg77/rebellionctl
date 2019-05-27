import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

currentDT = datetime.datetime.now()
value1=str(currentDT)
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Monitoreo-Casa").sheet1

# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)


row = [value1,"b8:8d:12:31:41:96 ","DeLorear"]
index = 1
sheet.append_row(row)