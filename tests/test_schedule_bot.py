import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime as dt
from bot.bot import Bot
from schedule_bot import get_schedule

def run_from_cline():
	schedule = get_schedule()
	for post in schedule:
		assert(post.clocktime is not None and post.account_url is not None)

if __name__ == '__main__':
	run_from_cline()