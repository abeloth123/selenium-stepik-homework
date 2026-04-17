import time
from selenium import webdriver
from selenium.webdriver.common.by import By

LINK_V1 = "http://suninjuly.github.io/registration1.html"
LINK_V2 = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(LINK_V1)

    first_name = browser.find_element(By.CSS_SELECTOR, "input[required].first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, "input[required].second")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, "input[required].third")
    email.send_keys("test@mail.ru")

    phone = browser.find_element(By.CSS_SELECTOR, "input[placeholder*='phone']")
    phone.send_keys("+71234567890")

    address = browser.find_element(By.CSS_SELECTOR, "input[placeholder*='address']")
    address.send_keys("Moscow")

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()

    time.sleep(2)
    success_header = browser.find_element(By.TAG_NAME, "h1")
    assert "Congratulations" in success_header.text

finally:
    time.sleep(5)
    browser.quit()
