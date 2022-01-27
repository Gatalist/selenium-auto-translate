import time
from browser import Base
from selenium.webdriver.common.keys import Keys
import pyperclip


class Google(Base):
	def __init__(self):
		super().__init__()
		self.link_google = 'https://translate.google.com/?hl=ru&tab=TT&sl=ru&tl=uk&op=translate'

	def start(self):
		self.openLink(self.link_google)

	def copy_text(self):
		button_coppy = self.browser.find_elements_by_xpath("//button")

		for name in button_coppy:
			if name.text == 'content_copy':
				name.click()
				time.sleep(1)
				print("###########")
				text = pyperclip.paste()
				print(text)
				print("###########")
				return text

	def clear_textarea(self):
		self.browser.find_element_by_xpath("//textarea").click()
		self.browser.find_element_by_xpath("//textarea").send_keys(Keys.CONTROL, 'a')
		time.sleep(1)
		self.browser.find_element_by_xpath("//textarea").send_keys(Keys.DELETE)

	def past_text(self, text):
		self.browser.find_element_by_xpath("//textarea").click()
		self.browser.find_element_by_xpath("//textarea").send_keys(text)
		time.sleep(3)

	def start_translate(self, text):
		# self.openLink(self.link_google)
		self.past_text(text)
		translate = self.copy_text()
		self.clear_textarea()
		return translate
