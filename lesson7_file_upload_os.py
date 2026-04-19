import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("ivan@example.com")

    
    file_name = "temp_file.txt"
    with open(file_name, "w") as f:
        f.write("")  

    
    file_input = browser.find_element(By.ID, "file")
    file_path = os.path.abspath(file_name)
    file_input.send_keys(file_path)

    
    os.remove(file_name)

    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    
    time.sleep(2)
    alert = browser.switch_to.alert
    print(f"🎉 КОД: {alert.text}")
    alert.accept()

finally:
    time.sleep(3)
    browser.quit()