from selenium import webdriver


class BaseTest:
    def get_driver(self):
        driver = webdriver.Chrome()
        driver.get('http://store.demoqa.com/')


    get_driver()
