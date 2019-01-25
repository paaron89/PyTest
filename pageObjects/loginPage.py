from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.usernameBox_ID = 'email'
        self.passwordBox_ID = 'passwd'
        self.loginButton_ID = 'SubmitLogin'
        self.alertBox_Xpath = '//*[@id="center_column"]/div[1]/p'

    def login(self,username, password):
        usernameBox = self.driver.find_element(By.ID, self.usernameBox_ID)
        passwordBox = self.driver.find_element(By.ID, self.passwordBox_ID)
        loginButtonBox = self.driver.find_element(By.ID, self.loginButton_ID)
        alertBox = self.driver.find_element(By.XPATH, self.alertBox_Xpath)

        usernameBox.clear()
        usernameBox.send_keys(username)
        passwordBox.clear()
        passwordBox.send_keys(password)
        loginButtonBox.click()

