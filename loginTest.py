import unittest

from driverProvider import DriverProvider
from pageObjects.loginPage import LoginPage


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverProvider.driver

    def test_login(self):
        driver = self.driver
        driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
        login = LoginPage(driver)
        login.login('username', 'password123')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('Tests are executed')
