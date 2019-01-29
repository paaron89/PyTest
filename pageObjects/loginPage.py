from assertpy import assert_that
from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME_BOX = (By.ID, 'email')
    PASSWORD_BOX = (By.ID, 'passwd')
    LOGIN_BUTTON = (By.ID, 'SubmitLogin')
    ALERT_BOX = (By.XPATH, '//*[@id="center_column"]/div[1]')
    ALERT_BOX_XPATH = '//*[@id="center_column"]/div[1]'

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        driver = self.driver
        usernameBox = driver.find_element(*self.USERNAME_BOX)
        passwordBox = driver.find_element(*self.PASSWORD_BOX)
        loginButtonBox = driver.find_element(*self.LOGIN_BUTTON)

        usernameBox.clear()
        usernameBox.send_keys(username)
        passwordBox.clear()
        passwordBox.send_keys(password)
        loginButtonBox.click()

        assert_that(driver.find_element(*self.ALERT_BOX).text, 'Hibaüzenet').contains('email')
