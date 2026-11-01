# "Test case 1" đến "Test case 6"

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

# 2. Đăng nhập không hợp lệ
def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(10)

    # Lấy thông báo lỗi từ phần tử
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username and password do not match" in error_message


# 3. Tên người dùng/Mật khẩu trống
def test_empty_username_password(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(10)

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username is required" in error_message


# 4. Chức năng đăng xuất
def test_logout_functionality(driver):
    test_valid_login(driver)

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(5)

    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(5)

    assert "saucedemo.com" in driver.current_url and "inventory.html" not in driver.current_url


# 5. Thêm sản phẩm vào giỏ hàng

# def test_add_item_to_cart(driver):
#     test_valid_login(driver)
#     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
#     time.sleep(3)
#     cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
#     time.sleep(3)
#     assert cart_count == "1"


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


# 6. Xóa sản phẩm khỏi giỏ hàng

# def test_remove_item_from_cart(driver):
#     test_add_item_to_cart(driver)
#
#     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
#     time.sleep(3)
#     driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
#     time.sleep(3)
#     cart_items = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
#     time.sleep(3)
#     assert len(cart_items) == 0  # Kiểm tra giỏ hàng trống

def test_remove_all_items_from_cart(driver):
    test_add_items_to_cart(driver)

    # driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    remove_buttons = [
        (By.ID, "remove-sauce-labs-backpack"),
        (By.ID, "remove-sauce-labs-bike-light"),
        (By.ID, "remove-sauce-labs-bolt-t-shirt"),
        (By.ID, "remove-sauce-labs-fleece-jacket"),
        (By.ID, "remove-sauce-labs-onesie"),
        (By.ID, "remove-test.allthethings()-t-shirt-(red)"),
    ]

    for locator in remove_buttons:
        time.sleep(1)
        driver.find_element(*locator).click()

    time.sleep(1)
    cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    time.sleep(3)
    assert len(cart_badge) == 0