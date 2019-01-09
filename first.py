import unittest
import time

from selenium import webdriver


#chrome_path = '/usr/local/lib/python2.7/site-packages/selenium/webdriver/chrome/webdriver.py'
sleep_t = 4
# Pay a bill - unauthenticated
google_url = "https://www.google.com"
inputarea_css = "#lst-ib"
button_css = 'input[type="submit"]'


class File2(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    # My Usage
    def test1(self):
        driver = self.driver
        driver.get(google_url)
        time.sleep(sleep_t)
        inputarea = self.driver.find_element_by_css_selector(inputarea_css)
        f=open("/app/f1.txt", "r")
        for line in f:
           print line
        inputarea.send_keys(line)
        time.sleep(sleep_t)
       # button = self.driver.find_element_by_css_selector(button_css)
       # button.click()

        time.sleep(sleep_t)

if __name__ == "__main__":
    unittest.main()