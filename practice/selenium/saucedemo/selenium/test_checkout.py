# "Test case 8"

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


# 5. Thêm sản phẩm vào giỏ hàng
def test_add_items_to_cart(driver):
    test_valid_login(driver)

    item_ids = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bike-light",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-fleece-jacket",
        "add-to-cart-sauce-labs-onesie",
        "add-to-cart-test.allthethings()-t-shirt-(red)"
    ]

    for item_id in item_ids:
        time.sleep(1)
        driver.find_element(By.ID, item_id).click()

    time.sleep(1)

    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    time.sleep(3)

    assert cart_count == str(len(item_ids))


# 8. Checkout Process (Quy trình thanh toán)
def test_checkout_process(driver):
    test_add_items_to_cart(driver)

    shopping_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    shopping_cart_link.click()

    time.sleep(2)
    assert "cart.html" in driver.current_url

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    time.sleep(2)

    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("La")
    time.sleep(1)
    last_name_input.send_keys("Phong")
    time.sleep(1)
    postal_code_input.send_keys("1234")
    time.sleep(1)

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    time.sleep(5)
    assert "checkout-step-two.html" in driver.current_url

    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()

    time.sleep(5)
    assert "checkout-complete.html" in driver.current_url