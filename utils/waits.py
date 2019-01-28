from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import driverProvider


class Waits(driverProvider.DriverProvider):
    wait = WebDriverWait(driverProvider.DriverProvider.driver, 5)

    def wait_until_visible(self, webelement):
        Waits.wait.until(
            expected_conditions.visibility_of(webelement)
        )

    def wait_until_invisible(self, webelement):
        Waits.wait.until(
            expected_conditions.invisibility_of_element(webelement)
        )

    def wai_until_clickable(self, webelement):
        Waits.wait.until(
            expected_conditions.element_to_be_clickable(webelement)
        )
