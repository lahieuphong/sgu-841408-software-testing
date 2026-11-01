from selenium.webdriver.common.by import By
import time

def logout(driver):
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(3)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(3)