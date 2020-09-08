from bot.bot import Bot
import logging
import sys

if __name__ == "__main__":
	#import logger
	logging.basicConfig(filename='bot.log',level=logging.DEBUG)
	logger = logging.getLogger('bash.bot_log')
	
	#parse args and run bot
	Bot(sys.argv[1],sys.argv[2])
