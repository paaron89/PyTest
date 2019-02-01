import unittest

from assertpy import assert_that

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

        assert_that(dropdown.get_drop_item_by_xpath(DropDownPage.DROP_FIRST_XPATH).text, 'DropDwonItem text is not ok'). \
            is_equal_to('Please select an option')

    def test_drop_menu_size(self):
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/dropdown')
        dropdown = DropDownPage(driver)
        dropdown.get_drop_menu_size()
        assert_that(dropdown.get_drop_menu_size(), 'The number of options are not OK').is_equal_to(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('\n' + 'Tests are executed')
