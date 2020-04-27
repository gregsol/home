import unittest

from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            list = ["input[placeholder='Input your first name']", "input[placeholder='Input your last name']", "input[placeholder='Input your email']"]
            for a in list:
                    input = browser.find_element_by_css_selector(a)
                    input.send_keys("test")

            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Welcome text differs")
        finally:
            time.sleep(10)
            browser.quit()

    def test_reg2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            list = ["input[placeholder='Input your first name']", "input[placeholder='Input your last name']", "input[placeholder='Input your email']"]
            for a in list:
                    input = browser.find_element_by_css_selector(a)
                    input.send_keys("test")

            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Welcome text differs")

        finally:
            time.sleep(10)
            browser.quit()

if __name__ == "__main__":
    unittest.main()
