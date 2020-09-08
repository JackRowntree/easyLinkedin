from selenium import webdriver,common
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from random import randint
class Bot:
	def __init__(self,account_url,clocktime):
		options = webdriver.ChromeOptions()
		options.add_argument("headless")
		self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
		self.logger = logging.getLogger('bot_log')
		self.login_url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
		self.clocktime=clocktime
		self.account_url=account_url
		self.account_activity_url = self.account_url +'/detail/recent-activity/shares/'
		self.username=param_store.get_username(account_url)
		self.password=param_store.get_password(account_url)
		self.random_sleep()
		self.login()
		self.navigate()
		self.like_last()
		# self.username = 
	def safe_find(self,css_selector,wait=5):
		# try:
		thing=WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((By.CSS_SELECTOR,css_selector)))
		return thing
		# except common.exceptions.TimeoutException:
		# 	print('no')
		# 	return None		

	def random_sleep(self):
		time.sleep(randint(30,1170))

	def bot_log(self,text):
		self.logger.info(f'Account: {self.account}, Clocktime: self.clocktime |' + text )
	def login(self):
		self.bot_log('Logging in')
		self.driver.get(self.login_url)
		self.safe_find('input[autocomplete = "username"],#username').send_keys(self.username)
		self.safe_find("input[autocomplete = 'current-password'],#password").send_keys(self.password)
		self.safe_find('.sign-in-form__submit-button, .btn__primary--large.from__button--floating').click()

	def navigate(self,url=False):
		self.bot_log('Navigating to user page')
		if not url:
			url = self.account_activity_url
		self.driver.get(url)
		time.sleep(10)

	def get_last_social(self):
		self.bot_log('Getting last linkedin post')
		activity=self.safe_find('pv-recent-activity-detail__core-rail.core-rail',1)
		most_recent = activity.find_element_by_css_selector('.social-details-social-activity.update-v2-social-activity ember-view',1)[0]
		self.most_recent_post = most_recent

	def like_last(self):
		self.bot_log('liking last linkedin post')
		self.get_last_social()
		like_btn = self.most_recent_post.find_element_by_css_selector('artdeco-button__text.react-button__text',1)
		classes=mr.get_attribute('class')
		if 'react-button__text--like' in classes:
			like_btn.click()

	def commment_last():
		self.bot_log('Commenting on last linkedin post')
		txt_input = self.most_recent_post.find_element_by_css_selector('')

# install creates bash crontab cronjob to run this every morning at 10 assuming posts are around 11- midday
# 