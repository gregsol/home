# https://stepik.org/lesson/184253/step/4?unit=158843

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = calc(int(browser.find_element_by_id('input_value').text))

    input = browser.find_element_by_id('answer').send_keys(x)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)

    browser.quit()
