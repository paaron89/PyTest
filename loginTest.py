import unittest

from selenium import webdriver
from pageObjects.loginPage import LoginPage

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/home/aron/Automation/drivers/chromedriver')

    def test_get_driver(self):
        driver = self.driver
        driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
        login = LoginPage(driver)
        login.login('username','password123')


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('Tests are executed')
