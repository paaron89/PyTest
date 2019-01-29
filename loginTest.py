import unittest

from driverProvider import DriverProvider
from pageObjects.loginPage import LoginPage
from utils.waits import Waits
from assertpy import  assert_that


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverProvider.driver

    def test_login(self):
        wait = Waits()
        driver = self.driver
        driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
        login = LoginPage(driver)
        login.login('username', 'password123')
        wait.wait_until_visible(driver.find_element_by_xpath(LoginPage.ALERT_BOX_XPATH))
        assert_that(driver.find_element_by_xpath(LoginPage.ALERT_BOX_XPATH).text,'Alert message').contains('email')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('Tests are executed')
