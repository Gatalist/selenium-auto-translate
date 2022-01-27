import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
import pyperclip


class Browser():
	def __init__(self):
		self.browser = webdriver.Chrome()
		self.link_login = 'https://my.ctrs.com.ua/ru/auth/login'
		self.link_login_email = 'https://my.ctrs.com.ua/ru/auth/email'
		self.link_login_sms = 'https://my.ctrs.com.ua/ru/auth/sms_code'
		self.link_admin = 'https://my.ctrs.com.ua/contento'

	# открытие ссылок
	def openLink(self, link):
		self.browser.get(link)
		time.sleep(2.5)

	# первая авторизация / сохраняем cookies
	def getCoociesUser(self):
		self.openLink(self.link_login)
		
		print('Авторизация пользователя')
		while True:
			if self.link_login == self.browser.current_url or \
			   self.link_login_email == self.browser.current_url or \
			   self.link_login_sms == self.browser.current_url:
				
				time.sleep(3)
			else:
				time.sleep(5)
				print('Вы вошли в систему! Данные сохранены')
				break

		pickle.dump(self.browser.get_cookies(), open('session', 'wb'))

	# авторизация
	def authUser(self):
		self.openLink(self.link_login)

		for cookie in pickle.load(open('session', 'rb')):
			self.browser.add_cookie(cookie)
		
		print("Куки загружены")

	def corect_url(self, start_page, item_in_page):
		curent_page = self.browser.current_url
		link_split = curent_page.split('&')

		link_split[1] = f'start={start_page}'
		link_split[2] = f'length={item_in_page}'
		new_page = "&".join(link_split)
		
		print(new_page)
		self.openLink(new_page)
	

	def next_url_translate(self, item_in_page):
		curent_page = self.browser.current_url
		link_split = curent_page.split('&')

		start_num = int(link_split[1][6:])
		link_split[1] = f'start={start_num + item_in_page}'
		new_page = "&".join(link_split)
		print(new_page)

		return new_page

	def login(self):
		try:
			self.authUser()
		except:
			self.getCoociesUser()


class Base(Browser):
	def __init__(self):
		super().__init__()
		self.list_options = {}
		self.options = "//select[@id='model_name']/option"  # выбор модели для перевода
		self.table = "//table[@id='data-table']/tbody/tr"
		self.table_name = "//table[@id='data-table']/tbody/tr/td[2]"
		self.modal = "//div[@id='name']/div"
		self.table_filter = "//div[@id='data-table_filter']"

	def search_model(self):
		elem_num = 1
		for option in self.browser.find_elements_by_xpath(self.options):
			print("[", str(elem_num), "]", option.text)
			self.list_options[elem_num] = option.text
			elem_num += 1
			
	def search_option(self):
		select = int(input("\nВведите номер модели со списка: "))
		
		if not isinstance(select, int):
			print("\nОшибка ввода, введите Число!")
			self.select_option()

		return select

	def select_options(self):
		select_option = self.search_option()
		for key, value in self.list_options.items():
			if key == select_option:
				print("\nВыбраная модель [", value, "]")
				for option_click in self.browser.find_elements_by_xpath(self.options):
					if option_click.text == value:
						option_click.click()
						time.sleep(2)

	def centre_browser(self):
		self.browser.find_element_by_xpath(self.table_filter).location_once_scrolled_into_view
		time.sleep(1)

	def range_item_translate(self, page_checking, item_in_page):
		for page in range(1, page_checking + 1):
			print(page)
			self.centre_browser()
			self.for_elem_in_table()
				
			print([f"страница - {page} | Все атрибуты переведены [+]"])
			if page < page_checking:
				new_page = self.next_url_translate(item_in_page)
				self.openLink(new_page)
			else:
				self.openLink(self.browser.current_url)


	def new_page(self, link, page):
		self.browser.execute_script("window.open('');")
		self.browser.switch_to.window(self.browser.window_handles[page])
		self.openLink(link)

	def tab_page(self, page):
		self.browser.switch_to.window(self.browser.window_handles[page])

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