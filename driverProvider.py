from selenium import webdriver

class DriverProvider:
    def driver_provider(self):
        driver = webdriver.Chrome(executable_path='/home/aron/Automation/drivers/chromedriver')
        return driver
