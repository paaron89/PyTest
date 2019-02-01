import unittest

from driverProvider import DriverProvider
from pageObjects.dropDownPage import DropDownPage


class DropDowntest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverProvider.driver

    def test_dropdown(self):
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/dropdown')
        dropdown = DropDownPage(driver)
        dropdown.drop_down(1)

    def test_drop_item_value(self):
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/dropdown')
        dropdown = DropDownPage(driver)
        dropdown.get_drop_item_by_xpath(DropDownPage.DROP_FIRST_XPATH)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('\n' + 'Tests are executed')
