import unittest

from assertpy import assert_that

from driverProvider import DriverProvider
from pageObjects.loginPage import LoginPage
from utils.waits import Waits


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverProvider.driver

    def test_login(self):
        driver = self.driver

        loginpage = LoginPage(driver)

        driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
        loginpage.login('username', 'password123')

        Waits.wait_until_visible(loginpage.get_alert_box())
        assert_that(loginpage.get_alert_box().text, 'Error message check').contains('email')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('Tests are executed')
