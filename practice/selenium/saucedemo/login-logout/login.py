from selenium.webdriver.common.by import By
import time

def login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)