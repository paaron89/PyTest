from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BaseTest(TestCase):

    def test_get_driver(self):
        self.driver = webdriver.Chrome('/home/aron/Automation/drivers/chromedriver')
        self.driver.get('http://automationpractice.com')
        search = self.driver.find_element(By.ID,'search_query_top')

        search.clear()
        search.send_keys('iphone')
        search.send_keys(Keys.ENTER)




