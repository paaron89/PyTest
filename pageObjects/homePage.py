class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.usernameBox_ID = 'email'
        self.passwordBox_ID = 'passwd'
        self.loginButton_ID = 'SubmitLogin'

    def login(self,username,password):


