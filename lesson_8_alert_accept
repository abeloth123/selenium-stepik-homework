import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.alert.accept()
    time.sleep(1)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(2)
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    time.sleep(3)
    browser.quit()