# https://stepik.org/lesson/228249/step/8?unit=200781

from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    list = ["input[placeholder='Enter first name']", "input[placeholder='Enter last name']", "input[placeholder='Enter email']"]
    for a in list:
            input = browser.find_element_by_css_selector(a)
            input.send_keys("test")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
    browser.find_element_by_id('file').send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(20)

    browser.quit()
