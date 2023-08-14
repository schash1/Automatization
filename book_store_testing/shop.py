import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

''' #Oтображение страницы товара
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
username = driver.find_element_by_id('username')
username.send_keys('schash1@mail.ru')
password = driver.find_element_by_id('password')
password.send_keys('AsdfgH123!@#')
login_btn = driver.find_element_by_css_selector('[value="Login"]')
login_btn.click()
logout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
shop = driver.find_element_by_id('menu-item-40')
shop.click()
html5_forms = driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]')
html5_forms.click()
html5_forms_title = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title.entry-title"), "HTML5 Forms"))
time.sleep(5)
driver.quit()
'''
''' #Kоличество товаров в категории
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
username = driver.find_element_by_id('username')
username.send_keys('schash1@mail.ru')
password = driver.find_element_by_id('password')
password.send_keys('AsdfgH123!@#')
login_btn = driver.find_element_by_css_selector('[value="Login"]')
login_btn.click()
logout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
shop = driver.find_element_by_id('menu-item-40')
shop.click()
html_category = driver.find_element_by_css_selector('.cat-item.cat-item-19>a')
html_category.click()
items_count = driver.find_elements_by_css_selector(".products.masonry-done>li")
if len(items_count) == 3:
    print("Отображается 3 товара")
else:
    print("Ошибка")
time.sleep(5)
driver.quit()
'''
''' #Cортировка товаров
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
username = driver.find_element_by_id('username')
username.send_keys('schash1@mail.ru')
password = driver.find_element_by_id('password')
password.send_keys('AsdfgH123!@#')
login_btn = driver.find_element_by_css_selector('[value="Login"]')
login_btn.click()
logout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
shop = driver.find_element_by_id('menu-item-40')
shop.click()
sort = driver.find_element_by_css_selector('[value="menu_order"]')
default_sorting_check = WebDriverWait(driver, 10).until(
    EC.element_to_be_selected(sort))
order_by = driver.find_element_by_css_selector('[name="orderby"]')
price_desc = Select(order_by)
price_desc.select_by_visible_text('Sort by price: high to low')
sort_2 = driver.find_element_by_css_selector('[value="price-desc"]')
price_desc_check = WebDriverWait(driver, 10).until(
    EC.element_to_be_selected(sort_2))
time.sleep(5)
driver.quit()
'''
''' # Oтображение, скидка товара
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
username = driver.find_element_by_id('username')
username.send_keys('schash1@mail.ru')
password = driver.find_element_by_id('password')
password.send_keys('AsdfgH123!@#')
login_btn = driver.find_element_by_css_selector('[value="Login"]')
login_btn.click()
logout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
shop = driver.find_element_by_id('menu-item-40')
shop.click()
android_qsg = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
android_qsg.click()
old_price = driver.find_element_by_css_selector(".price>del>.woocommerce-Price-amount.amount")
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"
new_price = driver.find_element_by_css_selector(".price>ins>.woocommerce-Price-amount.amount")
new_price_get_text = new_price.text
assert new_price_get_text == "₹450.00"
img = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images>a>img")))
img.click()
close_img = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
close_img.click()
time.sleep(5)
driver.quit()
'''
''' # Проверка цены в корзине 
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
shop = driver.find_element_by_id('menu-item-40')
shop.click()
html5_WAD_to_basket = driver.find_element_by_css_selector('[data-product_id="182"]')
html5_WAD_to_basket.click()
time.sleep(3)
count_in_cart = driver.find_element_by_css_selector(".cartcontents")
count_in_cart_get_text = count_in_cart.text
assert count_in_cart_get_text == "1 Item"
price_in_cart = driver.find_element_by_css_selector(".wpmenucart-contents>.amount")
price_in_cart_get_text = price_in_cart.text
assert price_in_cart_get_text == "₹180.00"
cart_btn = driver.find_element_by_css_selector(".wpmenucart-contents")
cart_btn.click()
subtotal = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Subtotal"]>span'), "₹180.00"))
total = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Total"]>strong>span'), "₹183.60"))
time.sleep(5)
driver.quit()
'''
''' # Pабота в корзине 
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
html5_WAD_to_basket = driver.find_element_by_css_selector('[data-product_id="182"]')
html5_WAD_to_basket.click()
time.sleep(3)
js_dsa_to_basket = driver.find_element_by_css_selector('[data-product_id="180"]')
js_dsa_to_basket.click()
time.sleep(3)
cart_btn = driver.find_element_by_css_selector(".cartcontents")
cart_btn.click()
time.sleep(3)
delete_item = driver.find_element_by_css_selector('td.product-remove>a')
delete_item.click()
time.sleep(5)
undo = driver.find_element_by_link_text('Undo?')
undo.click()
quantity = driver.find_element_by_css_selector('[title="Qty"]')
quantity.clear()
quantity.send_keys(3)
update_basket = driver.find_element_by_css_selector('[value="Update Basket"]')
update_basket.click()
js_dsa_quantity = driver.find_element_by_css_selector('[title="Qty"]')
js_dsa_quantity_check = js_dsa_quantity.get_attribute('value')
assert js_dsa_quantity_check == "3"
time.sleep(5)
apply_coupon = driver.find_element_by_css_selector('[value="Apply Coupon"]')
apply_coupon.click()
error = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-error'), "Please enter a coupon code."))
time.sleep(5)
driver.quit()
'''
''' # Покупка товара
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
html5_WAD_to_basket = driver.find_element_by_css_selector('[data-product_id="182"]')
html5_WAD_to_basket.click()
time.sleep(3)
cart_btn = driver.find_element_by_css_selector(".cartcontents")
cart_btn.click()
check_out = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a")))
check_out.click()
first_name = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys('Sonya')
last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('Ivanova')
email = driver.find_element_by_id('billing_email')
email.send_keys('schash1@mail.ru')
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('89175407244')
country = driver.find_element_by_id('s2id_billing_country')
country.click()
country_search = driver.find_element_by_id('s2id_autogen1_search')
country_search.send_keys('Russia')
name_country = driver.find_element_by_class_name('select2-match')
name_country.click()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_payment = driver.find_element_by_id('payment_method_cheque')
check_payment.click()
adress = driver.find_element_by_id('billing_address_1')
adress.send_keys('Tverskaya')
city = driver.find_element_by_id('billing_city')
city.send_keys('Moscow')
state = driver.find_element_by_id('billing_state')
state.send_keys('-')
postcode = driver.find_element_by_id('billing_postcode')
postcode.send_keys('111111')
place_order = driver.find_element_by_id('place_order')
place_order.click()
order = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))
payment = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tfoot>:nth-child(3)'), "Check Payments"))
time.sleep(5)
driver.quit()
'''
