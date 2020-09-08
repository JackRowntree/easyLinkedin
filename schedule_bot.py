from datetime import datetime as dt
import logging
from googlesheets import GoogleSheets
import subprocess



if __name__ == "__main__":
	#import logger
	logging.basicConfig(filename='bot_log',level=logging.DEBUG)

	#import schedule
	def get_schedule:
		schedule = GoogleSheet().get_todays_records()
		return schedule
	schedule = get_schedule()

	#schedule bot.py acording to import
	bashcommand = 'echo "python run_bot.py {account_url} {clocktime}" | at {clocktime}'
	for post in schedule:
		proc = subprocess.Popen(bashcommand.format(account_url=post.account_url, clocktime=post.clocktime).split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		(out, err) = proc.communicate()
		logger.INFO('Scheduling todays bot activity via subprocess:')
		logger.INFO(out)
		logger.INFO(err)