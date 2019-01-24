import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/home/aron/Automation/drivers/chromedriver')

    def test_get_driver(self):
        self.driver.get('http://automationpractice.com')
        search = self.driver.find_element(By.ID, 'search_query_top')

        search.clear()
        search.send_keys('iphone')
        search.send_keys(Keys.ENTER)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('Tests are executed')
