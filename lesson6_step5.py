import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)  

    
    secret_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    print(f"Ищем ссылку с текстом: {secret_text}")

    
    secret_link = browser.find_element(By.LINK_TEXT, secret_text)
    secret_link.click()
    print("Кликнули по ссылке, ждём загрузки формы...")
    time.sleep(2)  

    
    print(f"Текущий URL: {browser.current_url}")

    
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    
    alert = browser.switch_to.alert
    print(f"КОД: {alert.text}")
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()
