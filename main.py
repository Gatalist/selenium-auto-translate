from translate_api import Translate
from models import Product_48, Product_attribute

# old translaters
################## Translates ########################
# translate = Translate()
# translate_txt = translate.google_translate   # google переводчик
# translate_txt = translate.microsoft_translate  # microsoft переводчик



# все атрибуты - перевод (товар - група значение свойство)
####################################################
# start_page = 0      # с какой записи начать
# item_in_page = 5    # количечтво записей на странице
# page_checking = 12  # количечтво проверяемых страниц

# product_48 = Product_48()
# product_48.start(start_page, page_checking, item_in_page)



# перевод атибутов в карточке товара
####################################################
start_page = 0      # с какой записи начать
item_in_page = 5    # количечтво записей на странице
page_checking = 12  # количечтво проверяемых страниц

product_attribute = Product_attribute()
link_translate = 'https://my.ctrs.com.ua/contento/content/catalog/properties/20575?search=&start=0&length=10&order=4&sort=asc&prop_id=20575&actual=1&without_groups=0'
product_attribute.start(start_page, page_checking, item_in_page, link_translate)




