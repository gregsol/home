import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_basket_button(browser):
    browser.get(link)
    button = len(browser.find_elements_by_css_selector('button.btn-aqq:dd-to-basket'))
    assert button != '1', 'Add to basket button is not present'
    time.sleep(10)