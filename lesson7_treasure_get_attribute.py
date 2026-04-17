import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    
    treasure_img = browser.find_element(By.ID, "treasure")
    
    
    x_value = treasure_img.get_attribute("valuex")
    print(f"Значение x из атрибута: {x_value}")
    
    
    y = calc(x_value)
    print(f"Вычислен y: {y}")

    
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
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