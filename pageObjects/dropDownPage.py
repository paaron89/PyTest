from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDownPage:
    DROP_MENU = (By.ID, 'dropdown')
    DROP_FIRST_XPATH = '//*[@id="dropdown"]/option[1]'
    DROP_SECOND_XPATH = '//*[@id="dropdown"]/option[2]'
    DROP_THIRD_XPATH = '//*[@id="dropdown"]/option[3]'

    def __init__(self, driver):
        self.driver = driver

    def drop_down(self, index):
        driver = self.driver
        dropmenu = driver.find_element(*self.DROP_MENU)
        drop = Select(dropmenu)
        drop.select_by_index(index)

    def get_drop_item_by_xpath(self, item):
        driver = self.driver
        dropmenu_item = driver.find_element_by_xpath(item)
        return dropmenu_item

    def get_drop_menu_size(self):
        driver = self.driver
        dropmenu = driver.find_element(*self.DROP_MENU)
        drop = Select(dropmenu)
        return len(drop.options)
