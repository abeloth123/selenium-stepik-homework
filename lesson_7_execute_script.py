import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    
    answer_field = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView();", answer_field)

    
    answer_field.send_keys(y)

    
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    
    time.sleep(2)
    alert = browser.switch_to.alert
    print(f"🎉 КОД: {alert.text}")
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()