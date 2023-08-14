import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0, 600);")
selenium_book = driver.find_element_by_css_selector('[title="Selenium Ruby"]')
selenium_book.click()
reviews = driver.find_element_by_css_selector('.reviews_tab')
reviews.click()
stars = driver.find_element_by_class_name('star-5')
stars.click()
comment = driver.find_element_by_id('comment')
comment.send_keys("Nice book!")
name = driver.find_element_by_id('author')
name.send_keys('Sonya')
email = driver.find_element_by_id('email')
email.send_keys('schash1@mail.ru')
submit_btn = driver.find_element_by_id('submit')
submit_btn.click()
time.sleep(5)
driver.quit()
