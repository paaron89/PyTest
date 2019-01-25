from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.usernameBox_ID = 'email'
        self.passwordBox_ID = 'passwd'
        self.loginButton_ID = 'SubmitLogin'

    def login(self,username, password):
        usernameBox = self.driver.find_element(By.ID, self.usernameBox_ID)
        passwordBox = self.driver.find_element(By.ID, self.passwordBox_ID)
        loginButtonBox = self.driver.find_element(By.ID, self.loginButton_ID)

        usernameBox.clear()
        usernameBox.send_keys(username)

        passwordBox.clear()
        passwordBox.send_keys(password)

        loginButtonBox.click()
