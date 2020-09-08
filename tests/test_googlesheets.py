import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime as dt
from googlesheets import GoogleSheets

def test_get_records():
	assert len(GoogleSheets.get_todays_records()) > 0

if __name__ == '__main__':
	test_get_records()