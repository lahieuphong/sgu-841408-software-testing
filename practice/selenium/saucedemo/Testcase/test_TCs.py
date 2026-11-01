import pytest
from selenium import webdriver
from login import *
from logout import logout

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login(driver, "standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_invalid_login(driver):
    login(driver, "invalid_user", "wrong_password")
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message

def test_logout(driver):
    login(driver, "standard_user", "secret_sauce")
    logout(driver)
    assert "" in driver.current_url
