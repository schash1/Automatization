import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

''' # Pегистрация аккаунта
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
email = driver.find_element_by_id('reg_email')
email.send_keys('schash1@mail.ru')
password = driver.find_element_by_id('reg_password')
password.send_keys('AsdfgH123!@#')
register_btn = driver.find_element_by_css_selector('[value="Register"]')
register_btn.click()
time.sleep(5)
driver.quit()
'''
''' # Логин в систему
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
logout = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
time.sleep(5)
driver.quit()
'''