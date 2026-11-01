# "Test case 7"

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Use Chrome WebDriver
    driver.maximize_window()
    yield driver
    driver.quit()


# 1. Đăng nhập hợp lệ
def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()

    time.sleep(3)

    # Kiểm tra URL hiện tại
    assert "inventory.html" in driver.current_url


# 5.1 Thêm 1 sản phẩm vào giỏ hàng
def test_add_item_to_cart(driver):
    test_valid_login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(3)
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    time.sleep(3)
    assert cart_count == "1"


# 7. Xem giỏ hàng
def test_view_cart_functionality(driver):
    test_add_item_to_cart(driver)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    time.sleep(5)
    assert "cart.html" in driver.current_url, "URL không chứa 'cart.html'"