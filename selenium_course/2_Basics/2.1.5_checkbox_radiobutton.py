# https://stepik.org/lesson/165493/step/5

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_css_selector('#answer').send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']").click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']").click()

    button = browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(20)
    browser.quit()
