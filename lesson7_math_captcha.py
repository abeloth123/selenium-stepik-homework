import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)  

    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    print(f"Найден x: {x}")  

    
    y = calc(x)
    print(f"Вычислен y: {y}")

    
    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(y)

    
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    
    robots_rule_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_rule_radio.click()

    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    
    time.sleep(2)
    alert = browser.switch_to.alert
    print(f"🎉 КОД ДЛЯ ВВОДА: {alert.text}")
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()