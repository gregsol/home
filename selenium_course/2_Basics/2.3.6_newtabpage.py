# https://stepik.org/lesson/184253/step/6?unit=158843

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("button.btn").click()

    browser.switch_to.window(browser.window_handles[1])

    x = calc(int(browser.find_element_by_id('input_value').text))
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(25)

    browser.quit()
