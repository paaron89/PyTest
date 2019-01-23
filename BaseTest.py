from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BaseTest(TestCase):

    def test_get_driver(self):
        self.driver = webdriver.Chrome('/home/aron/Automation/drivers/chromedriver')
        self.driver.get('https://www.windguru.cz')
        search = self.driver.find_element(By.ID,'searchspot')

        search.clear()
        search.send_keys('iphone')
        search.send_keys(Keys.ENTER)




