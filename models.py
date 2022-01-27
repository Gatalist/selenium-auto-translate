import time
from selenium.common.exceptions import StaleElementReferenceException
from browser import Base


class Product_48(Base):
	def __init__(self):
		super().__init__()

	def for_elem_in_table(self):
		list_text = {}
		for elem in self.browser.find_elements_by_xpath(self.table_name):
			divs = elem.find_elements_by_tag_name('div')
			for div in divs:
				if (div.text).startswith('ru: '):
					a = div.find_element_by_tag_name('a')
					# a.get_attribute('title')
					text = a.text
					print("""""")
					print(text)
				# text = (div.text) #[17:-1]
				# print(text)
					self.tab_page(1)
					translate = self.start_translate(text)
					self.tab_page(0)
					print(translate)
					print("""""")
			
		
		# list_text = {}
		# for element in self.browser.find_elements_by_xpath(self.table):
		# 	i, name, change = 1, 2, 4
		# 	uk_translate = False
		# 	ru_translate = True
		# 	translate_local = True
		# 	away = True
		# 	for elem in element.find_elements_by_tag_name('td'):
		# 		if i == name:
		# 			for div in elem.find_elements_by_tag_name('div'):
		# 				if (div.text).startswith('uk: '):
		# 					uk = elem.find_element_by_tag_name('a')
		# 					if (uk.text).startswith('Нет'):
		# 						uk_translate = True
		# 				if (div.text).startswith('ru: '):
		# 					ru = elem.find_element_by_tag_name('a')
		# 					if (ru.text).startswith('Есть'):
		# 						ru_translate = False
		# 						text = (div.text)[17:-1]
		# 						# self.tab_page(1)
		# 						# translate = self.start_translate(text)
		# 						# self.tab_page(0)
		# 						list_text[text] = text
								
								# print(text_t)

				# if i == change and uk_translate == ru_translate == translate_local:
					# self.tab_page(1)
					# text_t = self.start_translate(text)
					# self.tab_page(0)
		# print('->', list_text)

					# link_chage = elem.find_element_by_tag_name('a')
					# link_chage.click()

					# self.modal_open(text_t)
					# away = False
					
			# 	i += 1
			# if away == False:
			# 	break

	def modal_open(self, text_t):
		time.sleep(2)
		group_inp = self.browser.find_element_by_xpath(self.modal)
		
		if not group_inp:
			time.sleep(2)
			group_inp = self.browser.find_element_by_xpath(self.modal)

		name_ru = group_inp.find_element_by_name('name[ru]')
		name_uk = group_inp.find_element_by_name('name[uk]')
		print('ru:', name_ru.get_attribute('value'))
		print('uk:', name_uk.get_attribute('value'))

		# text = translate_txt(name_ru.get_attribute('value'))
		
		# self.tab_page(1)
		# text = self.start_translate(name_ru.get_attribute('value'))
		# self.tab_page(0)

		group_inp = self.browser.find_element_by_xpath(self.modal)
		name_uk = group_inp.find_element_by_name('name[uk]')
		name_uk.click()

		name_uk.send_keys(text_t)
		self.modal_save()
	
	def modal_save(self):
		modal_save_btn = self.browser.find_element_by_class_name("modal-footer")
		save_btn = modal_save_btn.find_element_by_class_name("btn-primary")
		print(save_btn.text)
		time.sleep(2)
		save_btn.click()
		time.sleep(2.5)

	def start(self, start_page, page_checking, item_in_page):
		self.login()
		self.openLink('https://my.ctrs.com.ua/contento/translations/fields?search=&start=0&length=50&order=0&sort=asc')
		self.search_model()
		self.select_options()

		self.new_page('https://translate.google.com/?hl=ru&tab=TT&sl=ru&tl=uk&op=translate', 1)
		self.tab_page(0)

		self.corect_url(start_page, item_in_page)

		self.range_item_translate(page_checking, item_in_page)



class Product_attribute(Base):
	def __init__(self):
		super().__init__()

	def for_elem_in_table(self):
		try:

			for attr in self.browser.find_elements_by_xpath("//table[@id='data-table']/tbody/tr/td[3]"):
				links = attr.find_elements_by_tag_name('a')

				for locate in links:
					ru = locate.get_attribute('data-name')
					uk = locate.get_attribute('data-name')
					
					if ru == 'ru':
						ru_text = locate.text
						print("ru: ", ru_text)

					if uk == 'uk' and locate.text == 'Пусто':
						if locate.text == 'Пусто':		
							locate.click()
							self.tab_page(1)
							translate = self.start_translate(ru_text)
							print("uk: ", translate)
							self.tab_page(0)
							attr.find_element_by_tag_name('input').send_keys(translate)
							btns = attr.find_elements_by_tag_name('button')

							for btn in btns:
								ok = btn.get_attribute('type')
								if ok == 'submit':
									btn.click()
									time.sleep(2)
									break
						else:
							print("ru: ", locate.text)
		
		except StaleElementReferenceException:
			print(['Атрибут переведен [+]'])			


	def start(self, start_page, page_checking, item_in_page, link_translate):
		self.login()
		self.openLink(link_translate)
		self.corect_url(start_page, item_in_page)

		self.new_page('https://translate.google.com/?hl=ru&tab=TT&sl=ru&tl=uk&op=translate', 1)
		self.tab_page(0)
		self.range_item_translate(page_checking, item_in_page)
