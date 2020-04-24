# https://stepik.org/lesson/228249/step/6?unit=200781

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = calc(int(browser.find_element_by_id('input_value').text))

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)

    input = browser.find_element_by_id('answer').send_keys(x)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']").click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']").click()

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    
    browser.quit()

