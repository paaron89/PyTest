from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import driverProvider


class Waits(driverProvider.DriverProvider):
    wait = WebDriverWait(driverProvider.DriverProvider.driver, 5)

    @staticmethod
    def wait_until_visible(webelement):
        Waits.wait.until(
            expected_conditions.visibility_of(webelement)
        )
    @staticmethod
    def wait_until_invisible(webelement):
        Waits.wait.until(
            expected_conditions.invisibility_of_element(webelement)
        )
    @staticmethod
    def wai_until_clickable(webelement):
        Waits.wait.until(
            expected_conditions.element_to_be_clickable(webelement)
        )
