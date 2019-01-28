from selenium.webdriver.common.by import By
from utils.waits import Waits


class LoginPage:
    USERNAME_BOX = (By.ID, 'email')
    PASSWORD_BOX = (By.ID, 'passwd')
    LOGIN_BUTTON = (By.ID, 'SubmitLogin')
    ALERT_BOX = (By.XPATH, '//*[@id="center_column"]/div[1]')

    wait = Waits()

    def __init__(self, driver):
        self.driver = driver

        self.alertBox_Xpath = '//*[@id="center_column"]/div[1]'

    def login(self, username, password):
        usernameBox = self.driver.find_element(*self.USERNAME_BOX)
        passwordBox = self.driver.find_element(*self.PASSWORD_BOX)
        loginButtonBox = self.driver.find_element(*self.LOGIN_BUTTON)

        usernameBox.clear()
        usernameBox.send_keys(username)
        passwordBox.clear()
        passwordBox.send_keys(password)
        loginButtonBox.click()

        LoginPage.wait.wait_until_visible(self.driver.find_element(*self.ALERT_BOX))



        # print("\n" + (*self.ALERT_BOX).text)
