# "Test case 9" đến "Test case 12"

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
    assert "inventory.html" in driver.current_url


# 9. Session Management (Quản lý phiên)
def test_session_management(driver):
    test_valid_login(driver)
    print("Waiting for session timeout (10 seconds)...")  # Thay đổi thời gian chờ nếu cần
    time.sleep(10)  # Đợi 10 giây để phiên hết hạn

    # Xóa tất cả cookie
    driver.delete_all_cookies()

    driver.refresh()

    # Kiểm tra rằng URL hiện tại không phải là trang inventory.html
    assert "saucedemo.com" in driver.current_url, f"Expected URL to contain 'saucedemo.com', but got: {driver.current_url}"
    assert "inventory.html" not in driver.current_url, f"Expected 'inventory.html' not to be in URL, but got: {driver.current_url}"


# 10. Access Control Testing (Kiểm tra quyền truy cập)
def test_access_control(driver):
    # Cố gắng truy cập trang inventory.html mà không cần đăng nhập
    driver.get("https://www.saucedemo.com/inventory.html")
    time.sleep(2)

    # Kiểm tra rằng URL hiện tại là trang chính (trang không có quyền truy cập)
    assert driver.current_url == "https://www.saucedemo.com/", f"Expected 'https://www.saucedemo.com/' but got '{driver.current_url}'"


# 11. Data Encryption Verification (Xác minh mã hóa dữ liệu)
def test_data_encryption(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)

    # Đảm bảo rằng URL sử dụng HTTPS
    assert "https" in driver.current_url, f"Expected URL to use HTTPS, but got: {driver.current_url}"

    # Kiểm tra xem giao thức có phải là HTTPS không
    assert driver.current_url.startswith("https://"), f"Expected URL to start with 'https://', but got: {driver.current_url}"


# 12. SQL Injection Attempt (Thử tấn công SQL Injection)
def test_sql_injection(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("admin' OR '1'='1")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Username and password do not match" in error_message