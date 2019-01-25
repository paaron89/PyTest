from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.usernameBox_ID = 'email'
        self.passwordBox_ID = 'passwd'
        self.loginButton_ID = 'SubmitLogin'
        self.alertBox_Xpath = '//*[@id="center_column"]/div[1]'

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 5)
        usernameBox = self.driver.find_element(By.ID, self.usernameBox_ID)
        passwordBox = self.driver.find_element(By.ID, self.passwordBox_ID)
        loginButtonBox = self.driver.find_element(By.ID, self.loginButton_ID)

        usernameBox.clear()
        usernameBox.send_keys(username)
        passwordBox.clear()
        passwordBox.send_keys(password)
        loginButtonBox.click()


        wait.until(
            expected_conditions.visibility_of(
                self.driver.find_element(By.XPATH, self.alertBox_Xpath)
            ))
        print("\n" + self.driver.find_element(By.XPATH, self.alertBox_Xpath).text)



