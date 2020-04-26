# https://stepik.org/lesson/181384/step/8?unit=156009

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )

    browser.find_element_by_css_selector("button.btn").click()

    x = calc(int(browser.find_element_by_id('input_value').text))
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_id("solve").click()
finally:
    time.sleep(20)
    browser.quit()
