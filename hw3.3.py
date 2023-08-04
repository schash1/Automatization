import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/WebTable.html")
time.sleep(15)
switch_to = driver.find_element_by_link_text('SwitchTo')
switch_to.click()
alerts = driver.find_element_by_link_text('Alerts')
alerts.click()
time.sleep(15)
alert_ok_btn = driver.find_element_by_css_selector('#OKTab>[onclick="alertbox()"]')
alert_ok_btn.click()
alert = driver.switch_to.alert
alert_text = alert.text
if alert_text == "I am an alert box!":
    print(alert_text)
    alert.accept()
else:
    print('Ошибка')
driver.execute_script("window.open();")
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.get("https://demo.automationtesting.in/Alerts.html")
time.sleep(15)
alert_okcancel_btn = driver.find_element_by_link_text('Alert with OK & Cancel')
alert_okcancel_btn.click()
cancel_btn = driver.find_element_by_css_selector('#CancelTab>[onclick="confirmbox()"]')
cancel_btn.click()
confirm = driver.switch_to.alert
confirm.dismiss()
driver.execute_script("window.open();")
window_after = driver.window_handles[2]
driver.switch_to.window(window_after)
driver.get("https://demo.automationtesting.in/Alerts.html")
time.sleep(15)
alert_textbox = driver.find_element_by_link_text('Alert with Textbox')
alert_textbox.click()
textbox_btn = driver.find_element_by_css_selector('#Textbox>[onclick="promptbox()"]')
textbox_btn.click()
prompt = driver.switch_to.alert
prompt.send_keys("Ура! Задание выполнено!")
prompt.accept()
time.sleep(5)
driver.quit()
