from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDownpage:
    DROP_MENU = (By.ID, 'dropdown')
    DROP_FIRST = (By.XPATH, '//*[@id="dropdown"]/option[1]')
    DROP_SECOND = (By.XPATH, '//*[@id="dropdown"]/option[2]')
    DROP_THIRD = (By.XPATH, '//*[@id="dropdown"]/option[3]')

    def __init__(self, driver):
        self.driver = driver

    def drop_down(self, index):
        driver = self.driver
        dropmenu = driver.find_element(*self.DROP_MENU)
        drop = Select(dropmenu)
        drop.select_by_index(index)
