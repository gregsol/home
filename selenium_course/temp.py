# temporary file

from selenium import webdriver

browser = webdriver.Chrome()
link = "https://www.degreesymbol.net/"
browser.get(link)

try:
    link = browser.find_element_by_link_text("» Degree symbol examples")
    link.click()

    link = browser.find_element_by_partial_link_text("examples")
    link.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
