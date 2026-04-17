import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    
    num1_elem = browser.find_element(By.ID, "num1")
    num2_elem = browser.find_element(By.ID, "num2")
    num1 = int(num1_elem.text)
    num2 = int(num2_elem.text)
    print(f"Числа: {num1} + {num2}")

    
    total = num1 + num2
    total_str = str(total)
    print(f"Сумма: {total_str}")

    
    select_elem = browser.find_element(By.TAG_NAME, "select")
    select = Select(select_elem)
    select.select_by_visible_text(total_str)  

    
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    
    time.sleep(2)
    alert = browser.switch_to.alert
    print(f"🎉 КОД: {alert.text}")
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()
