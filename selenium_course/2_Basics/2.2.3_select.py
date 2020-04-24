# https://stepik.org/lesson/228249/step/3?unit=200781

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id('num1').text)
    y = int(browser.find_element_by_id('num2').text)
    sum = x + y
    print(sum)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(sum))

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(20)
    browser.quit()
