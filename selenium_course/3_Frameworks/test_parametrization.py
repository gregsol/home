import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

url_list = ['https://stepik.org/lesson/236895/step/1','https://stepik.org/lesson/236896/step/1','https://stepik.org/lesson/236897/step/1','https://stepik.org/lesson/236898/step/1','https://stepik.org/lesson/236899/step/1','https://stepik.org/lesson/236903/step/1','https://stepik.org/lesson/236904/step/1','https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('urls', url_list)
def test_correct_answer(browser, urls):
    link = f"{urls}"
    browser.get(link)
    browser.implicitly_wait(15)
    browser.find_element_by_tag_name('textarea').send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector('button.submit-submission').click()
    browser.implicitly_wait(5)
    result = browser.find_element_by_css_selector('pre.smart-hints__hint').text
    print(result)
    assert result == 'Correct!', \
        f'expected "Correct!", got {result}'
    message123 += result

