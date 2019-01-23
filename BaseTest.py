from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_driver():
    driver = webdriver.Chrome('/home/aron/Automation/drivers/chromedriver')
    driver.get('http://store.demoqa.com/')
    search = driver.find_element(By.NAME, 's')

    search.clear()
    search.send_keys('iphone')
    search.send_keys(Keys.ENTER)





get_driver()
