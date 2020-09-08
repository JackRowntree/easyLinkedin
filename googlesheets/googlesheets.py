import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime as dt

class GoogleSheets:
    'google sheets connection'
    def __init__(self,scope):
        # use creds to create a client to interact with the Google Drive API
        self.scope='https://www.googleapis.com/auth/spreadsheets.readonly'
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('googlesheets/client_secret.json', self.scope)
        self.client = gspread.authorize(self.creds)
        # Find a workbook by name and open the first sheet
        self.sheet = self.client.open("Linkedin Post Schedule").sheet1

    def get_records(self):
        # Extract and print all of the values
        list_of_hashes = self.sheet.get_all_records()
        return list_of_hashes

    def get_todays_records(self):
        records=self.get_records()
        todays_records = ([
            {'account_url':account,'clocktime ':dt.strptime(timestamp,"%I:%M %p")} 
            for timestamp, account in records.items() 
            if dt.strptime(timestamp,'%Y-%m-%d %H:%M:%S').date() == dt.now().date()
            ])
        return todays_records

