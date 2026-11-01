import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from get_chrome_driver_with_custom_user_agent import get_driver_with_custom_profile


OPENCART_DEMO_EMAIL = os.environ.get("OPENCART_DEMO_EMAIL", "")
OPENCART_DEMO_PASSWORD = os.environ.get("OPENCART_DEMO_PASSWORD", "")
if not OPENCART_DEMO_EMAIL or not OPENCART_DEMO_PASSWORD:
    raise SystemExit("Set OPENCART_DEMO_EMAIL and OPENCART_DEMO_PASSWORD before running this script.")

# Khởi tạo trình duyệt với hồ sơ người dùng tùy chỉnh
driver = get_driver_with_custom_profile(r'my_chrome_profile')

try:
    # Truy cập trang đăng nhập
    driver.get("https://demo.opencart.com/en-gb?route=account/login")

    # Nhập địa chỉ email
    email_input = driver.find_element(By.ID, "input-email")
    email_input.send_keys(OPENCART_DEMO_EMAIL)

    # Nhập mật khẩu
    password_input = driver.find_element(By.ID, "input-password")
    password_input.send_keys(OPENCART_DEMO_PASSWORD)

    # Nhấn nút đăng nhập
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Chờ một chút để trang tải
    time.sleep(3)

    # Kiểm tra xem đã đăng nhập thành công hay chưa
    current_url = driver.current_url
    expected_url = "https://demo.opencart.com/en-gb?route=account/account&customer_token="

    if current_url.startswith(expected_url):
        print("Đăng nhập thành công!")
    else:
        print("Đăng nhập không thành công!")

    # Nhấn vào logo để quay lại trang chính
    logo = driver.find_element(By.CSS_SELECTOR, "img[title='Your Store']")
    logo.click()

    # Chờ một chút để trang tải
    time.sleep(3)

    # Kiểm tra URL trang chính
    if driver.current_url == "https://demo.opencart.com/en-gb":
        print("Quay lại trang chính thành công!")
    else:
        print("Không thể quay lại trang chính!")

    # Điều hướng đến trang OpenCart
    driver.get("https://demo.opencart.com/")

    # Tạm dừng để xem trang
    time.sleep(1200)  # Dừng trong 20 phút

finally:
    # Đóng trình duyệt
    driver.quit()
